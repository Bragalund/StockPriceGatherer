# Stock Price Gatherer

Project for gathering stock-related data and storing it in a influx-database(time seriaes database).


## Viktig data

dato, openingtime, closingtime, highest_price, lowest_price, closing_price, volume_of_stocks_sold, name_of_company, ticker(kort navn), Børsverdi(hvis mulig), Belåningsgrad, siste


### utforskning

Nordnet api:
https://www.nordnet.no/api/2/accounts/1/performance/aggregated?include_today=true&from=2019-01-01
https://www.nordnet.no/api/2/accounts/1/performance/aggregated?include_today=true&from=2018-11-15
https://www.nordnet.no/api/2/accounts/1/performance/aggregated?include_today=true&from=2016-11-15
https://www.nordnet.no/api/2/instruments/historical/yields/16801605?from=2009-11-17 

Webscraper-chrome extension:
https://webscraper.io/

Scrapy:
https://scrapy.org/
python bibliotek for å lage webcrawler.



