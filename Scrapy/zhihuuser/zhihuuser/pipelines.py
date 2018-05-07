# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo

# class ZhihuPipeline(object):
    # mongo_uri = 'localhost'
    # mongo_db = 'zhihu'

    # def __init__(self, mongo_uri, mongo_db):
    #     self.mongo_uri = mongo_uri
    #     self.mongo_db = mongo_db
    #
    # @classmethod
    # def from_crawler(cls, crawler):
    #     return cls(
    #         mongo_uri=crawler.settings.get('MONGO_URI'),
    #         mongo_db=crawler.settings.get('MONGO_DATABASE')
    #     )
    #
    # def open_spider(self, spider):
    #     self.client = pymongo.MongoClient(self.mongo_uri)
    #     self.db = self.client[self.mongo_db]
    #
    # def close_spider(self, spider):
    #     self.client.close()
    #
    # def process_item(self, item, spider):
    #     self.db['user'].update({'url_token':item['url_token']},{'$set':item},True)
    #     return item




class ZhihuPipeline(object):

    def __init__(self):
        self.client = pymongo.MongoClient('localhost')
        self.db = self.client['zhihu']

    def process_item(self,item,spider):
        self.db['user'].update({'url_token':item['url_token']},{'$set':item},True)  # 字典形式
        print("保存成功")
        return item
