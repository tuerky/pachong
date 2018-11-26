# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql.cursors
from decimal import Decimal


'''class doubanPipeline(object):
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
        sql = 'insert into `swapi_moviestar` values("0","%s","%s","%s","%s","%s","%.1f","%s")'%(title,img,director,type,country,source,starring)#decimal(2,1)
        print('ok')
        cursor.execute(sql) #执行sql
        cursor.close()
        connection.commit()
        print('成功插入一条数据')
        connection.close()'''

class musicPipeline(object):
    def process_item(self, item, music_info):
        title = item['title']
        pic_url = item['pic_url']
        singer = item['singer']
        album = item['album']
        song_id = item['song_id']
        lyric = item['lyric']

        connection = pymysql.connect(host='127.0.0.1', user='root', password='123456', port=3306, db='mysql', charset='utf8')
        cursor = connection.cursor()
        sql = 'INSERT INTO `music_newest` VALUES ("0","%s","%s","%s","%s","%s","%s",NOW(),NOW())' % (title, pic_url, singer, album, song_id, lyric)
        print('ok')
        cursor.execute(sql)  # 执行sql
        cursor.close()
        connection.commit()
        print('成功插入一条数据')
        connection.close()