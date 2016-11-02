# -*- coding: utf-8 -*-
'''
Created on 2016年11月1日
'''


class urlManager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()
    
    def add_new_url(self, url):
        if url is None:
            return
        
        if  url not in self.old_urls and url not in self.new_urls: 
            self.new_urls.add(url)
    
    def already_crawling_count(self):
        return len(self.old_urls)
    
    def wait_crawling_count(self):
        return len(self.new_urls)
    
    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url

    
    def has_new_url(self):
        return len(self.new_urls) != 0

    
    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)
            
    def add_error_url(self, error_url):
        self.old_urls.remove(error_url)
        self.new_urls.add(error_url)
        
        
        