'''global imports'''
from pydantic import BaseModel,Field
from typing import Optional


'''Blogs table schema and validation'''
class BlogsRequest(BaseModel):

    Blog_Name:str = Field(min_length=4,max_length=15)
    In_Language:str = Field(min_length=4,max_length=15)
    Author:str = Field(min_length=2,max_length=15)
    Published_Date:Optional[str] | None
    Rating:int = Field(gt=0,lt=6)
    Is_Active:bool

    '''example schema confi.'''
    class Config:
        json_schema_extra = {
            'example':{
                'Blog_Name':'Atomic Habits',
                'In_Language':'English',
                'Author':'Hurry Enland',
                'Published_Date':'01-02-2023',
                'Rating':'4',
                'Is_Active':True
            }
        }

'''schema for gettiing data by post method using post body'''
class BlogsR(BaseModel):
    Author:str=Field(min_length=3,max_length=15)

    class Config:
        json_schema_extra = {
            'example':{
                'Author':'Enric Will'
            }
        }