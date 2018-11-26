# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector
from scrapy import Request
#from PIL import Image
#import urllib.request
import datetime
import os

class xiangq(scrapy.Spider):
    name = "xiangq"
    host = "http://date.jobbole.com/"

    start_urls = [
        "http://date.jobbole.com/tag/shanghai/",
    ]

    def start_requests(self):
        for i in range(3):
            url = self.host + 'tag/shanghai/page/%d/'%(i+1) #翻页
            yield Request(url=url,callback=self.parse)

    def parse(self, response):
        selector = Selector(response)
        content_list = selector.xpath("//*[@class=\"media\"]/div[@class=\"media-body\"]/h3/a[@target=\"_blank\"]/@href").extract()
        for content in content_list:
            url = content
            yield Request(url=url,meta={'url':url},callback=self.parse_dl)

    def parse_dl(self,response):
        pil = response.meta['url']
        selector = Selector(response)
        listcon = selector.xpath("//*[@class=\"p-single\"]/div[@class=\"p-entry\"]/p[1]").extract()
        lis = listcon[0]
        try:
            a = int(lis[8:12])
        except ValueError:
            print(ValueError)
        else:
            if int(lis[8:12]) >= 1990:
              print(int(lis[8:12]))
              p = pil + '\n'
              curPath = os.path.abspath(os.path.dirname(__file__))
              envPath = os.path.join(curPath, "a.txt")
              file = open(envPath, 'a') #使用a模式打开文件，指针指向文件末尾，所以直接在文件末尾新增内容
              file.write(p)
              file.close()






