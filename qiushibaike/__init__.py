# -*- coding: utf-8 -*-
import logging

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