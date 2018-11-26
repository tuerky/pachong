#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "tuerky"
# Date: 2018/3/19
import scrapy
import requests
import json
from scrapy import Selector
from scrapy import Request
# from PIL import Image
# import urllib.request
import datetime
import re
from pachong.items import musicItem

# import os
nowTime = datetime.datetime.now().strftime('%Y%m%d')
nowTimes = datetime.datetime.now().strftime('%Y%m%d%H%M%S')


def parse_dl(response):
    pic_url = response.meta['pic']
    id = response.meta['id']
    # html = str(response.body, 'utf-8')
    selector = Selector(response)
    title = selector.xpath("//div[@class=\"cnt\"]/div[1]/div[1]/em/text()").extract()[0]
    singer = selector.xpath("//div[@class=\"cnt\"]/p[1]/span[1]/a/text()").extract()[0]
    album = selector.xpath("//div[@class=\"cnt\"]/p[2]/a/text()").extract()[0]

    lyr_url = 'http://music.163.com/api/song/lyric?id=%s&lv=1&kv=1&tv=-1' % id
    reback = requests.get(url=lyr_url)
    Lyric = reback.text
    lyc = json.loads(Lyric)
    ly1 = lyc['lrc']['lyric']  # 多歌词层列
    if lyc['klyric']['lyric'] is None or lyc['klyric']['lyric'] == '':
        ly2 = ''
    else:
        ly2 = lyc['klyric']['lyric']
    if lyc['tlyric']['lyric'] is None or lyc['tlyric']['lyric'] == '':  # python null --> none
        ly3 = ''
    else:
        ly3 = lyc['tlyric']['lyric']
    ly = ly1 + ly2 + ly3
    rv = re.compile(
        r'(\[(.*)\]|'')((.{2,})(：| : | ：)(.*)\n|'')')  # 正则或条件 | 中括号包含的全部或者为''，接着如果后续为''也匹配，接着只匹配冒号左边两个以上字符，最后如果是：或 :也匹配
    lyric = re.sub(rv, '', ly)
    song_id = id
    item = musicItem()
    item['title'] = title
    item['pic_url'] = pic_url
    item['singer'] = singer
    item['album'] = album
    item['song_id'] = song_id
    item['lyric'] = lyric
    yield item


class music_original(scrapy.Spider):
    name = 'music_original'
    host = 'http://music.163.com/'
    start_url = [
        'http://music.163.com/discover/toplist?id=19723756',
    ]

    def start_requests(self):
        url = self.start_url[0]
        yield Request(url=url, callback=self.parse)

    def parse(self, response):
        html = str(response.body, 'utf-8')
        url_list = re.findall(
            r'<li><a href="/song\?id=(\d*?)">', html)  # 非贪婪匹配，*默认贪婪匹配 ,\? 转义匹配自身
        pic_list = re.findall(
            r'"picUrl":"(.*?)"', html
        )
        for i in range(100):
            url = self.host + 'song?id=' + url_list[i]
            pic_url = pic_list[i]

            yield Request(url=url, meta={'pic': pic_url, 'id': url_list[i]}, callback=parse_dl)  # 参数集合可以用meta=完成

