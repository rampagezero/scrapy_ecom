# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from itemadapter import ItemAdapter
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column
from bliblipng.bliblipngtable import Base,BlibliTable
from sqlalchemy.orm import Session

class BliblipngPipeline:
    def open_spider(self,item):
        self.engine=create_engine('postgresql://salesanalyst:**salesanalyst*@103.190.223.194:5432/scrapping_osa')
        Base.metadata.create_all(self.engine)
    
    def process_item(self, item, spider):
        item=ItemAdapter(item)
        if item['original_price']=="":
             item['original_price']=0
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
                                sold=item['sold']
                                )
                session.add(table)
                session.commit()
                return item
    


