from sqlalchemy.orm import Mapped,DeclarativeBase
from sqlalchemy import DateTime,Column,Integer,Text
from sqlalchemy.sql import func
import datetime
class Base(DeclarativeBase):
    pass
class BukaTable(Base):
    __tablename__='BukalapakData'
    id=Column(Integer,primary_key=True,auto_increment=True)
    skuid:Mapped[str]
    url:Mapped[str]
    stock:Mapped[int]
    date:Mapped[datetime.datetime]= Column(DateTime(timezone=True), server_default=func.now())
