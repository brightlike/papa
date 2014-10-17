# -*- coding: utf-8 -*-

import urllib 
from scrapy.spider import Spider
from scrapy.selector import Selector

from jimome.items import JimomeItem

from sqlalchemy import *
from sqlalchemy.databases import mysql

class JimomeSpider(Spider):
    name = "jimome"

    # start_urls = [
    #     "http://www.youyuan.com/221939507-profile/"
    # ]

    def __init__(self, user_id=None, *args, **kwargs):
        super(JimomeSpider, self).__init__(*args, **kwargs)
        self.start_urls = ["http://www.youyuan.com/%s-profile/" % user_id]

    def parse(self, response):
        # filename = response.url.split("/")[-2]

        
        
        sel = Selector(response)
        # with open(filename, 'wb') as f:

        #     # src = sel.xpath("/html/head/title/text()").extract()[0].encode('utf-8')
        #     # src = response.selector.xpath("/html/head/title/text()")
        #     # print "src", src[0]

        #     src = sel.xpath("//dl[@class='personal_cen']/dt/img/@src").extract()[0]
        #     print "src", src
        #     f.write(src)


        # item = JimomeItem()
        # item['nick'] = sel.xpath("")

        nick = sel.xpath("//div[@class='main']/strong/text()").extract()[0]
        print "nick", nick
        local = sel.xpath("//p[@class='local']/text()").extract()[0]
        print "local", local
        for sel in response.xpath("//ol[@class='hoby']"):
            lis = sel.xpath("li/text()").extract()
            for li in lis:
                print li
            # print "li", li
        for sel in response.xpath("//ul[@class='block_photo']"):
            lis = sel.xpath("li/@data_url_full").extract()
            for li in lis:

                # url = r"http://www.udooo.com/cooperate/qq/images/081128/left.swf"  
                # path = r"c:/spider/left2.swf"  
                # data = urllib.urlretrieve(url, a.) 
                filename = li[-20:].split('.')[0]
                print "filename", filename
                img_format = li[-8:].split('.')[-1]
                print "img_format", img_format
                path = "%s.%s" % (filename, img_format)
                urllib.urlretrieve(li, path) 
                # print last_str
                print li, type(li)
            # print "lis", lis
        intro = sel.xpath("//ul[@class='requre']/li/p/text()").extract()[0].encode('utf-8')
        print "intro", intro

        # print "message", response.xpath("//div[@class='message']/ol/li")

        for sel in response.xpath("//div[@class='message']/ol/li/span"):
            nick = sel.xpath("text()").extract()[0].encode('utf-8')
            print "nick", nick

        data_handle = DataHandle()

class DataHandle():

    def __init__(self):
        self.mysql_engine = create_engine('mysql://jiaoyou:jiaoyou11_@laoshurds.mysql.rds.aliyuncs.com/jiaoyou')
        self.mysql_engine.connect()

        print "conn", self.mysql_engine


        


        
