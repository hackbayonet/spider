# -*- coding: utf-8 -*-
'''
Created on 2016年11月1日
'''
try:
    import urllib.request as urllib2
    from urllib.error import HTTPError as  URLError
except ImportError:
    import urllib2
    from urllib2 import URLError


from qiushibaike import logger

class htmlDownload(object):
    
    def urllib(self, url):
        response = None
        header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
        request = urllib2.Request(url=url, headers=header)
        try:
            response = urllib2.urlopen(request, timeout=10)
        except URLError as e:
            if hasattr(e, 'code'):
                logger.error('spider download error status code is (%d)', e.code)
        else:
            return response.read()
        finally:
            if response:
                response.close()
        