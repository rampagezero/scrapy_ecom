from typing import Iterable
import scrapy
import json
from scrapy.crawler import Crawler
from scrapy.crawler import CrawlerProcess
import datetime
from scrapy.utils.project import get_project_settings
from sys import path
path.append('/home/dikapc/project/scrapy/lazada_scrapy/lazada_osa')
from lazada_osa.items import LazadaOsaItem
class LazadaSpider(scrapy.Spider):
    name = "lazada"
    allowed_domains = [f"https://www.lazada.co.id/"]
    download_delay=0.25
    def __init__(self):
        # if datetime.datetime.today().time()>datetime.time(hour=11,minute=58) and datetime.datetime.today().time()<datetime.time(hour=14,minute=58) :
        #     self.url={"philips-lighting-store":9,"quaker":3,"tefal":6}
        # else:
        # self.url={"nabati-snack":6}
        self.url={"pg-official-store":20,"olay":5,"philips-lighting-store":9,'fumakilla':3,"quaker":3,"totalenergies":3,"delfi-official-store":10,'tefal':6,'imeal-official-store':4,'skrineer':4,'nivea':8,'hansaplast1629968595':5}
        # ,'fumakilla':3,"quacker":3,"totalenergies":3,"delfi-official-store":9,"pg-official-store":20,"olay":5
        # self.url={"tefal":6}
    def start_requests(self):
        for url in self.url:
            for page in range(1,self.url[url]):
                yield scrapy.Request(url=f"https://www.lazada.co.id/{url}/?ajax=true&from=wangpu&isFirstRequest=true&langFlag=id&page={page}&pageTypeId=2&q=All-Products",method='GET',headers={
                    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0",
                    "path":f"/{url}/?ajax=true&from=wangpu&isFirstRequest=true&langFlag=id&page={page}&pageTypeId=2&q=All-Products",
                    "accept":"application/json, text/plain, */*",
                    "accept-language":"en-US,en;q=0.5",
                    "accept-encoding":"gzip, deflate, br",
                    "referer":"https://www.lazada.co.id/",
                    "X-CSRF-TOKEN":"ef5be8b1b13eb",
                    "alt-Used":"www.lazada.co.id",
                    "connection":"keep-alive",
                    "cookie":" __wpkreporterwid_=426d1d5e-2ca4-495d-0e0b-7c4772cbeb8c; lwrid=AQGL%2F3AB4wn50MCJj9rlvA129ISZ; isg=BFJSCt7bYMulxp9xULddHMO1oBg0Y1b9U--w-hyrfoXwL_IpBPOmDVhMnxMTRM6V; epssw=1*MgOs11iCtCQFtEz4IASGt9tItdVSNqzaIAb9QeHOsAfwulGdKQCTFGxM6TsczQ9AjhvBuB_CZxBLCjW-6T9C3C65NOH931Lu0WJBbc6kKHxloyopqTJSX1-d9ZOWegQPvIP4YD4RyMD7xkmnxv9-dLEUxTB4pLHgvq-B_Zj3k9CXYUwjBMmnpLnnxDm3xf..; lzd_cid=0a99e3d7-f725-4db3-b8d3-61fa7bc4b17c; t_uid=0a99e3d7-f725-4db3-b8d3-61fa7bc4b17c; t_fv=1700797621321; _bl_uid=XqlpLp4bc8p25tzX1n4FmLXsqIhL; cna=tQrnHUQHgmkCAWe+38J11JN9; tfstk=f1yjI3DuQEYf6CUBRjIrFwkbdHkNYP6EHhiTxlp2XxHvWFEKzASD_smsC4aiufFVSzgToz0ZkAy4FPaQ8oy4gsj_FlEKucS0C7v_xl2VmASDnoDiBw7FLwr0mA4rP9rlzuItjtlCuyXUmox-Bw7FL9R6Nbl15VU9M43-rcvtBKnOV4nsxCpYWAI724mMHmdxMTK-fcO9z98SbsiTcNJKJFpJbsqmPdp_rmG-J90WBdeSceuLD6p9B8ijiRsXwBAZg5Ent-r5CLD4A7H-fRjp1VGQ6-k8HaBKZfF_W0Vl5CgQ6oPn2JIwt4ySuPejwMJI_YeE9xFPZZlZhcHxt7jMgVFTAJM4uavtuWZ8PXyyzpkLtzws9vIzbpuQyXA6VXvtVIj5VCAwIMvHVlXuWplxqmBFVgTWsev9QB2NVCpZM0mYngsWP35..; __itrace_wid=e6d36f99-b242-46b0-afd1-d3af4363eac0; _ga=GA1.3.918513016.1701231822; _ga_44FMGEPY40=GS1.3.1713773789.79.1.1713773789.60.0.0; _fbp=fb.2.1701231823263.202456374; AMCV_126E248D54200F960A4C98C6%40AdobeOrg=-1124106680%7CMCIDTS%7C19836%7CMCMID%7C33818851704425127832786202363156150771%7CMCAAMLH-1714378590%7C3%7CMCAAMB-1714378590%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1713780990s%7CNONE%7CMCSYNCSOP%7C411-19843%7CvVersion%7C5.2.0; _gcl_au=1.1.1019125016.1709108758; hng=ID|id-ID|IDR|360; userLanguageML=id; hng.sig=to18pG508Hzz7EPB_okhuQu8kDUP3TDmLlnu4IbIOY8; _m_h5_tk=b4b4854cb2142b168f4d3cba5b4d4e34_1713774951062; _m_h5_tk_enc=486d95bcd42c86814ef003b2f1256af6; xlly_s=1; _gid=GA1.3.459705263.1713759869; EGG_SESS=S_Gs1wHo9OvRHCMp98md7OFnZD_49Y70n9VMmn2sPCWSXiq9I2wsD71iqE-nZijojPb5PM-NkmP_7W_J5q4_UaE5NiZxFUpan-8KmakZpAwC05dIs00HX5BNLBdsR8gTPUKYBMYgKLLQo7BTmDgnBm7jINX56lMzuL0M-Bl2nrQ=; x5sec=7b22617365727665722d6c617a6164613b33223a22307c434e474e6d4c4547454b7a653370442f2f2f2f2f2f7745776f632f683067553d222c22733b32223a2231356563343133656235363163623661227d; t_sid=A67Jo01yqeMshw1kRVrTp0IDGSsh5o81; utm_channel=NA; lzd_sid=11c49ccdf67df74f3bf9caf3f59ff290; _tb_token_=ef5be8b1b13eb; _gat_UA-29801013-1=1; AMCVS_126E248D54200F960A4C98C6%40AdobeOrg=1",
                    "Sec-Fetch-Dest":"empty",
                    "Sec-Fetch-Mode":"cors",
                    "Sec-Fetch-Site":"same-origin"
                },cookies={
        "__itrace_wid":	"e6d36f99-b242-46b0-afd1-d3af4363eac0",
        "__wpkreporterwid_":	"426d1d5e-2ca4-495d-0e0b-7c4772cbeb8c",
        "_bl_uid":	"XqlpLp4bc8p25tzX1n4FmLXsqIhL",
        "_fbp":	"fb.2.1701231823263.202456374",
        "_ga":	"GA1.3.918513016.1701231822",
        "_ga_44FMGEPY40":	"GS1.3.1713773789.79.1.1713775576.60.0.0",
        "_gcl_au":	"1.1.1019125016.1709108758",
        "_gid":	"GA1.3.459705263.1713759869",
        
        "_m_h5_tk":	"7de247a2f0398de2627a0f2c4d6e6647_1713783453402",
        "_m_h5_tk_enc":	"5e990f5ae42711d6bc65fd2910d57672",
        "_tb_token_":
            "ef5be8b1b13eb",
        "_uetsid":	"647c3f90005a11efa2ae8f2b306bfaf8",
        "_uetvid":	"cb30da00985111eeb49ebfc2d18c8a5b",
        "AMCV_126E248D54200F960A4C98C6@AdobeOrg":	"-1124106680|MCIDTS|19836|MCMID|33818851704425127832786202363156150771|MCAAMLH-1714378590|3|MCAAMB-1714378590|6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y|MCOPTOUT-1713780990s|NONE|MCSYNCSOP|411-19843|vVersion|5.2.0",
        "AMCVS_126E248D54200F960A4C98C6@AdobeOrg":	"1",
        "cna":	"tQrnHUQHgmkCAWe+38J11JN9",
        "EGG_SESS":	"S_Gs1wHo9OvRHCMp98md7OFnZD_49Y70n9VMmn2sPCWSXiq9I2wsD71iqE-nZijojPb5PM-NkmP_7W_J5q4_UaE5NiZxFUpan-8KmakZpAwC05dIs00HX5BNLBdsR8gTPUKYBMYgKLLQo7BTmDgnBm7jINX56lMzuL0M-Bl2nrQ=",
        "epssw"	:"1*GdA611ir613ctEz4IA7SZ-FFh2z4urza7yFmF2UpBOgV7lGIvQFSH1B5NKCKbJ926BhOF96VVL1DGv1g9R6wF_6A6TCWHIHvNtdszd9vV-QG2NQk8ueVR_5IPaCCO2VWysPjviy4FtuRyTINxkDR3kmndLedjTB4Ftz9ARj4y7bJ48OlYUwjBMmnpL3RyTB4dC..",
        "hng":	"ID|id-ID|IDR|360",
        "hng.sig":	"to18pG508Hzz7EPB_okhuQu8kDUP3TDmLlnu4IbIOY8",
        "isg":	"BJGR37msk4Y7avzU_3oOYQTgo50r_gVwdPpTX3Mm3dh3GrBsu0oSQR95vHb8CZ2o",
        "lwrid":	"AQGL/3AB4wn50MCJj9rlvA129ISZ",
        "lzd_cid":	"0a99e3d7-f725-4db3-b8d3-61fa7bc4b17c",
        "lzd_sid":	"11c49ccdf67df74f3bf9caf3f59ff290",
        "t_fv":	"1700797621321",
        "t_sid":	"A67Jo01yqeMshw1kRVrTp0IDGSsh5o81",
        "t_uid":	"0a99e3d7-f725-4db3-b8d3-61fa7bc4b17c",
        "tfstk":	"feCxnejzbuqmp2BGEZwlbEuuYVUHB1QVPi7IshxmCgIRRwoDCG24CCIFXd1DiNN9W3_NjnAMGNi9qgWGItq46CIy2jcMidcO2I5lnfx00CQ1xBE3xWVhuZRe1kqnaeibII89fj9jjLgWuXzjouPhuZuW1kq3tWDteH5bWhsshYOW4F3X5nssF4ty7FiX5naRP3861Ft61QNWReGscfTovrKrlEhOZshQrUVwOfG1GKJvXnDi6fCJkKHVl3QAk_LvHHv-VFKhGgb1isJzCAdNr9IOCMZonn6pJgphHkhAvi81VUs0SA8RBN1egiEx3n6c2p8WFVFerMx5us6870_fxndRd14i6H6C5s9AUWoXjTbd6FCab7Id5wW6e1nA4SCh9hXSxHLiHzCsQAJXrDqlT8ttUJlDyH4XhAkwIUliH14ZCAiEZUK3lvHZQdxG.",
        "userLanguageML":	"id",
        "utm_channel":	"NA",
        "xlly_s":	"1"
                },callback=self.parse)
    def parse(self, response):
        data=json.loads(response.body)
        print(len(data['mods']['listItems']))
        for i in range(0,len(data['mods']['listItems'])):
            item=LazadaOsaItem()
            item["name"]=data['mods']['listItems'][i]['name']
            item["url"]=data['mods']['listItems'][i]['itemUrl']
            item['link_id']=data['mods']['listItems'][i]['itemUrl']
            item['sku']=data['mods']['listItems'][i]['sku']
            item['count_sold']=data['mods']['listItems'][i]['querystring']
            item["stock"]=data['mods']['listItems'][i]['inStock']
            item["rating"]=data['mods']['listItems'][i]['ratingScore']
            item["review"]=data['mods']['listItems'][i]['review']
            item["price"]=data['mods']['listItems'][i]['priceShow']
            item['shop_name']=data['mods']['listItems'][i]['sellerName']
            item['category']=data['mods']['listItems'][i]['querystring']
            item['original_price']=data['mods']['listItems'][i]['originalPriceShow']
            yield item
settings=get_project_settings()
process=CrawlerProcess(settings)
process.crawl(LazadaSpider)
process.start()

