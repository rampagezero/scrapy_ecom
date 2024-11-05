# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class BlibliPipeline:
    def process_item(self, item, spider):
        return item
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from sqlalchemy import create_engine
from sqlalchemy.orm import Mapped
from blibli.blibli_table import Base,BlibliTable
from sqlalchemy.orm import Session


class BlibliPipeline:
    def open_spider(self,item):
        self.engine=create_engine('postgresql://salesanalyst:**salesanalyst*@192.168.33.182:5432/scrapping_osa')
        Base.metadata.create_all(self.engine)
    
    def process_item(self, item, spider):
        item=ItemAdapter(item)
        if item['original_price']=="":
             item['original_price']="0"
        with Session(self.engine) as session:
                table=BlibliTable(name=item['name'],
                                url=item['url'],
                                stock=item['stock'],
                                sku=item['sku'],
                                rating=item['rating'],
                                review=item['review'],
                                original_price=item['original_price'],
                                price=item['price'], 
                                shop_name=item['shop_name'],
                                category=item['category']
                                )
                session.add(table)
                session.commit()
                return item
    


