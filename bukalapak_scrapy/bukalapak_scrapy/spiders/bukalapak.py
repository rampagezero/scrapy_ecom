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
import gspread
import json
path.append(r'/home/dikapc/project/scrapy_old_v2/scrapy_ecom/bukalapak_scrapy/bukalapak_scrapy')
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
        
        yield scrapy.Request("https://www.bukalapak.com/p/mobil-part-dan-aksesoris/aksesoris-mobil/aksesoris-interior/3tf3hzj-jual-ambipur-pengharum-mobil-vanila-2ml",callback=self.parse)
    
    def parse(self,response):
        soup=BeautifulSoup(response.body,'html.parser')
        script=soup.find_all('script')
        gc=gspread.service_account('/home/dikapc/dashboard-osa-069587892c63.json')
        sh=gc.open_by_url('https://docs.google.com/spreadsheets/d/1keKW8fbYaX9CNI3oct1ON4mIz0wQEuxG0wedHUK1skw/edit?gid=0#gid=0')
        worksheet=sh.get_worksheet(0)
        data_link=pd.DataFrame(worksheet.get_all_records())
        ids=data_link[(data_link['eCustomer']=='Bukalapak') & (data_link['Availabilty']=='Active')].iloc[:,8]
        for i in script:
            if str(i).__contains__('access_token'):
               token=str(i).split('"access_token":')[1][1:].split(',"created_at"')[0][:-1] 
               
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

