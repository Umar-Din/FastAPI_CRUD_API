'''global imports'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

'''database url'''
SQLALCHEMY_DATABASE_URL = "sqlite:///./BLOGSDATABASE.db"

'''engine instance'''
engine=create_engine(SQLALCHEMY_DATABASE_URL,connect_args={"check_same_thread":False})

SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base=declarative_base()
