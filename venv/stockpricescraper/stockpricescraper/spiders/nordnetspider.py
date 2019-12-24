# -*- coding: utf-8 -*-
from datetime import datetime

import scrapy


def convertstringtofloat(somestring):
    return float(somestring.replace(",", "."))


class NordnetSpider(scrapy.Spider):
    name = 'nordnet'
    start_urls = ['https://www.nordnet.no/market/stocks?sortField=diff_pct&sortOrder=desc&page=1&exchangeCountry=NO',
                  'https://www.nordnet.no/market/stocks?sortField=diff_pct&sortOrder=desc&page=2&exchangeCountry=NO',
                  'https://www.nordnet.no/market/stocks?sortField=diff_pct&sortOrder=desc&page=3&exchangeCountry=NO']

    def parse(self, response):
        for stockline in response.xpath("//tbody/tr"):
            date_today = datetime.today()
            stockname = stockline.xpath("td[@data-title='Navn']/a/text()").get()
            last_price_today = stockline.xpath("td[@data-title='Siste']/span/span[@aria-hidden='true']/text()").get()
            last_price_today = convertstringtofloat(last_price_today)
            highest_price_today = stockline.xpath("td[@data-title='Høy']/text()").get()
            highest_price_today = convertstringtofloat(highest_price_today)
            lowest_price_today = stockline.xpath("td[@data-title='Lav']/text()").get()
            lowest_price_today = convertstringtofloat(lowest_price_today)
            turnover = stockline.xpath("td[@data-title='Omsetning']/span/span[@aria-hidden='true']/text()").get()
            turnover = convertstringtofloat(turnover)
            time_of_day = stockline.xpath("td[@data-title='Tid']/span/text()").get()

            yield {
                'date': date_today,
                'stockname': stockname,
                'last_price_today': last_price_today,
                'highest_price_today': highest_price_today,
                'lowest_price_today': lowest_price_today,
                'turnover': turnover,
                'time_of_day': time_of_day
            }
