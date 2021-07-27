from sqlalchemy.sql.sqltypes import Boolean, DateTime
from database import Base
from sqlalchemy import Column,Integer,String,Boolean,DateTime

class User(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True,index=True)
    user_email=Column(String)
    password=Column(String)
    user_name=Column(String)
    user_city=Column(String)
    email_verify=Column(Boolean)
    otp_time=Column(DateTime)
    otp=Column(Integer)