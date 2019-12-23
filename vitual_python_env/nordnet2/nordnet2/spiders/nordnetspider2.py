# -*- coding: utf-8 -*-
import datetime
import scrapy


def convertStringToFloat(someString):
    return float(someString.replace(",","."))


class Nordnetspider2Spider(scrapy.Spider):
    name = 'nordnetspider2'
    start_urls = ['https://www.nordnet.no/market/stocks?sortField=diff_pct&sortOrder=desc&page=1&exchangeCountry=NO',
                  'https://www.nordnet.no/market/stocks?sortField=diff_pct&sortOrder=desc&page=2&exchangeCountry=NO',
                  'https://www.nordnet.no/market/stocks?sortField=diff_pct&sortOrder=desc&page=3&exchangeCountry=NO']

    def parse(self, response):
        for stockline in response.xpath("//tbody/tr"):

            dateToday = datetime.datetime.today()
            stockname = stockline.xpath("td[@data-title='Navn']/a/text()").get()
            lastPriceToday = stockline.xpath("td[@data-title='Siste']/span/span[@aria-hidden='true']/text()").get()
            lastPriceToday = convertStringToFloat(lastPriceToday)
            highestPriceToday = stockline.xpath("td[@data-title='Høy']/text()").get()
            highestPriceToday = convertStringToFloat(highestPriceToday)
            lowestPriceToday = stockline.xpath("td[@data-title='Lav']/text()").get()
            lowestPriceToday = convertStringToFloat(lowestPriceToday)
            turnover = stockline.xpath("td[@data-title='Omsetning']/span/span[@aria-hidden='true']/text()").get()
            turnover = convertStringToFloat(turnover)
            timeOfDay = stockline.xpath("td[@data-title='Tid']/span/text()").get()

            yield{
                'date': dateToday,
                'stockname': stockname,
                'last_price_today': lastPriceToday,
                'highest_price_today': highestPriceToday,
                'lowest_price_today': lowestPriceToday,
                'turnover': turnover,
                'time_of_day': timeOfDay
            }

