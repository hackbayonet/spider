# -*- coding: utf-8 -*-
'''
Created on 2016年11月1日
'''
from qiushibaike import output_data, html_downloader, url_manager, html_parser, logger
import socket
import threading
import os
import json
try:
    from urllib.error import HTTPError as  URLError
except ImportError:
    from urllib2 import URLError

class SpiderMian(object):

    
    def __init__(self):
        self.timer = threading.Timer(3, self.showinfo)
        self.htmlDownload = html_downloader.htmlDownload()
        self.urls = url_manager.urlManager()
        self.htmlParser = html_parser.htmlParser()
        self.outputData = output_data.outputData()
        self.spiderCount = 0
        self.dataConut = 0
        self.status = False
    
    def showinfo(self):
        if self.status:
            return
        
        logger.info('Get to %d URL per second, already crawling count: %d, wait crawling count: %d' % 
                    (self.spiderCount, 
                     self.urls.already_crawling_count(),
                     self.urls.wait_crawling_count())
                    )
        self.spiderCount = 0
        threading.Timer(3, self.showinfo).start()
        new_urls_file = open('new_urls.txt', 'w')
        old_urls_file = open('old_urls.txt', 'w')
        for url in self.urls.new_urls:
            # 清除之前的换行符。 并添加新的换行
            new_urls_file.write(url.replace('\n', '') + '\n')
        for url in self.urls.old_urls: 
            old_urls_file.write(url.replace('\n', '') + '\n')
        new_urls_file.close()
        old_urls_file.close()
        
    
    
    def crawler(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        self.timer.start()
        while self.urls.has_new_url():
            new_url = self.urls.get_new_url()
            logger.info('creawl %d : %s' % (count, new_url))
            try:
                html_content = self.htmlDownload.urllib(new_url)
                new_urls, new_data = self.htmlParser.parser(new_url, html_content)
                self.spiderCount += len(new_urls)
                self.dataConut += len(new_urls)
                self.urls.add_new_urls(new_urls)
                self.outputData.xml(new_data , new_url)
            except socket.timeout:
                logger.error('crawler fail Error: timeout')
                self.urls.add_error_url(new_url)
            except TypeError:
                logger.error('crawler fail Error: TypeError')
            except URLError:
                logger.error('crawler fail Error: URLError')
                self.urls.add_error_url(new_url)
            except:
                pass
            count += 1


if __name__ == '__main__':
        obj_spider = SpiderMian()
        if os.path.exists('new_urls.txt') and os.path.exists('old_urls.txt'):
            new_urls_file = open('new_urls.txt', 'r')
            old_urls_file = open('old_urls.txt', 'r')
            obj_spider.urls.reload_urls(new_urls_file.readlines(), old_urls_file.readlines())
            old_urls_file.close()
            new_urls_file.close()
            root_url = None
        else:
            root_url = 'http://www.qiushibaike.com/'
        try:
            obj_spider.crawler(root_url)
        except KeyboardInterrupt:
            obj_spider.status = True
            exit()
        
