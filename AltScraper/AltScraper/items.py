# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AltscraperItem(scrapy.Item):
    names = scrapy.Field()
    source = scrapy.Field()
    category = scrapy.Field()
