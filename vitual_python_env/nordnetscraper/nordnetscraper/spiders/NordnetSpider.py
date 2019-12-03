import scrapy


class NordnetSpider(scrapy.Spider):
    name = 'nordnet'
    start_urls = ['https://www.nordnet.no/market/stocks?sortField=diff_pct&sortOrder=desc&page=1&exchangeCountry=NO',
                  'https://www.nordnet.no/market/stocks?sortField=diff_pct&sortOrder=desc&page=2&exchangeCountry=NO',
                  'https://www.nordnet.no/market/stocks?sortField=diff_pct&sortOrder=desc&page=3&exchangeCountry=NO']

    def parse(self, response):
        for name in response.xpath("//div[@data-title='Navn']/span/a/text()"):
            yield {
                'stockname': name.strip()
            }
