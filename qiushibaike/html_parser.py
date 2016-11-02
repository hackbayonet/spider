# -*- coding: utf-8 -*-
'''
Created on 2016年11月1日
'''
from lxml import etree  # @UnresolvedImport
try:
    from urlparse import urljoin
except ImportError:
    from urllib.parser import urljoin
import re


class htmlParser(object):
    
    def _get_data(self, html):
        content = set()
        datas = html.xpath('//*[@id="single-next-link"]//*/text()|\
        //*[@id="single-next-link"]//*/@src')
        if len(datas) == 0:
            return 
        for data in datas: 
            if re.search('^http', data):
                content.add(data)
            else:
                data = data.replace('\n','')
                content.add(data)
        return content
    
    def _get_all_urls(self, page_url, html):
        new_urls = set()
        links = html.xpath('//a/@href')
        for link in links:
            if re.search('^/users/\d+/', link) or re.search('^/article/\d+', link):
                url = urljoin(page_url, link)
                new_urls.add(url)
                
        return new_urls
    def parser(self, page_url, html_content):
        if html_content is None or page_url is None:
            return
        
        html = etree.HTML(html_content)
        new_urls = self._get_all_urls(page_url, html)
        new_data = self._get_data(html)
        return new_urls, new_data