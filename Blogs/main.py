'''Global imports'''
from fastapi import FastAPI,Depends,Path,Query,HTTPException
from typing import Annotated
from sqlalchemy.orm import Session
from starlette import status

'''local imports'''
from database import engine,SessionLocal
from schema import BlogsRequest,BlogsR
import models
from models import Blogs

app=FastAPI()

'''creating all modles'''
models.Base.metadata.create_all(engine)

'''database dependencies'''
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

'''dependency and session for database'''
Dependency= Annotated[Session, Depends(get_db)]


'''
Http Post method
Getting all blogs
'''
@app.get('/blogs',status_code=status.HTTP_200_OK)
async def getAllBlogs(db:Dependency):
    blogs=db.query(Blogs).all()
    if blogs:
        return blogs
    raise HTTPException(status_code=500, detail='Internal Server error')

'''getting blogs based on id (query parameter)'''
@app.get('/blogs/',status_code=status.HTTP_200_OK)
async def getBlogById(db:Dependency,id:int = Query(gt=0)):
    blog=db.query(Blogs).filter(Blogs.id==id).first()
    if blog:
        return blog
    raise HTTPException(status_code=404, detail='details not found')

'''getting blogs based on author name (path parameter)'''
@app.get('/blogs/{author}',status_code=status.HTTP_200_OK)
async def blogsByAuthor(db:Dependency,author:str=Path(max_length=15)):
    blogs=db.query(Blogs).filter(Blogs.Author==author).all()
    if not blogs:
        raise HTTPException(status_code=404,detail='Details by author not found')
    return blogs

'''
Http post method
creating a new blog
'''
@app.post('/create',status_code=status.HTTP_201_CREATED)
async def createBlog(request:BlogsRequest,db:Dependency):
    try:
        newBlog=Blogs(
            Blog_Name=request.Blog_Name,
            In_Language=request.In_Language,
            Author=request.Author,
            Published_Date=request.Published_Date,
            Rating=request.Rating,
            Is_Active=request.Is_Active
        )
        db.add(newBlog)
        db.commit()
        return {'status':'blog created'}
    except:
        raise HTTPException(status_code=500,detail='internal server error')

'''
Http Put Method
updating blog by id
'''
@app.put('/update')
async def updateBlog(db:Dependency,request:BlogsRequest,id:int=Query(gt=0)):
    blog=db.query(Blogs).filter(Blogs.id==id).first()
    if blog is None:
        raise HTTPException(status_code=404,detail='details not found')
    blog.Blog_Name=request.Blog_Name,
    blog.In_Language=request.In_Language,
    blog.Author=request.Author,
    blog.Published_Date=request.Published_Date,
    blog.Rating=request.Rating,
    blog.Is_Active=request.Is_Active

    db.add(blog)
    db.commit()
    return {'status':'blog updated'}

'''
Http Delete method
Deleting blog using id
'''

@app.delete('/delete')
async def deleteBlog(db:Dependency,id:int=Query(gt=0)):
    blog=db.query(Blogs).filter(Blogs.id==id).first()
    if blog is None:
        raise HTTPException(status_code=404,detail='Details not found')
    db.delete(blog)
    db.commit()
    return {'status':'Blog Deleted'}

'''
Use of Http Post Method Instead of Http Get Method to retreive Data (by using the Post Body) 
'''
@app.post('/getblogs')
async def getBlogsByPostMethod(db:Dependency,request:BlogsR):
    blogs=db.query(Blogs).filter(Blogs.Author==request.Author).all()
    if blogs is None:
        raise HTTPException(status_code=404,detail='Details not Found')
    return blogs