# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector
from scrapy import Request
from PIL import Image
import urllib.request
import datetime
import os
nowTime = datetime.datetime.now().strftime('%Y%m%d')
nowTimes = datetime.datetime.now().strftime('%Y%m%d%H%M%S')

class NgaSpider(scrapy.Spider):
    name = "NgaSpider"
    host = "http://www.wmpic.me"
    start_urls = [
        "http://www.wmpic.me/page/1",
    ]


    def start_requests(self):
        urlforword = self.start_urls[0][25:]
        for i in range(500,502): #设定图片数量限制
          url = self.host + ('/page/%d'%(int(urlforword)+i))
          yield Request(url=url, callback=self.parse)


    def parse(self, response):
        n = -1
        selector = Selector(response)
        content_list = selector.xpath("//*[@class=\"item_box\"]/div[1]/a[@target=\"_blank\"]")
        img_list = selector.xpath("//*[@class=\"item_box\"]/div[1]/a[@target=\"_blank\"]/img/@src").extract()
        for cont in content_list:
            n+= 1
            href = cont.xpath("@href").extract()#href为列表
            #print('href:'+ href[0][1:])
            imgcon = img_list[n]
            #print(imgcon)
            os.mkdir("D:/spiderpic/%s" % href[0][1:])
            file = urllib.request.urlopen(imgcon)
            #conbtye = content.encode()
            #temp = file.read()
            image = Image.open(file)
            image.save('D:/spiderpic/%s/%s%d封面图.png'%(href[0][1:],nowTime,n)) #格式化入参只提供一个%
            url = self.host + href[0]
            yield Request(url=url,meta={'href':href[0][1:]},callback=self.parse_dl)#参数集合可以用meta=完成


    def parse_dl(self,response):
        m = 0
        dirname = response.meta['href']
        selector = Selector(response)
        contentlist = selector.xpath("//*[@class =\"content-c\"]/center/p/img/@src").extract()
        for con in contentlist:
            m+= 1
            #print('m:'+ str(m))
            fd = urllib.request.urlopen(con)
            image = Image.open(fd)
            image.save('D:/spiderpic/%s/%s%d内容图.png' % (dirname, nowTimes, m))



