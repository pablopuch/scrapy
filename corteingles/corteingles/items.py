# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CorteinglesItem(scrapy.Item):
    # define the fields for your item here like:
    marca = scrapy.Field()
    price = scrapy.Field()
    name = scrapy.Field()
    pass
