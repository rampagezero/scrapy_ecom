from sqlalchemy.orm import Mapped
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import DateTime,Column,Integer,Text
from sqlalchemy.sql import func
import datetime
Base=declarative_base()
class BlibliTable(Base):
    __tablename__='BlibliData'
    id=Column(Integer,primary_key=True,auto_increment=True)
    name=Column(String(50))
    sku=Column(String(50))
    url=Column(String(50))
    stock=Column(String(50))
    rating=Column(String(50))
    review=Column(String(50))
    price=Column(String(50))
    original_price=Column(Text,default=None)
    shop_name=Column(String(50))
    category=Column(String(50))
    date= Column(DateTime(timezone=True), server_default=func.now())
