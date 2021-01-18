# Worldometers-Population_Web-Scraping-1
Year wise population data of each country using python scrapy

To run this complete file, download the repo:
1. from dir folder open python terminal
2. use command "scrapy crawl countries"
3. To save the data in csv file use command "scrapy crawl countries -o dataset.csv"


Scrapy by default don't use the "UTF-8" encoding ,so if the scraped data gets unicode then 
->go to setting.py in the project folder
->at the last add "FEED_EXPORT_ENCODING: 'utf-8' "


Scrapy by default set the user-agent as "scrapy", but due to which the spider can be banned immediately by some websites.
So use the user agent same as the browser like chrome, for this enter this in the setting.py file.
DEFAULT_REQUEST_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
   }
