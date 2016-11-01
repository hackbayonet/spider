# -*- coding: utf-8 -*-
'''
Created on 2016年11月1日
'''
from qiushibaike import output_data, html_downloader, url_manager, html_parser
import socket


class SpiderMian(object):
    def __init__(self):
        self.htmlDownload = html_downloader.htmlDownload()
        self.urls = url_manager.urlManager()
        self.htmlParser = html_parser.htmlParser()
        self.outputData = output_data.outputData()
    
    def crawler(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            new_url = self.urls.get_new_url()
            print('creawl %d : %s' % (count, new_url))
            try:
                html_content = self.htmlDownload.urllib(new_url)
                new_urls, new_data = self.htmlParser.parser(new_url, html_content)
            except socket.timeout:
                self.urls.add_error_url(new_url)
            except TypeError:
                print('NoneType')
            self.urls.add_new_urls(new_urls)
            self.outputData.mysql(new_data)
            if count == 1000:
                break
            count += 1


if __name__ == '__main__':
    root_url = 'http://www.qiushibaike.com/'
    obj_spider = SpiderMian()
    obj_spider.crawler(root_url)
