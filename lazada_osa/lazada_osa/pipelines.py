# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column
from lazada_osa.lazada_table import Base,LazadaTable
from sqlalchemy.orm import Session


class LazadaOsaPipeline:
    def open_spider(self,item):
        self.engine=create_engine('postgresql://salesanalyst:**salesanalyst*@103.190.223.194:5432/scrapping_osa')
        Base.metadata.create_all(self.engine)
    
    def process_item(self, item, spider):
        item=ItemAdapter(item)
        if item['original_price']=="":
             item['original_price']="0"
        with Session(self.engine) as session:
                table=LazadaTable(name=item['name'],
                                url=item['url'],
                                stock=item['stock'],
                                sku=item['sku'],
                                link_id=item['link_id'].split('-')[-1].replace('.html',''),
                                count_sold=item['count_sold'].split("%")[23],
                                rating=item['rating'],
                                review=item['review'],
                                price=item['price'],
                                shop_name=item['shop_name'],
                                category=item['category'].split("%")[23],
                                original_price=item['original_price']
                                )
                session.add(table)
                session.commit()
                return item
    


