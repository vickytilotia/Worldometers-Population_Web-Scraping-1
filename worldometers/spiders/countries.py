# -*- coding: utf-8 -*-
import scrapy
import logging


class CountriesSpider(scrapy.Spider):
    name = 'countries'
    allowed_domains = ['www.worldometers.info']  #remember no extra forward /
    start_urls = ['https://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        #title = response.xpath("//h1/text()").get()
        countries = response.xpath("//td/a")
        for country in countries:
            name = country.xpath(".//text()").get()  # use . when not using response
            link = country.xpath(".//@href").get()

            #This is the method to yield all name and links.
            """yield{

                'country_name' : name, 
                'country_link' : link  
            }"""
            
            #Method 1
            #as the country link is relative, we have to add https://www.worldometers.info to it.
            #absolute_url =  f"https://www.worldometers.info{link}"   # not that much efficient way
            
            #Method 2
            #So we use urljoin method
            """absolute_url = response.urljoin(link)
            yield scrapy.Request(url = absolute_url)""" 


            #Method 3
            #If we don't want the urljoin and all these confusion
            #yield response.follow(url=link) 

            #now we want to use this link to yield more information from these link pages
            # for that we have to make one more method.
            # and we have to also use callback to yiled response link
            yield response.follow(url=link, callback = self.parse_country, meta ={'country_name':name}) 
            # now response will be sent to parse_country method

    def parse_country(self,response):
        name = response.request.meta['country_name']
        rows = response.xpath("(//table[@class='table table-striped table-bordered table-hover table-condensed table-list'])[1]/tbody/tr")
        for row in rows:
            year = row.xpath(".//td[1]/text()").get()  # get method return the asked data in string
            population = row.xpath(".//td[2]/strong/text()").get()

            yield {
                'year' : year,
                'population' : population,
                #here we want the country name also from previous method
                #If we make a global varibal for that, then country name don't sync everytime
                #and we get the same country name everytime
                # for this problem we use request method
                # to send or sync data between two methods we use request.
                # for this we have to use "meta"
                'country_name' : name
            }
