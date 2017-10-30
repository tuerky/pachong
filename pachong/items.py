# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class doubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()  #对应数据库字段
    img = scrapy.Field()
    director = scrapy.Field()
    type = scrapy.Field()
    country = scrapy.Field()
    sorce = scrapy.Field()
    starring = scrapy.Field()
