# -*- coding: utf-8 -*-
'''
Created on 2016年11月1日
'''
from qiushibaike import output_data, html_downloader, url_manager, html_parser, logger
import socket
import threading

class SpiderMian(object):

    
    def __init__(self):
        self.timer = threading.Timer(3, self.showinfo)
        self.htmlDownload = html_downloader.htmlDownload()
        self.urls = url_manager.urlManager()
        self.htmlParser = html_parser.htmlParser()
        self.outputData = output_data.outputData()
        self.spiderCount = 0
        self.dataConut = 0
    
    def showinfo(self):
        logger.info('Get to %d URL per second, already crawling count: %d, wait crawling count: %d' % 
                    (self.spiderCount, 
                     self.urls.already_crawling_count(),
                     self.urls.wait_crawling_count())
                    )
        self.spiderCount = 0
        threading.Timer(3, self.showinfo).start()
    
    
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
            except socket.timeout:
                self.urls.add_error_url(new_url)
            except TypeError:
                pass
            self.urls.add_new_urls(new_urls)
            self.outputData.mysql(new_data)
            count += 1


if __name__ == '__main__':
    root_url = 'http://www.qiushibaike.com/'
    obj_spider = SpiderMian()
    obj_spider.crawler(root_url)
