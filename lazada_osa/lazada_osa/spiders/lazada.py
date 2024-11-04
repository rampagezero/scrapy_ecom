from typing import Iterable
import scrapy
import json
from scrapy.crawler import Crawler
from scrapy.crawler import CrawlerProcess
import datetime
from scrapy.utils.project import get_project_settings
from sys import path
path.append('/home/dikapc/project/scrapy_old_v2/scrapy_ecom/lazada_osa')
from lazada_osa.items import LazadaOsaItem
class LazadaSpider(scrapy.Spider):
    name = "lazada"
    allowed_domains = [f"https://www.lazada.co.id/"]
    download_delay=10
    def __init__(self):
        # if datetime.datetime.today().time()>datetime.time(hour=11,minute=58) and datetime.datetime.today().time()<datetime.time(hour=14,minute=58) :
        #     self.url={"philips-lighting-store":9,"quaker":3,"tefal":6}
        # else:
        # self.url={"nabati-snack":6}
        self.url={"pg-official-store":16,"olay":3,"philips-lighting-store":9,'fumakilla':4,"quaker":3,"totalenergies":2,"delfi-official-store":8,'tefal':4,'imeal-official-store':4,'skrineer':3,'nivea':6,'hansaplast1629968595':5}
        # ,'fumakilla':3,"quacker":3,"totalenergies":3,"delfi-official-store":9,"pg-official-store":20,"olay":5
        # self.url={"tefal":6}
    def start_requests(self):
        cookies_2= {
        "_wpkreporterwid": "49714c4a-d522-4a26-22b8-8da418026343",
        "_bl_uid": "bXm1F2CIbjpkFU27pg3nzRUtXwIX",
        "_fbp": "fb.2.1729064013174.509957913488493088",
        "_ga": "GA1.3.840652735.1729064012",
        "_ga_44FMGEPY40": "GS1.3.1729064012.1.1.1729065770.60.0.0",
        "_gcl_au": "1.1.1985701982.1729064011",
        "_m_h5_tk": "96d192d912ef8fb3aad6414f8385c9b5_1730695425122",
        "_m_h5_tk_enc": "32b32b09efd4c5eff3293875f0453508",
        "tb_token": "f45ee35a844a0",
        "AMCV_126E248D54200F960A4C98C6@AdobeOrg": "-1124106680|MCIDTS|20013|MCMID|45830569797874570182769665348184729479|MCAAMLH-1729668813|3|MCAAMB-1729668813|6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y|MCOPTOUT-1729071213s|NONE|MCSYNCSOP|411-20020|vVersion|5.2.0",
        "cna": "zVmWH2o34xICAWe+38L796Uf",
        "EGG_SESS": "S_Gs1wHo9OvRHCMp98md7P9EtbE2pMTHAJbU0wngNEqmSvQ0wmWSjVnCwXD9_Hc2jpE_4A_KuAcK1UsVYLEftMD2szWjqCtl6XxySXpmvODQEvG78XgpOjiosjt6Ud4kHOf0P6zPnNcnJd13E33CNoUzeZ-PT5M_kN1m5Qrmokg=",
        "epssw": "7*FH5ss6UaWa8hYuDjT21sus36MJo8zrhMvwegD8SshtT4csm5bPUR9A60QRl9sG8WT21jNw8vsssssIDL3dDug6dKdumoTDf67BAziyFj7j1LNNYFEMVBz4BvzhF3p7x-_vuoPz-KZHSpCUT9ePwGAQLgRyRkZb7aswERI3ntXxjsWjqO-OQyQPOOldEsCDxO7VGPT-fOU1DKu6KJBPQv-apMhrAbO3a1bAKJ_BCiDoZPQLaC_sZqAqEesaRbOhNbgpDQNX-weF0FU-rbssIb0s6hGZs66E..",
        "hng": "ID|id-ID|IDR|360",
        "hng.sig": "to18pG508Hzz7EPB_okhuQu8kDUP3TDmLlnu4IbIOY8",
        "isg": "BKOjkb_DwKJTHYyxrv2xTdKvMedNmDfa7g2PHdUAGoIlFMA2XWstK8tHCnwar4_S",
        "lwrid": "AgGSlD0VoB1tw14NjdVvvA129Py5",
        "lwrtk": "AAEEZyiWp1EypluBVAJQC/6xhSvix8VcwrvFVM3Fdhdh1pI/Q1snFgU=",
        "lzd_cid": "69d2f803-ffab-4875-ac71-fa4da327e50f",
        "lzd_sid": "112cf3225c3fd60da5b0df97a1102f35",
        "t_fv": "1729063884173",
        "t_sid": "kZXiZE2MMCOKJNarGRLOqZkYyxRddX97",
        "t_uid": "5cf1gL1KyD3lBmElgK8fjh00g3N293VM",
        "tfstk": "fD-E6Z2H8DnEPIyvt6SP3PGj08Qd4Mcfx315ELvld6f3AkNk7CdzFvh-JF5ys19BVMj7ahRMGU9I9esrU198V6_SpCypbIr7AX3pEuSfqjGjcm9LpgIoGN7YbU1dedfoJ-usWpIRqfGjcm9ppIfhEzCFqAoGhtIutkAlScfOeTVhEkDwI3EJMPDzawwWF1YSMHuEzlvN_uqy697GimCaquxNLS1DK4EuqhWFJ3pvcGShRUvAkH_r4lIB3FjGLQmmtNLHQ37v24GpBM5eHN8tTlX6QLYf7hMmDMShtUspF-lBQHRBphJ7EyRylBLAz3cU01xd4uNRIHXe2ePurwq5QsMZQL27s1fiwy7UyzQdBO5jK5aurSEYVy-SdzURRPBNGv41.",
        "userLanguageML": "id",
        "utm_channel": "NA",
        "x5sec": "7b22617365727665722d6c617a6164613b33223a22617c434a2f566f4c6b47454e76722b49594249676c795a574e686348526a614745776f39795979514e4b556a41304d446c6d5a6a41774d4441774d4441774d4451774d4441774d4441774d4441774d4441774d4441774d4441774d4441774d4441774d4441774d4441774e445933596d566b5a6d4d794f5759794d5759304d544e6c4e57557a4e7a55794e7a41774d4441774d4441774d44453d222c22733b32223a2232346265623163373437343963363464227d",
        "xlly_s": "1"
    }
            # headers_ 1={
            #         "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0",
            #         "path":f"/{url}/?ajax=true&from=wangpu&isFirstRequest=true&langFlag=id&page={page}&pageTypeId=2&q=All-Products",
            #         "accept":"application/json, text/plain, */*",
            #         "accept-language":"en-US,en;q=0.5",
            #         "accept-encoding":"gzip, deflate, br",
            #         "referer":"https://www.lazada.co.id/",
            #         "X-CSRF-TOKEN":"ef5be8b1b13eb",
            #         "alt-Used":"www.lazada.co.id",
            #         "connection":"keep-alive",
            #         "cookie":" __wpkreporterwid_=426d1d5e-2ca4-495d-0e0b-7c4772cbeb8c; lwrid=AQGL%2F3AB4wn50MCJj9rlvA129ISZ; isg=BFJSCt7bYMulxp9xULddHMO1oBg0Y1b9U--w-hyrfoXwL_IpBPOmDVhMnxMTRM6V; epssw=1*MgOs11iCtCQFtEz4IASGt9tItdVSNqzaIAb9QeHOsAfwulGdKQCTFGxM6TsczQ9AjhvBuB_CZxBLCjW-6T9C3C65NOH931Lu0WJBbc6kKHxloyopqTJSX1-d9ZOWegQPvIP4YD4RyMD7xkmnxv9-dLEUxTB4pLHgvq-B_Zj3k9CXYUwjBMmnpLnnxDm3xf..; lzd_cid=0a99e3d7-f725-4db3-b8d3-61fa7bc4b17c; t_uid=0a99e3d7-f725-4db3-b8d3-61fa7bc4b17c; t_fv=1700797621321; _bl_uid=XqlpLp4bc8p25tzX1n4FmLXsqIhL; cna=tQrnHUQHgmkCAWe+38J11JN9; tfstk=f1yjI3DuQEYf6CUBRjIrFwkbdHkNYP6EHhiTxlp2XxHvWFEKzASD_smsC4aiufFVSzgToz0ZkAy4FPaQ8oy4gsj_FlEKucS0C7v_xl2VmASDnoDiBw7FLwr0mA4rP9rlzuItjtlCuyXUmox-Bw7FL9R6Nbl15VU9M43-rcvtBKnOV4nsxCpYWAI724mMHmdxMTK-fcO9z98SbsiTcNJKJFpJbsqmPdp_rmG-J90WBdeSceuLD6p9B8ijiRsXwBAZg5Ent-r5CLD4A7H-fRjp1VGQ6-k8HaBKZfF_W0Vl5CgQ6oPn2JIwt4ySuPejwMJI_YeE9xFPZZlZhcHxt7jMgVFTAJM4uavtuWZ8PXyyzpkLtzws9vIzbpuQyXA6VXvtVIj5VCAwIMvHVlXuWplxqmBFVgTWsev9QB2NVCpZM0mYngsWP35..; __itrace_wid=e6d36f99-b242-46b0-afd1-d3af4363eac0; _ga=GA1.3.918513016.1701231822; _ga_44FMGEPY40=GS1.3.1713773789.79.1.1713773789.60.0.0; _fbp=fb.2.1701231823263.202456374; AMCV_126E248D54200F960A4C98C6%40AdobeOrg=-1124106680%7CMCIDTS%7C19836%7CMCMID%7C33818851704425127832786202363156150771%7CMCAAMLH-1714378590%7C3%7CMCAAMB-1714378590%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1713780990s%7CNONE%7CMCSYNCSOP%7C411-19843%7CvVersion%7C5.2.0; _gcl_au=1.1.1019125016.1709108758; hng=ID|id-ID|IDR|360; userLanguageML=id; hng.sig=to18pG508Hzz7EPB_okhuQu8kDUP3TDmLlnu4IbIOY8; _m_h5_tk=b4b4854cb2142b168f4d3cba5b4d4e34_1713774951062; _m_h5_tk_enc=486d95bcd42c86814ef003b2f1256af6; xlly_s=1; _gid=GA1.3.459705263.1713759869; EGG_SESS=S_Gs1wHo9OvRHCMp98md7OFnZD_49Y70n9VMmn2sPCWSXiq9I2wsD71iqE-nZijojPb5PM-NkmP_7W_J5q4_UaE5NiZxFUpan-8KmakZpAwC05dIs00HX5BNLBdsR8gTPUKYBMYgKLLQo7BTmDgnBm7jINX56lMzuL0M-Bl2nrQ=; x5sec=7b22617365727665722d6c617a6164613b33223a22307c434e474e6d4c4547454b7a653370442f2f2f2f2f2f7745776f632f683067553d222c22733b32223a2231356563343133656235363163623661227d; t_sid=A67Jo01yqeMshw1kRVrTp0IDGSsh5o81; utm_channel=NA; lzd_sid=11c49ccdf67df74f3bf9caf3f59ff290; _tb_token_=ef5be8b1b13eb; _gat_UA-29801013-1=1; AMCVS_126E248D54200F960A4C98C6%40AdobeOrg=1",
            #         "Sec-Fetch-Dest":"empty",
            #         "Sec-Fetch-Mode":"cors",
            #         "Sec-Fetch-Site":"same-origin"
            #     }
        for url in self.url:
            cookies={
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
                        }
            # headers={
            #         "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0",
            #         "path":f"/{url}/?ajax=true&from=wangpu&isFirstRequest=true&langFlag=id&page={page}&pageTypeId=2&q=All-Products",
            #         "accept":"application/json, text/plain, */*",
            #         "accept-language":"en-US,en;q=0.5",
            #         "accept-encoding":"gzip, deflate, br",
            #         "referer":"https://www.lazada.co.id/",
            #         "X-CSRF-TOKEN":"ef5be8b1b13eb",
            #         "alt-Used":"www.lazada.co.id",
            #         "connection":"keep-alive",
            #         "cookie":" __wpkreporterwid_=426d1d5e-2ca4-495d-0e0b-7c4772cbeb8c; lwrid=AQGL%2F3AB4wn50MCJj9rlvA129ISZ; isg=BFJSCt7bYMulxp9xULddHMO1oBg0Y1b9U--w-hyrfoXwL_IpBPOmDVhMnxMTRM6V; epssw=1*MgOs11iCtCQFtEz4IASGt9tItdVSNqzaIAb9QeHOsAfwulGdKQCTFGxM6TsczQ9AjhvBuB_CZxBLCjW-6T9C3C65NOH931Lu0WJBbc6kKHxloyopqTJSX1-d9ZOWegQPvIP4YD4RyMD7xkmnxv9-dLEUxTB4pLHgvq-B_Zj3k9CXYUwjBMmnpLnnxDm3xf..; lzd_cid=0a99e3d7-f725-4db3-b8d3-61fa7bc4b17c; t_uid=0a99e3d7-f725-4db3-b8d3-61fa7bc4b17c; t_fv=1700797621321; _bl_uid=XqlpLp4bc8p25tzX1n4FmLXsqIhL; cna=tQrnHUQHgmkCAWe+38J11JN9; tfstk=f1yjI3DuQEYf6CUBRjIrFwkbdHkNYP6EHhiTxlp2XxHvWFEKzASD_smsC4aiufFVSzgToz0ZkAy4FPaQ8oy4gsj_FlEKucS0C7v_xl2VmASDnoDiBw7FLwr0mA4rP9rlzuItjtlCuyXUmox-Bw7FL9R6Nbl15VU9M43-rcvtBKnOV4nsxCpYWAI724mMHmdxMTK-fcO9z98SbsiTcNJKJFpJbsqmPdp_rmG-J90WBdeSceuLD6p9B8ijiRsXwBAZg5Ent-r5CLD4A7H-fRjp1VGQ6-k8HaBKZfF_W0Vl5CgQ6oPn2JIwt4ySuPejwMJI_YeE9xFPZZlZhcHxt7jMgVFTAJM4uavtuWZ8PXyyzpkLtzws9vIzbpuQyXA6VXvtVIj5VCAwIMvHVlXuWplxqmBFVgTWsev9QB2NVCpZM0mYngsWP35..; __itrace_wid=e6d36f99-b242-46b0-afd1-d3af4363eac0; _ga=GA1.3.918513016.1701231822; _ga_44FMGEPY40=GS1.3.1713773789.79.1.1713773789.60.0.0; _fbp=fb.2.1701231823263.202456374; AMCV_126E248D54200F960A4C98C6%40AdobeOrg=-1124106680%7CMCIDTS%7C19836%7CMCMID%7C33818851704425127832786202363156150771%7CMCAAMLH-1714378590%7C3%7CMCAAMB-1714378590%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1713780990s%7CNONE%7CMCSYNCSOP%7C411-19843%7CvVersion%7C5.2.0; _gcl_au=1.1.1019125016.1709108758; hng=ID|id-ID|IDR|360; userLanguageML=id; hng.sig=to18pG508Hzz7EPB_okhuQu8kDUP3TDmLlnu4IbIOY8; _m_h5_tk=b4b4854cb2142b168f4d3cba5b4d4e34_1713774951062; _m_h5_tk_enc=486d95bcd42c86814ef003b2f1256af6; xlly_s=1; _gid=GA1.3.459705263.1713759869; EGG_SESS=S_Gs1wHo9OvRHCMp98md7OFnZD_49Y70n9VMmn2sPCWSXiq9I2wsD71iqE-nZijojPb5PM-NkmP_7W_J5q4_UaE5NiZxFUpan-8KmakZpAwC05dIs00HX5BNLBdsR8gTPUKYBMYgKLLQo7BTmDgnBm7jINX56lMzuL0M-Bl2nrQ=; x5sec=7b22617365727665722d6c617a6164613b33223a22307c434e474e6d4c4547454b7a653370442f2f2f2f2f2f7745776f632f683067553d222c22733b32223a2231356563343133656235363163623661227d; t_sid=A67Jo01yqeMshw1kRVrTp0IDGSsh5o81; utm_channel=NA; lzd_sid=11c49ccdf67df74f3bf9caf3f59ff290; _tb_token_=ef5be8b1b13eb; _gat_UA-29801013-1=1; AMCVS_126E248D54200F960A4C98C6%40AdobeOrg=1",
            #         "Sec-Fetch-Dest":"empty",
            #         "Sec-Fetch-Mode":"cors",
            #         "Sec-Fetch-Site":"same-origin"
            #     }
            for page in range(1,self.url[url]):
                headers={
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
                }
                headers_1={
                    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0",
                    "path":f"/{url}/?ajax=true&from=wangpu&isFirstRequest=true&langFlag=id&page={page}&pageTypeId=2&q=All-Products",
                    "accept":"application/json, text/plain, */*",
                    "accept-language":"en-US,en;q=0.5",
                    "accept-encoding":"gzip, deflate, br",
                    "referer":"https://www.lazada.co.id/",
                    "X-CSRF-TOKEN":"f45ee35a844a0",
                    "alt-Used":"www.lazada.co.id",
                    "connection":"keep-alive",
                    "cookie":"_wpkreporterwid=49714c4a-d522-4a26-22b8-8da418026343; lzd_cid=69d2f803-ffab-4875-ac71-fa4da327e50f; hng=ID|id-ID|IDR|360; userLanguageML=id; t_fv=1729063884173; t_uid=5cf1gL1KyD3lBmElgK8fjh00g3N293VM; lwrid=AgGSlD0VoB1tw14NjdVvvA129Py5; epssw=7*FH5ss6UaWa8hYuDjT21sus36MJo8zrhMvwegD8SshtT4csm5bPUR9A60QRl9sG8WT21jNw8vsssssIDL3dDug6dKdumoTDf67BAziyFj7j1LNNYFEMVBz4BvzhF3p7x-vuoPz-KZHSpCUT9ePwGAQLgRyRkZb7aswERI3ntXxjsWjqO-OQyQPOOldEsCDxO7VGPT-fOU1DKu6KJBPQv-apMhrAbO3a1bAKJ_BCiDoZPQLaC_sZqAqEesaRbOhNbgpDQNX-weF0FU-rbssIb0s6hGZs66E..; cna=zVmWH2o34xICAWe+38L796Uf; isg=BKOjkb_DwKJTHYyxrv2xTdKvMedNmDfa7g2PHdUAGoIlFMA2XWstK8tHCnwar4_S; _m_h5_tk=96d192d912ef8fb3aad6414f8385c9b5_1730695425122; _m_h5_tk_enc=32b32b09efd4c5eff3293875f0453508; lwrtk=AAEEZyiWp1EypluBVAJQC/6xhSvix8VcwrvFVM3Fdhdh1pI/Q1snFgU=; _bl_uid=bXm1F2CIbjpkFU27pg3nzRUtXwIX; _gcl_au=1.1.1985701982.1729064011; _ga=GA1.3.840652735.1729064012; _ga_44FMGEPY40=GS1.3.1729064012.1.1.1729065770.60.0.0; AMCV_126E248D54200F960A4C98C6%40AdobeOrg=-1124106680%7CMCIDTS%7C20013%7CMCMID%7C45830569797874570182769665348184729479%7CMCAAMLH-1729668813%7C3%7CMCAAMB-1729668813%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1729071213s%7CNONE%7CMCSYNCSOP%7C411-20020%7CvVersion%7C5.2.0; _fbp=fb.2.1729064013174.509957913488493088; hng.sig=to18pG508Hzz7EPB_okhuQu8kDUP3TDmLlnu4IbIOY8; EGG_SESS=S_Gs1wHo9OvRHCMp98md7P9EtbE2pMTHAJbU0wngNEqmSvQ0wmWSjVnCwXD9_Hc2jpE_4A_KuAcK1UsVYLEftMD2szWjqCtl6XxySXpmvODQEvG78XgpOjiosjt6Ud4kHOf0P6zPnNcnJd13E33CNoUzeZ-PT5M_kN1m5Qrmokg=; lzd_sid=112cf3225c3fd60da5b0df97a1102f35; _tb_token=f45ee35a844a0; t_sid=kZXiZE2MMCOKJNarGRLOqZkYyxRddX97; utm_channel=NA; xlly_s=1; x5sec=7b22617365727665722d6c617a6164613b33223a22617c434a2f566f4c6b47454e76722b49594249676c795a574e686348526a614745776f39795979514e4b556a41304d446c6d5a6a41774d4441774d4441774d4451774d4441774d4441774d4441774d4441774d4441774d4441774d4441774d4441774d4441774d4441774e445933596d566b5a6d4d794f5759794d5759304d544e6c4e57557a4e7a55794e7a41774d4441774d4441774d44453d222c22733b32223a2232346265623163373437343963363464227d; tfstk=fD-E6Z2H8DnEPIyvt6SP3PGj08Qd4Mcfx315ELvld6f3AkNk7CdzFvh-JF5ys19BVMj7ahRMGU9I9esrU198V6_SpCypbIr7AX3pEuSfqjGjcm9LpgIoGN7YbU1dedfoJ-usWpIRqfGjcm9ppIfhEzCFqAoGhtIutkAlScfOeTVhEkDwI3EJMPDzawwWF1YSMHuEzlvN_uqy697GimCaquxNLS1DK4EuqhWFJ3pvcGShRUvAkH_r4lIB3FjGLQmmtNLHQ37v24GpBM5eHN8tTlX6QLYf7hMmDMShtUspF-lBQHRBphJ7EyRylBLAz3cU01xd4uNRIHXe2ePurwq5QsMZQL27s1fiwy7UyzQdBO5jK5aurSEYVy-SdzURRPBNGv41.",
                    "Sec-Fetch-Dest":"empty",
                    "Sec-Fetch-Mode":"cors",
                    "Sec-Fetch-Site":"same-origin"
                }
                yield scrapy.Request(url=f"https://www.lazada.co.id/{url}/?ajax=true&from=wangpu&isFirstRequest=true&langFlag=id&page={page}&pageTypeId=2&q=All-Products",method='GET',headers=headers,cookies=cookies,callback=self.parse)
    def parse(self, response):
        data=json.loads(response.body)
        print(len(data['mods']['listItems']))
        for i in range(0,len(data['mods']['listItems'])):
            item=LazadaOsaItem()
            item["name"]=data['mods']['listItems'][i]['name']
            item["url"]=data['mods']['listItems'][i]['itemUrl']
            item['link_id']=data['mods']['listItems'][i]['itemUrl']
            item['sku']='i'+str(data['mods']['listItems'][i]['nid'])
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

