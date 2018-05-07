# -*- coding: utf-8 -*-
import json
import random

import requests
from scrapy import Request,Spider

from zhihuuser.items import UserItem



class ZhihuSpider(Spider):
    name = "zhihu"
    allowed_domains = ["www.zhihu.com"]

    # proxies = ['http://218.73.130.15:28919', 'http://115.210.177.88:29884', 'http://171.12.166.202:24852', 'http://183.135.249.89:49209', 'http://113.120.60.75:37901', 'http://117.95.71.120:37919', 'http://59.57.28.102:49031', 'http://114.225.86.17:22889', 'http://113.121.40.192:24604', 'http://180.114.175.57:32668', 'http://140.224.98.61:23964', 'http://114.239.222.150:24020', 'http://121.205.181.1:25842', 'http://1.196.131.144:42945', 'http://60.175.199.80:31728', 'http://113.121.36.131:44372', 'http://60.186.158.96:38806', 'http://115.203.218.1:28144', 'http://180.122.150.222:40950', 'http://115.221.113.98:35053', 'http://120.39.115.146:36011', 'http://27.156.144.252:28258', 'http://117.57.91.253:24122', 'http://175.147.117.26:32569', 'http://222.191.168.212:33951', 'http://110.88.127.16:20156', 'http://222.89.81.104:40268', 'http://123.161.155.101:46400', 'http://140.250.139.203:25791', 'http://171.14.91.201:31777']
    user_url = 'https://www.zhihu.com/api/v4/members/{user}?include={include}'
    user_query = 'locations,employments,gender,educations,business,voteup_count,thanked_Count,follower_count,following_count,cover_url,following_topic_count,following_question_count,following_favlists_count,following_columns_count,answer_count,articles_count,pins_count,question_count,commercial_question_count,favorite_count,favorited_count,logs_count,marked_answers_count,marked_answers_text,message_thread_token,account_status,is_active,is_force_renamed,is_bind_sina,sina_weibo_url,sina_weibo_name,show_sina_weibo,is_blocking,is_blocked,is_following,is_followed,mutual_followees_count,vote_to_count,vote_from_count,thank_to_count,thank_from_count,thanked_count,description,hosted_live_count,participated_live_count,allow_message,industry_category,org_name,org_homepage,badge[?(type=best_answerer)].topics'

    start_user = 'excited-vczh'

    follows_url = 'https://www.zhihu.com/api/v4/members/{user}/followees?include={include}&offset={offset}&limit={limit}'
    follows_query = 'data[*].answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics'

    followers_url = 'https://www.zhihu.com/api/v4/members/{user}/followers?include={include}&offset={offset}&limit={limit}'
    followers_query = 'data[*].answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics'

    # ip = random.choice(proxies)
    

    def start_requests(self):
        # Request.meta['proxy'] = self.ip
        yield Request(self.user_url.format(user=self.start_user, include=self.user_query), callback=self.parse_user)
        yield Request(self.follows_url.format(user=self.start_user, include=self.follows_query, offset=0, limit=20),callback=self.parse_follows)
        yield Request(self.followers_url.format(user=self.start_user, include=self.followers_query, offset=0, limit=20),callback=self.parse_followers)

    def parse_user(self, response):
        # Request.meta['proxy'] = self.ip
        result = json.loads(response.text)
        item = UserItem()
        for field in item.fields:
            if field in result.keys():  #
                if result.get(field):
                    item[field] = result.get(field)
        print(response.url)

        yield item

        yield Request(self.follows_url.format(user=result.get('url_token'), include=self.follows_query, limit=20, offset=0), self.parse_follows)
        yield Request(self.followers_url.format(user=result.get('url_token'), include=self.followers_query, limit=20, offset=0), self.parse_followers)

    def parse_follows(self,response):
        # Request.meta['proxy'] = self.ip
        results = json.loads(response.text)
        if 'data' in results.keys():
            for result in results.get('data'):
                yield Request(self.user_url.format(user=result.get('url_token'),include=self.user_query),self.parse_user)

        if 'paging' in results.keys() and results.get('paging').get('is_end') == False:
            next_page = results.get('paging').get('next')
            yield Request(next_page,self.parse_follows)


    def parse_followers(self,response):
        # Request.meta['proxy'] = self.ip
        results = json.loads(response.text)
        if 'data' in results.keys():
            for result in results.get('data'):
                yield Request(self.user_url.format(user=result.get('url_token'),include=self.user_query),self.parse_user)

        if 'paging' in results.keys() and results.get('paging').get('is_end') == False:
            next_page = results.get('paging').get('next')
            yield Request(next_page,self.parse_followers)

