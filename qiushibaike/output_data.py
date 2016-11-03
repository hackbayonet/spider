# -*- coding: utf-8 -*-
'''
Created on 2016年11月1日
'''
import os
from qiushibaike import logger

class outputData(object):
    
    
    def mysql(self, data):
        pass
    

    def xml(self, data, url):
        if data is None or len(data) == 0:
            return 0
        path = os.path.join(u'数据', data['name'])
        try:
            os.mkdir(path)
        except OSError:
            pass
        
        path = os.path.join(path, data['title'].replace('\n', ''))
        
        path = path.replace(u' - 糗事百科', '') + '.xml'
        file = open(path.encode('utf-8'), 'w')
        
            
        file.write('<?xml version="1.0" encoding="utf-8"?>\r\n')
        file.write('<data>\n')
        file.write('<title>%s</title>\n' % (data['title'].encode('utf-8')))
        file.write('<url>%s</url>\n' %  (url))
        file.write('<content>\n')
        for text in data['text']:
            file.write(text.encode('utf-8'))
        file.write('</content>\n')
        file.write('</data>\n')
        logger.info('sava : %s ok!' % (path))