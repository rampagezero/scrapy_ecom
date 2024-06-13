from typing import Iterable
import scrapy
import json
from scrapy.crawler import Crawler
from scrapy.crawler import CrawlerProcess
import pandas as pd
from bs4 import BeautifulSoup
import datetime
from scrapy.utils.project import get_project_settings
from sys import path
import json
path.append(r'/home/dikapc/project/scrapy/bukalapak_scrapy')
from bukalapak_scrapy.items import BukalapakItem
class BukalapakSpider(scrapy.Spider):
    name="bukalapak"
    download_delay=0.15
    # custom_settings = {
    #     "FEEDS": {
    #         "items.json":{
    #             "format": "json"
    #         }
    #     }
    # }
    # allowed_domains=['https://www.bukalapak.com','https://api.bukalapak.com/products']
    def start_requests(self):
        yield scrapy.Request("https://www.bukalapak.com/p/perawatan-kecantikan/hair-care/2dhr0v1-jual-pantene-gold-series-smooth-sleek-conditioner-320ml?from=brand-page&product_owner=brand_seller",callback=self.parse)
    def parse(self,response):
        soup=BeautifulSoup(response.body,'html.parser')
        script=soup.find_all('script')
        for i in script:
            if str(i).__contains__('access_token'):
               token=str(i).split('"access_token":')[1][1:].split(',"created_at"')[0][:-1] 
            ids=pd.read_excel(r'/home/dikapc/project/scrapy/bukalapak_scrapy/list_id_bukalapak.xlsx')['depan'].to_list()   
        for id in ids:
            yield scrapy.Request(f'https://api.bukalapak.com/products/{id}?access_token={token}',callback=self.request_stock,meta={'id':id})
    def request_stock(self,response):
            data=json.loads(response.body)
            item=BukalapakItem()
            item['url']=data['data']['url']
            item['stock']=data['data']['stock']
            item['skuid']=response.meta.get('id')
            yield item

settings=get_project_settings()
process=CrawlerProcess(settings)
process.crawl(BukalapakSpider)
process.start()

# class BukalapakBot(scrapy.Spider):
#     name="bukalapak"
#     # allowed_domains=['https://www.bukalapak.com','https://api.bukalapak.com/products']
#     def start_requests(self):
#         item=ItemLoader(BukalapakAccess)
#         print(item.load_item())
#         ids=pd.read_excel(r'D:\Daily\OSA\list_id_bukalapak.xlsx')['depan'].to_list()
#         for id in ids:
#             yield scrapy.Request(f'https://api.bukalapak.com/products/{id}?access_token=data')
#     def parse(self,response):
#         data=json.loads(response.body)
#         yield {'url':data['data']['url'],'stock':data['data']['stock']} 

