# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class BlibliItem(scrapy.Item):
    name=scrapy.Field()
    url=scrapy.Field()
    sku=scrapy.Field()
    product_code=scrapy.Field()
    item_code=scrapy.Field()
    stock=scrapy.Field()
    sold=scrapy.Field()
    rating=scrapy.Field()
    review=scrapy.Field()
    price=scrapy.Field()
    original_price=scrapy.Field()
    shop_name=scrapy.Field()