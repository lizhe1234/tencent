# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class DoubanbookItem(scrapy.Item):
    # # 图书详情页链接
    # link=scrapy.Field()
    # # 图书名称
    # title=scrapy.Field()
    # # 作者,出版信息,价格等信息
    # info=scrapy.Field()
    # # 豆瓣评分
    # rating=scrapy.Field()
    # # 引论
    # quote=scrapy.Field()
    positionname = scrapy.Field()
    positionlink = scrapy.Field()
    positionType = scrapy.Field()
    positionNum = scrapy.Field()
    positionLocation = scrapy.Field()
    publishTime = scrapy.Field()