from sqlalchemy.orm import Mapped,DeclarativeBase
from sqlalchemy import DateTime,Column,Integer,Text
from sqlalchemy.sql import func
import datetime
class Base(DeclarativeBase):
    pass
class LazadaTable(Base):
    __tablename__='LazadaTable'
    id=Column(Integer,primary_key=True,auto_increment=True)
    name:Mapped[str]
    count_sold:Mapped[str]
    sku:Mapped[str]
    url:Mapped[str]
    link_id:Mapped[str]
    stock:Mapped[str]
    rating:Mapped[str]
    review:Mapped[str]
    price:Mapped[str]
    shop_name:Mapped[str]
    category:Mapped[str]
    original_price:Mapped[str]=Column(Text,default=None)
    date:Mapped[datetime.datetime]= Column(DateTime(timezone=True), server_default=func.now())
