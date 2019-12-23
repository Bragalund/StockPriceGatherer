# -*- coding: utf-8 -*-
import scrapy


class Nordnetspider2Spider(scrapy.Spider):
    name = 'nordnetspider2'
    start_urls = ['https://www.nordnet.no/market/stocks?sortField=diff_pct&sortOrder=desc&page=1&exchangeCountry=NO',
                  'https://www.nordnet.no/market/stocks?sortField=diff_pct&sortOrder=desc&page=2&exchangeCountry=NO',
                  'https://www.nordnet.no/market/stocks?sortField=diff_pct&sortOrder=desc&page=3&exchangeCountry=NO']

    def parse(self, response):
        for stockline in response.xpath("//tbody/tr/td[@data-title='Navn']/a"):
            yield{
                'stockname': stockline.xpath("text()").get()
            }
