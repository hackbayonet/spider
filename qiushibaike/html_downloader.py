# -*- coding: utf-8 -*-
'''
Created on 2016年11月1日
'''
from urllib.error import HTTPError
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2



class htmlDownload(object):
    
    def urllib(self, url):
        response = None
        header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
        request = urllib2.Request(url=url, headers=header)
        try:
            response = urllib2.urlopen(request, timeout=30)
        except HTTPError as e:
            if hasattr(e, 'code'):
                print('Error code:', e.code)
            elif hasattr(e, 'reason'):
                print('Reason:',e.reason)
        else:
            return response.read()
        finally:
            if response:
                response.close()
        