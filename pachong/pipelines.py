# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql.cursors
from decimal import Decimal


class doubanPipeline(object):
    def process_item(self, item,douban_moviestar):
        title = item['title']
        img = item['img']
        director = item['director']
        type = item['type']
        country = item['country']
        country = country.replace(' ','') # 去除字符串中的空格
        sorce = item['sorce']
        source = Decimal(float(sorce))
        starring = item['starring']
        connection = pymysql.connect(host = '127.0.0.1',user = 'root',password = '123456',port = 3306,db = 'mysql',charset = 'utf8')
        cursor = connection.cursor()
        sql = 'insert into `douban_moviestar` values("0","%s","%s","%s","%s","%s","%.1f","%s")'%(title,img,director,type,country,source,starring)
        print('ok')
        cursor.execute(sql) #执行sql
        cursor.close()
        connection.commit()
        print('成功插入一条数据')
        connection.close()

