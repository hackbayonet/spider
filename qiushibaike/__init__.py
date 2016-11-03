# -*- coding: utf-8 -*-
import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pymysql

# log 
logger = logging.getLogger()
ConnectHandler = logging.StreamHandler()
formatter = logging.Formatter(
        '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
ConnectHandler.setFormatter(formatter)
logger.addHandler(ConnectHandler)
logger.setLevel(logging.DEBUG)

fileHandler = logging.FileHandler('test.log')
fileHandler.setFormatter(formatter)
fileHandler.setLevel(logging.DEBUG) 
logger.addHandler(fileHandler)


# database
pymysql.install_as_MySQLdb()
DB_CONNECT_STRING = 'mysql+mysqldb://root:cidao1!@localhost/qiushibaike?charset=utf8'
engine = create_engine(DB_CONNECT_STRING, echo=True)
DB_Session = sessionmaker(bind=engine)
session = DB_Session()