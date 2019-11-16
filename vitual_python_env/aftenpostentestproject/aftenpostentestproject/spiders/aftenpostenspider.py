import scrapy


class NordnetSpider(scrapy.Spider):
    name = 'aftenposten'
    start_urls = ['https://www.aftenposten.no']

    def parse(self, response):
        for title in response.xpath("//h2/text()"):
            yield {
                'overskrift': title.get().strip()
                }


