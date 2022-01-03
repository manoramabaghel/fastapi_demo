import os

from sqlalchemy import create_engine  # type: ignore
from sqlalchemy.ext.declarative import declarative_base  # type: ignore
from sqlalchemy.orm import sessionmaker  # type: ignore
import urllib
from config import config

# host = 'localhost'
# port = '3306'
# user = 'manoj'
# password = 'Manoj@123'
# db = 'demo'
# dbtype = "mysql+pymysql"
# SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:%s@localhost/imdb' % urllib.parse.quote('Manoj@123')
SQLALCHEMY_DATABASE_URI = f"{config.DBTYPE}://{config.USER}:%s@{config.HOST}:{config.PORT}/{config.DB}" % urllib.parse.quote(config.PASSWORD)

engine = create_engine(SQLALCHEMY_DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
