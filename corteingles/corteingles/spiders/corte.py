import scrapy
from corteingles.items import CorteinglesItem
from scrapy.exceptions import CloseSpider
from scrapy.exporters import CsvItemExporter


class CorteSpider(scrapy.Spider):
    name = "corte"
    allowed_domains = ["www.elcorteingles.es"]
    start_urls = ["https://www.elcorteingles.es/electronica/accesorios-informatica/teclados/"]
    handle_httpstatus_list = [404] # to catch 404 with callback
    page_number = 1

    def parse(self, response):
        
        # stop spider on 404 response
        if response.status == 404: 
            raise CloseSpider('Recieve 404 response')
                
        # stop spider when no quotes found in response
        if len(response.css('div.product_preview-body')) == 0:
            raise CloseSpider('No quotes in response')
        
        exporter = CsvItemExporter(open('data.csv', 'w', encoding='utf-8-sig'))
        exporter.start_exporting()

        quote_item = CorteinglesItem()
        for quote in response.css('div.product_preview-body'):
            quote_item['marca'] = quote.css('div.product_preview-brand::text').get()
            quote_item['price'] = quote.css('span.price _big ::text').get()
            yield quote_item
            
        exporter.finish_exporting()

        # go to next page
        self.page_number += 1
        next_page = f'https://www.elcorteingles.es/electronica/accesorios-informatica/teclados/{self.page_number}/'
        yield response.follow(next_page, callback=self.parse)
