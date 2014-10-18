# -*- coding: utf-8 -*-

import sys

import urllib 
from scrapy.spider import Spider
from scrapy.selector import Selector

from jimome.items import JimomeItem
import const
from sqlalchemy import *
from sqlalchemy.databases import mysql

class JimomeSpider(Spider):

    reload(sys)
    sys.setdefaultencoding('utf-8')

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

        item = JimomeItem()

        # 获取头像路径
        item['icon'] = sel.xpath("//dl[@class='personal_cen']/dt/img/@src").extract()[0]
        print "icon", item['icon']

        # 获取昵称
        item['nick'] = sel.xpath("//div[@class='main']/strong/text()").extract()[0]
        print "nick", item['nick']

        # 获取所在地、年龄、身高、薪水、是否有房文本内容
        local = sel.xpath("//p[@class='local']/text()").extract()[0]
        # print "local", local
        # 以空字符为分隔符拆分文本到列表中
        local = local.split(' ')
        # 过滤列表中空字符文本，并将所在地、年龄、身高、薪水、是否有房信息存放到tmp1中
        tmp1 = []
        for i in local:
            if i:
                tmp1.append(i)

        # 获取所在地编号
        place = tmp1[0]
        if len(place) == 4:
            item['province'] = const.PROVINCE.get(place[0:2], '1')
            item['city'] = const.CITY.get(place[2:5], '1')
        elif len(place) > 4:
            for i in xrange(2, len(place)+1):
                if not const.PROVINCE.get(place[0:i], None):
                    continue
                item['province'] = const.PROVINCE.get(place[0:i], '1')
                item['city'] = const.CITY.get(place[i:len(place)+1], '1')

        print "province", item['province']
        print "city", item['city']

        # 获取年龄编号
        age = tmp1[1]
        # print "age", const.AGE[age]
        item['age'] = const.AGE.get(age, '1')
        print "age", item['age']

        # 获取身高编号
        height = tmp1[2]
        # print "height", const.HEIGHT[height]
        item['height'] = const.HEIGHT.get(height, '1')
        print "height", item['height']

        # 获取薪水编号
        salary = tmp1[3]
        # print "salary", const.SALARY[salary]
        item['salary'] = const.SALARY.get(salary, '1')
        print "salary", item['salary']

        # 获取是否有房编号
        has_house = tmp1[4]
        # print "has_house", const.HAS_HOUSE[has_house]
        item['has_house'] = const.HAS_HOUSE.get(has_house, '1')
        print "has_house", item['has_house']

        # 获取兴趣、个性编号
        hobbies = ''
        pesonalitys = ''
        for sel in response.xpath("//ol[@class='hoby']"):
            lis = sel.xpath("li/text()").extract()
            
            for li in lis:
                tmp = const.FLAGS[li.strip()]
                print "tmp", tmp
                if tmp[0] == '1':
                    hobbies += '%s,' % tmp[1]
                    # print "hobbies", hobbies
                elif tmp[0] == '2':
                    pesonalitys += '%s,' % tmp[1]
                    # print "pesonalitys", pesonalitys

        # print "hobbies", hobbies
        item['hobbies'] = hobbies
        print "hobbies", item['hobbies']
        # print "pesonalitys", pesonalitys
        item['pesonalitys'] = pesonalitys
        print "pesonalitys", item['pesonalitys']

        # 获取照片路径
        photos = []
        for sel in response.xpath("//ul[@class='block_photo']"):
            url = sel.xpath("li/@data_url_full").extract()[-20:]
            photos.append(url)
        item['photos'] = photos
        print "photos", item['photos']

        # filename = img[0]
        # format = img[2]
        # path = "%s.%s" % (filename, img_format)
        # urllib.urlretrieve(li, path) 

        intro = sel.xpath("//ul[@class='requre']/li/p/text()").extract()[0].encode('utf-8')
        item['intro'] = intro.strip()
        print "intro", item['intro']

        sels = response.xpath("//div[@class='message']/ol/li")

        # 获取体重编号
        weight = sels[1].xpath("span/text()").extract()[0]
        item['weight'] = const.WEIGHT.get(weight, '21')
        print "weight", item['weight']

        

        for sel in response.xpath("//div[@class='message']/ol/li/span"):
            nick = sel.xpath("text()").extract()[0].encode('utf-8')
            print "nick", nick

        data_handle = DataHandle()

class DataHandle():

    def __init__(self):
        self.mysql_engine = create_engine('mysql://jiaoyou:jiaoyou11_@laoshurds.mysql.rds.aliyuncs.com/jiaoyou')
        self.mysql_engine.connect()

        print "conn", self.mysql_engine


        


        
