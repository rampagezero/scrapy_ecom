# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html


# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class BukalapakItem(scrapy.Item):
    url=scrapy.Field()
    stock=scrapy.Field()
    skuid=scrapy.Field()
    pass
