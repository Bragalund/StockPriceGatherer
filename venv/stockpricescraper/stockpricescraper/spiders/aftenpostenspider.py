from datetime import datetime

import scrapy


class AftenpostenSpider(scrapy.Spider):
    name = 'aftenposten'
    start_urls = ['https://www.aftenposten.no']

    def parse(self, response):
        for title in response.xpath("//h2/text()"):
            date = datetime.today()
            yield {
                'dato': date,
                'overskrift': title.get().strip()
                }


