from database import Base
from sqlalchemy import Column,Integer,String,MetaData

class User(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True,index=True)
    user_email=Column(String)
    password=Column(String)
    user_name=Column(String)
    user_city=Column(String)
