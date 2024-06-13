from sqlalchemy.orm import Mapped,DeclarativeBase
from sqlalchemy import DateTime,Column,Integer,Text
from sqlalchemy.sql import func
import datetime
class Base(DeclarativeBase):
    pass

class BlibliTable(Base):
    __tablename__='BlibliDataPng'
    id=Column(Integer,primary_key=True,auto_increment=True)
    name:Mapped[str]
    sku:Mapped[str]
    url:Mapped[str]
    stock:Mapped[str]
    sold:Mapped[int]=Column(Text,default=None)
    rating:Mapped[str]
    review:Mapped[str]
    price:Mapped[int]
    original_price:Mapped[float]=Column(Text,default=None)
    shop_name:Mapped[str]
    date:Mapped[datetime.datetime]= Column(DateTime(timezone=True), server_default=func.now())