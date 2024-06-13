# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

class LazadaOsaItem(scrapy.Item):
    name=scrapy.Field()
    url=scrapy.Field()
    link_id=scrapy.Field()
    sku=scrapy.Field()
    count_sold=scrapy.Field()
    stock=scrapy.Field()
    rating=scrapy.Field()
    review=scrapy.Field()
    price=scrapy.Field()
    shop_name=scrapy.Field()
    category=scrapy.Field()
    original_price=scrapy.Field()
    pass
