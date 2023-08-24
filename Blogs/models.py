'''global imports'''
from sqlalchemy import Column,Integer,Boolean,String
'''local imports'''
from database import Base

'''creating Blogs Model'''
class Blogs(Base):
    __tablename__ = "blogs"

    id=Column(Integer,primary_key=True,index=True)
    Blog_Name=Column(String)
    In_Language=Column(String)
    Author=Column(String)
    Published_Date=Column(String,default=None)
    Rating=Column(Integer)
    Is_Active=Column(Boolean,default=True)