# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector
from scrapy import Request
#from PIL import Image
#import urllib.request
import datetime
from pachong.items import doubanItem
#import os
nowTime = datetime.datetime.now().strftime('%Y%m%d')
nowTimes = datetime.datetime.now().strftime('%Y%m%d%H%M%S')

class douban_moviestar(scrapy.Spider):
    name = 'douban_moviestar'
    host = 'https://movie.douban.com'
    start_url = [
        'https://movie.douban.com/top250',
        ]

    def start_requests(self):
        for i in range(10):
            url = self.host + '/top250?start=%d&filter='%(i*25) #翻页
            yield Request(url=url,callback=self.parse)

    def parse(self, response):

        selector = Selector(response)
        content_list = selector.xpath("//*[@class=\"grid_view\"]/li/div[1]/div[2]/div[1]/a[1]/@href").extract()
        for content in content_list:
            url = content
            yield Request(url=url,callback=self.parse_dl)

    def parse_dl(self,response):
        item = doubanItem()  #实例化
        selector = Selector(response)
        title = selector.xpath("//div[@id=\"wrapper\"]/div[@id=\"content\"]/h1/span[1]/text()").extract()[0]
        img = selector.xpath("//*[@id=\"mainpic\"]/a[@class=\"nbgnbg\"]/img/@src").extract()[0]
        director = selector.xpath("//*[@class=\"subject clearfix\"]/div[2]/span[1]/span[@class=\"attrs\"]/a[@rel=\"v:directedBy\"]/text()").extract()[0]
        tp_list = selector.xpath("//*[@class=\"subject clearfix\"]/div[2]/span[@property = \"v:genre\"]/text()").extract()
        type = '/'.join(tp_list)
        country = selector.xpath("//*[@class=\"subject clearfix\"]/div[2]/span[text()=\"制片国家/地区:\"]/following::text()[1]").extract()[0]
        sorce = selector.xpath("//*[@id=\"interest_sectl\"]/div[1]/div[2]/strong[@class=\"ll rating_num\"]/text()").extract()[0]
        act_list = selector.xpath("//*[@class=\"subject clearfix\"]/div[2]/span[@class=\"actor\"]/span[@class=\"attrs\"]/a[@rel=\"v:starring\"]/text()").extract()
        starring = '/'.join(act_list)
        item['title'] = title
        item['img'] = img
        item['director'] = director
        item['type'] = type
        item['country'] = country
        item['sorce'] = sorce
        item['starring'] = starring
        yield item




















