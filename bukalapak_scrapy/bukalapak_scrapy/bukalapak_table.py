from sqlalchemy.orm import Mapped
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import DateTime,Column,Integer,Text
from sqlalchemy import Column, Integer, String
from sqlalchemy.sql import func
import datetime
Base=declarative_base()

class BukaTable(Base):
    __tablename__='BukalapakData'
    id=Column(Integer,primary_key=True,auto_increment=True)
    skuid=Column(String(50))
    url=Column(String(50))
    stock=Column(String(50))
    date=Column(DateTime(timezone=True), server_default=func.now())
