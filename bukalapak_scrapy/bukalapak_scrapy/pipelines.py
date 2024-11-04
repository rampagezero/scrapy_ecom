# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column
from bukalapak_scrapy.bukalapak_table import Base,BukaTable
from sqlalchemy.orm import Session


class BukalapakScrapyPipeline:
    def open_spider(self,item):
        self.engine=create_engine('postgresql://salesanalyst:**salesanalyst*@103.190.223.194:5432/scrapping_osa')
        Base.metadata.create_all(self.engine)
    
    def process_item(self, item, spider):
        with Session(self.engine) as session:
            table=BukaTable(skuid=item['skuid'],
                              url=item['url'],
                              stock=item['stock'],
                              )
            session.add(table)
            session.commit()
        return item
    
    def close_spider(self):
        try:
            with Session(self.engine) as session:
                session.commit()
                session.close()
        except:
            pass


