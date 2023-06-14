import scrapy

class PccomSpider(scrapy.Spider):
    name = "pccom"
    allowed_domains = ["www.pccomponentes.com"]
    start_urls = ["https://www.pccomponentes.com/teclados?page=1"]
    page_number = 1

    def parse(self, response):
        # stop spider on 404 response
        if response.status == 404: 
            return
                
        for quote in response.css('div.quote'):
            quote_item = {
                'name': quote.css('h1.h3 product-title::text').get(),
                'price': quote.css('span.product-price::text').get()
            }
            yield quote_item

        # go to next page
        self.page_number += 1
        next_page = f'https://www.pccomponentes.com/teclados?page={self.page_number}/'
        yield response.follow(next_page, callback=self.parse)
