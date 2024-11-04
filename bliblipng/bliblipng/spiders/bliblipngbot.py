from typing import Iterable
import scrapy
import json
from sys import path
from scrapy.crawler import Crawler
from scrapy.crawler import CrawlerProcess
import datetime
from scrapy.utils.project import get_project_settings
path.append('/home/dikapc/project/scrapy_old_v2/scrapy_ecom/bliblipng')
from bliblipng.items import BlibliItem 
class BliblibotSpider(scrapy.Spider):
    name = "bliblipngbot"
    download_delay=0.5
    allowed_domains = ["www.blibli.com"]
    def start_requests(self):
        import pandas as pd
        # sheet_id='1keKW8fbYaX9CNI3oct1ON4mIz0wQEuxG0wedHUK1skw'
        # sheet_name='update_osa'
        # url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
        # df= pd.read_csv(url)
        # sku_id=df[df['eCustomer']=='Blibli Jabodetabek']['Full SKU ID'].to_list()
        yield scrapy.Request(f"https://www.blibli.com/backend/product-detail/products/is--PGG-18081-01026-00001/_summary",headers=
                                 {"host":"www.blibli.com",
"user-agent":"mozilla/5.0 (windows nt 10.0; win64; x64; rv:126.0) gecko/20100101 firefox/126.0",
"accept":"application/json, text/plain, /",
"accept-language":"en-us,en;q=0.5",
"accept-encoding":"gzip, deflate, br, zstd",
"referer":"https://www.blibli.com/p/gillette-isi-ulang-vector-pisau-cukur-2-pcs/ps--PGG-18081-01026?pickupPointCode=PP-3523981",
"cache-control":"no-cache",
"sec-fetch-dest":"empty",
"sec-fetch-mode":"cors",
"sec-fetch-site":"same-origin",
"connection":"keep-alive",
"cookie":"abck=f5f72d0d61c5a63889cfbec01d492a49~0~yaaqvz42fzwlir+paqaai8rk5gzvt2c9bb1fi3+ympm8qm0cgb25kku5eudowgsp67zvdymjdrvmtl10wrfwsrjcooao2udajwygis+wjjwgu6fal+bycnan727p2g4vi5l590ojcfkwrjse3btwpcu0qgnzwqmpt/r7/b8msndhnpkbgfjfmmt4tghg8jp/21p8lzzrkt5e5dsxyemdrttfpyad1txybdc1pf2mrjvq5nvcycjvkc8qggrrtywwcc+m7dpf6a8hg4hcolovpdpg9d1ypo6/kgswey/rv4akvhadles6xce3g7wubog8brpqxjmxw9tcc013pqcjxqv65zelisncxlbt2ivu6ddw322ke9fndys2z0w5ti7/lb8xfcywe2+xbrpzyuke0vrzhyqfplc46ubeobibuunzgh9crw==-1-1~-1; blibli-device-id=u.d2f207e1-ab7a-4650-85cd-753c99c0efd8; blibli-device-id-signature=2e07b5b5649ccef016ef51e1abd85d31ea1709cc; _gcl_au=1.1.641217210.1713852952; __bwa_user_id=657116261.u.5278806020167375.1713852953; __bwa_user_session_sequence=65; _ga=ga1.2.102805860.1713852953; _ga_g3zp2f3mw9=gs1.1.1717573350.21.1.1717573876.60.0.0; _cs_ex=1; _cs_c=0; _cc_id=23041d1c78731719b8dfa94b423c6c92; ir_pi=f068c89e-0138-11ef-8722-15fcf2d6df23%7c1713852952901; _vwo_uuid_v2=d15c8f1396c013e62b7f77a9b960a0cfd|e36049cbb8bc426439893e158db2c22a; _fbp=fb.1.1713852956365.2032131872; _vwo_ssm=1; _vis_opt_s=37%7c; _vwo_uuid=d0f7b4c05f4407ad29d7ed634a2a0654b; _vwo_ds=3%3at_0%2ca_0%3a0%241713852956%3a23.24824455%3a%3a11_0%2c7_0%2c6_0%2c5_0%2c4_0%2c3_0%2c2_0%3a252_0%2c251_0%2c250_0%2c210_0%2c209_0%2c208_0%2c3_0%2c2_0%3a1; _vis_opt_exp_357_exclude=1; _ce.s=v~41ef8e12f336575c643ba5366b2e244fa86cdde5~lcw~1717573874931~lva~1717555617512~vpv~34~v11.fhb~1717573410154~v11.lhb~1717573847831~v11.cs~295312~v11.s~4d648690-230f-11ef-a2c5-b138095a6266~v11.sla~1717573875292~gtrk.la~lx1j4vz6~v11.send~1717573874931~lcw~1717573875292; afuserid=4a87a41f-913b-4529-b97d-2a362f691a9e-p; _vis_opt_exp_287_exclude=1; _ga_g3zp2f3mw9=deleted; __utma=205442883.102805860.1713852953.1714635678.1714635678.1; __utmz=205442883.1714635678.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _ga_7mfs22zgbj=gs1.2.1714635680.1.0.1714635680.60.0.0; _vis_opt_exp_409_exclude=1; panoramaid_expiry=1718178591118; panoramaid=4591fd4e161d3d4b9fb8fbd5ef784945a7023d552cef8670e89a3a96acea3553; panoramaidtype=panoindiv; blibli-user-id=03b9e35e-a876-46d3-83f8-07b4ead3612f; blibli-is-member=false; blibli-is-remember=false; blibli-session-id=07338a69-910a-4b35-bda8-d41df391c1a0; blibli-signature=1c90b33b54c5a5a8758722f378183786fd7e3a3f; _vis_opt_exp_411_exclude=1; _vis_opt_exp_412_exclude=1; _gid=ga1.2.1904024954.1717386997; _vis_opt_exp_413_exclude=1; _vis_opt_test_cookie=1; ir_gbd=blibli.com; ir_19024=1717573876572%7c4120732%7c1717573876572%7c%7c; moe_uuid=75da6a7d-54a9-4abe-824a-f55fd069d062; _ce.irv=returning; cebs=1; cebsp=19; _cf_bm=jfs2bddhlzq5qjfdwigwmk5pnmoxpuu2l.tcjxsbdnu-1717573340-1.0.1.1-f7moqvu..id_ztrkpdm6cbvlsw0wtmxqox9kdchjo5ajmmnbcv_r3eydlpuxlmtg10zftoly1wfdtltm0tgv.q; _cfuvid=rhuxbmopzgfx1k.roqibslq77yuw_2uy_0kozlcktha-1717573340704-0.0.1.1-604800000; _cs_mk_ga=0.9244187107574622_1717573347803; __bwa_session_action_sequence=40; __bwa_session_id=723337755.s.9816699863417812.1717573350; _vwo_sn=3720392%3a78; blibli-dv-id=jd-g3q_cn-bo4abmqejxc9k6dcpc8br6xwyzfw_bc40zv; blibli-dv-token=jt_zr4oq4numgud7fhry8amylrqiqqfu6ywh-ni7jrsxkj; blibli-dv-id-version=2; _ce.clock_event=1; _ce.clock_data=160%2c103.190.223.194%2c1%2c5e8407a4b97acbbfb041aeeddfe3844c%2cfirefox%2cid; af_sync=1717573412608; cf_clearance=oumevu3u2cx6d8y4vynav_h.a6imcw6rg2cjtijhnvs-1717573528-1.0.1.1-qsz2qbdlozctesydp525sxiwabwkc6t0pprkxlb6czmn08l0mieedn5osmvd6hr9naqfkmqujhycvjq6bt0hpq; _dc_gtm_ua-21718848-13=1",
"te":"trailers"},callback=self.parse,meta={'sku':'PGG-18081-01026-00001'})
    def parse(self, response):
        data=json.loads(response.body)
        item=BlibliItem()
        item["name"]=data['data']['name']
        item['item_code']=data['data']['productSku']
        item['product_code']=data['data']['productCode']
        item['sku']=response.meta.get('sku')
        item['stock']=data['data']['stock']
        item['rating']=data['data']['review']['decimalRating']
        item['review']=data['data']['review']['count']
        item['sold']=data['data']['statistics']['sold']
        item['url']=data['data']['url']
        item['shop_name']=data['data']['merchant']['name']
        try:
            item['original_price']=data['data']['price']['listed']
        except:
            item['original_price']=0
        item['price']=data['data']['price']['offered']
        yield item
# settings=get_project_settings()
# process=CrawlerProcess(settings)
# process.crawl(BliblibotSpider)
# process.start()