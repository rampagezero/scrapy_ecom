from typing import Iterable
import scrapy
import json
from sys import path
from scrapy.crawler import Crawler
from scrapy.crawler import CrawlerProcess
import datetime
from scrapy.utils.project import get_project_settings
path.append('/home/dikapc/project/scrapy/blibli_scrapy/blibli')
from blibli.items import BlibliItem 

class BliblibotSpider(scrapy.Spider):
    name = "bliblibot"
    download_delay=1.5
    allowed_domains = ["www.blibli.com"]
    def start_requests(self):
        # 'downy-official-store':['DOS-60031',4],'olay-official-store':['OLY-60021',4],'p-g-pc':['PGG-18081',12],'tefal-official-store':['TEO-60051',5],'philips-lighting-official-store':['PHL-60022',11],'indohome-mart-official-store':['BLP-44298',3],'p-g-joglosemar-official-store':['PGJ-60021',4],
        # 'downy-official-store':['DOS-60031',4],'olay-official-store':['OLY-60021',4],'p-g-pc':['PGG-18081',12],'tefal-official-store':['TEO-60051',5],'philips-lighting-official-store':['PHL-60022',11],'indohome-mart-official-store':['BLP-44298',3],'p-g-joglosemar-official-store':['PGJ-60021',4],'p-g-surabaya-official-store':['PGS-60022',3],'bliblimart-personal-care-anak-p-g':['BLP-60063',2]
        list_store={'downy-official-store':['DOS-60031',4],'olay-official-store':['OLY-60021',4],'p-g-pc':['PGG-18081',12],'tefal-official-store':['TEO-60051',5],'philips-lighting-official-store':['PHL-60022',11],'indohome-mart-official-store':['BLP-44298',3],'p-g-joglosemar-official-store':['PGJ-60021',4],'p-g-surabaya-official-store':['PGS-60022',3],'bliblimart-personal-care-anak-p-g':['BLP-60063',2]}
        for store in list_store.keys():
            start=0
            for page in range(1,list_store[store][1]):
                png=f"https://www.blibli.com/backend/search/merchant/{list_store[store][0]}?excludeProductList=false&promoTab=false&page={page}&start={start}&showFacet=false&multiCategory=true"
                png_headers={
    "Host": " www.blibli.com",
    "User-Agent": " Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv125.0) Gecko/20100101 Firefox/125.0",
    "Accept": " application/json, text/plain, */*",
    "Accept-Language": " en-US,en;q=0.5",
    "Accept-Encoding": " gzip, deflate, br",
    "Referer": f"https://www.blibli.com/merchant/{store}/{list_store[store][1]}?pickupPointCode=PP-3035142&excludeProductList=false&promoTab=false&page={page}&start={start}",
    "Cache-Control": " no-cache",
    "channelId": " web",
    "params": " [object Object]",
    "Sec-Fetch-Dest": " empty",
    "Sec-Fetch-Mode": " cors",
    "Sec-Fetch-Site": " same-origin",
    "Connection": " keep-alive",
    "Cookie": " _abck=F5F72D0D61C5A63889CFBEC01D492A49~0~YAAQljLdF1Mb80ePAQAAe3wgYAuw5nbyWNVMQSJwedvs4CYn45tigk0oWrXpN+1v3acFgYBdJFqoD4LdhuSN9w6hXigaT76+dItI0mKOKa/Eb+IeTlWpksi1P247gLeAZ+DoIZW0ZMpNQ2T5Rwfxk5C8zknEx/CEjBrlqam8eqy9GByRrUd1M9NW0VN66Tvl+G+MxhRGnFD2TsmGPW3IqWiPHAw1J9klz1H8sgwB2mLKqlqRnZNM23vxekAh97TfFtG6Vozf098eIAbK869aTmEIUcTohQxsyBfjw55niXiTPWt9GKwDfLaIdQ+WEe58XpxHPW1PKOOaYkETxUB1cr5JFLjrGn6gthqlKAEszBedZeRDliu+60M5hwSrrKAhEXGcVNHVN4JqsOIgLB7KlxCndu07Wdx0vbr/3FCOY4EqC047bA==~-1~-1~-1; Blibli-Device-Id=U.d2f207e1-ab7a-4650-85cd-753c99c0efd8; Blibli-Device-Id-Signature=2e07b5b5649ccef016ef51e1abd85d31ea1709cc; _gcl_au=1.1.641217210.1713852952; __bwa_user_id=657116261.U.5278806020167375.1713852953; __bwa_user_session_sequence=24; _ga=GA1.2.102805860.1713852953; _ga_G3ZP2F3MW9=GS1.1.1715308011.25.1.1715308257.49.0.0; _cs_ex=1; _cs_c=0; _cc_id=23041d1c78731719b8dfa94b423c6c92; IR_PI=f068c89e-0138-11ef-8722-15fcf2d6df23%7C1713852952901; _vwo_uuid_v2=D15C8F1396C013E62B7F77A9B960A0CFD|e36049cbb8bc426439893e158db2c22a; _fbp=fb.1.1713852956365.2032131872; _vwo_ssm=1; _vis_opt_s=16%7C; _vwo_uuid=D0F7B4C05F4407AD29D7ED634A2A0654B; _vwo_ds=3%3At_0%2Ca_0%3A0%241713852956%3A23.24824455%3A%3A11_0%2C7_0%2C6_0%2C5_0%2C4_0%2C3_0%2C2_0%3A252_0%2C251_0%2C250_0%2C210_0%2C209_0%2C208_0%2C3_0%2C2_0%3A1; _vis_opt_exp_357_exclude=1; _ce.s=v~41ef8e12f336575c643ba5366b2e244fa86cdde5~lcw~1715314695954~lva~1715308014424~vpv~13~v11.fhb~1715308015813~v11.lhb~1715314696958~v11.cs~295312~v11.s~c52360c0-0e74-11ef-928b-e10a2eb48a1e~v11.sla~1715308257188~gtrk.la~lw028lyz~v11.send~1715308256944~lcw~1715314696958; afUserId=4a87a41f-913b-4529-b97d-2a362f691a9e-p; _vis_opt_exp_287_exclude=1; _ga_G3ZP2F3MW9=deleted; __utma=205442883.102805860.1713852953.1714635678.1714635678.1; __utmz=205442883.1714635678.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _ga_7MFS22ZGBJ=GS1.2.1714635680.1.0.1714635680.60.0.0; panoramaId_expiry=1715913055973; panoramaId=4591fd4e161d3d4b9fb8fbd5ef784945a7023d552cef8670e89a3a96acea3553; panoramaIdType=panoIndiv; Blibli-User-Id=004ea6ec-82b8-4b7a-9175-523b5dcc0703; Blibli-Is-Member=false; Blibli-Is-Remember=false; Blibli-Session-Id=88ab273e-7b7d-41fc-ac96-c5187bccd158; Blibli-Signature=1b70902fbd98edc20f7e649a6655fa4be831702e; AF_SYNC=1715073542869; bm_sz=23AE1FB71108E7C52D86102F782815AC~YAAQljLdFzyL/UePAQAAIe/DYBescRtBkWGaP+abJDLtlZpjsHsmr2LxVZl2LX0rDAMFzcxixgYc1yZuYOGHvYGyGlCFe4nroozeXnWSjJN+HPMFFAqli/3AWYPqwX5GKAzjjTvX3WeJHwOch2eaee3iN4htOUBK6iR7mhFQCPWjUqU70cVW3wr0sXKYJYW+K6Z7r3lL81C22+FsroRGRxiV/uOe9WHDQJBMek+NqHggN6m25OxQ1nwsrKv4vthGFp7sPnw7RHcJWEJ1OqIWkfhVNjWnGAe+eM7pei3LjKFJWV5p9gDs1y48sCp6e/jCCB0SSxgymA+aejPtgrMWmzc2XWLSNcM4XM1mpE09wEtuMs2CGBP/j3eBrxZTcMKB+x8ZfudT8RrpLV1/bpqqwgZ3Wp7ulhQ2cttqHzOMmy/OVEnpJwVlVbtWUSxX+8GQqA==~3425584~3159346; _gid=GA1.2.751156081.1715304695; Blibli-dv-id=JD_-G3q_cN-bO4AbmQEJxC9K6DCpc8BR6XWYzfW_bc40zV; Blibli-dv-token=JT_4GcfFunPgru2ON_fPqnwnkXPOViQZTfwAB6u7j4iAHz; Blibli-dv-id-version=2; _ce.clock_event=1; _ce.clock_data=-508%2C103.190.223.194%2C1%2C89fcffeff64f7d9db258b092f5302a60; ak_bmsc=EC6970E9BE4B33B37DCC6C8691EC2B90~000000000000000000000000000000~YAAQljLdF8aL/UePAQAAY/PDYBdQtv0aKp3Gi8UXjZ7V2i4gFV4E4hlI4vjlzz+a9AtyungHJ40c8pk4bM2ZCz9ZDTZBryCALLDbOZXmbR+SBMAHDKg3j2SfOKGTdDXnXvLiZB5NiRGWe4XMPSzPDTSI782PMeB4ZEfQ/xFnk+NJ8eLjMrKtQm4rXq4jEu8hbePfQrQzrstpI/wVv5HEROTAPxNnaZsblUtFC1CxHcCFYURKO7ZrdSnxGqTWkdzlrnUg7WQvwGb1tNnRcyI6tho/ETRGu8lKgw8fC6G1/+rh/m6WZ5jwEk1skH2Od1EHTurhBm6aIY0WOHs+pZ8Goo4UXmA+XzrovFpoo8Hw+9A0xX4WsOROMfQN0J5/lhYDmoUHG21NiBbymrRJqTztU4fa+n25RMrT+5XK2iw9/iSHUlc0khQAM/a5eYPrhlK8L77qB/jxjEM4tmInrw==; bm_sv=D70AD86EC027669C1E0A7B583799EE12~YAAQljLdFyiN/UePAQAAOf/DYBfOLMk8OvbFqYg0J8eix35T1P6J0nccA/hbR2DtORmeVRFWiMUZhOq5VtqPdXRTBK+9hSmYxvrOtennUzfsLTd+FjZaIEWoKZ61P+laF3FC1gJqsFNjJ8p0tVyUsONHInA59g7rzBNVGNVQg9bWIfPtdQzqAMJo1cXhEPEZxwiHwIMy6os7xnXPoq6zK8DQt6Zhmb8xgxptGwxRhaix0jwwtNzzVhMLGvQYUu+4~1; __bwa_session_action_sequence=1; __bwa_session_id=657116261.S.5813006803583028.1715315406; IR_gbd=blibli.com; IR_19024=1715315406541%7C4120732%7C1715315406541%7C%7C; _vis_opt_test_cookie=1; _vwo_sn=1462450%3A1",
    "TE": " trailers"
                }
                yield scrapy.Request(png,callback=self.parse,headers=png_headers)
                start+=40
    def parse(self, response):
        data=json.loads(response.body)
        for i in range(0,len(data['data']['products'])):
            item=BlibliItem()
            item["name"]=data['data']['products'][i]['name']
            item['sku']=data['data']['products'][i]['images'][0].split('/')[-2]
            item["url"]=data['data']['products'][i]['url']  
            item["stock"]=data['data']['products'][i]['status']
            item["rating"]=data['data']['products'][i]['review']['absoluteRating']
            item["review"]=data['data']['products'][i]['review']['count']
            item["price"]=data['data']['products'][i]['price']['priceDisplay']
            try:
                item['original_price']=data['data']['products'][i]['price']['strikeThroughPriceDisplay']
            except:
                item['original_price']="0"
            item['shop_name']=data['data']['products'][i]['merchantName']
            item['category']=data['data']['products'][i]['rootCategory']['name']
            yield item
settings=get_project_settings()
process=CrawlerProcess(settings)
process.crawl(BliblibotSpider)
process.start()