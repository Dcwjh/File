# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import requests
from scrapy import signals
import random


class ZhihuuserUser_agentMiddleware(object):
    def __init__(self, agents):
        self.agents = agents

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings.getlist('USER_AGENTS'))

    def process_request(self, request, spider):
        # print "**************************" + random.choice(self.agents)
        request.headers.setdefault('User-Agent', random.choice(self.agents))


# class ZhihuuserProxyMiddleware(object):
#     # Not all methods need to be defined. If a method is not defined,
#     # scrapy acts as if the downloader middleware does not modify the
#     # passed objects.
#
#     def __init__(self, proxy):
#         self.proxy = proxy
#
#     @classmethod
#     def from_crawler(cls, crawler):
#         return cls(crawler.settings.getlist('PROXIES'))
#
#     def process_request(self, request, spider):
#         # print "**************************" + random.choice(self.agents)
#         request.meta['proxy'] = "http://" + self.proxy

import base64

# 代理服务器
proxyServer = "http://http-dyn.abuyun.com:9020"

# 代理隧道验证信息
proxyUser = "H1HE86N4GL96486D"
proxyPass = "06CCB195E4515352"





# for Python2
#proxyAuth = "Basic " + base64.b64encode(proxyUser + ":" + proxyPass)oxyPass)

# for Python3
proxyAuth = "Basic " + base64.urlsafe_b64encode(bytes((proxyUser + ":" + proxyPass), "ascii")).decode("utf8")

class ProxyMiddleware(object):
    def process_request(self, request, spider):
        request.meta["proxy"] = proxyServer

        request.headers["Proxy-Authorization"] = proxyAuth
