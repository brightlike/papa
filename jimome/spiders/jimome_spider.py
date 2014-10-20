# -*- coding: utf-8 -*-

import sys
import random
import time
import datetime
import urllib 
from scrapy.spider import Spider
from scrapy.selector import Selector

from jimome.items import JimomeItem
import const

from sqlalchemy import *
from sqlalchemy.databases import mysql
from sqlalchemy.orm import sessionmaker

import oss
from oss.oss_api import *

class JimomeSpider(Spider):

    name = "jimome"

    urls = []
    for i in xrange(100):
        user_id = random.randint(200000000, 259999999)
        url = "http://www.youyuan.com/%s-profile/" % user_id
        urls.append(url)
    print "urls", urls
    start_urls = urls

    # start_urls = [
    #     "http://www.youyuan.com/221939507-profile/"
    # ]

    # def __init__(self, user_id=None, *args, **kwargs):
    #     super(JimomeSpider, self).__init__(*args, **kwargs)
    #     self.start_urls = ["http://www.youyuan.com/%s-profile/" % user_id]

    def parse(self, response):

        sel = Selector(response)

        item = JimomeItem()

        # 获取头像路径
        item['icon'] = sel.xpath("//dl[@class='personal_cen']/dt/img/@src").extract()[0]
        print "icon", item['icon']

        # 获取昵称
        nick = sel.xpath("//div[@class='main']/strong/text()").extract()[0]
        if nick == u'男士' or nick == u'女士':
            item['nick'] = ''
        else:
            item['nick'] = nick
        print "nick", item['nick']

        # 获取所在地、年龄、身高、薪水、是否有房文本内容
        local = sel.xpath("//p[@class='local']/text()").extract()[0]
        # print "local", local
        # 以空字符为分隔符拆分文本到列表中
        local = local.split(' ')
        # 过滤列表中空字符文本，并将所在地、年龄、身高、薪水、是否有房信息存放到tmp1中
        tmp = []
        for i in local:
            if i:
                tmp.append(i)

        # 获取所在地编号
        place = tmp[0]
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

        # 获取年龄
        age = tmp[1]
        last_letter = age.index('岁')
        print "last_letter", last_letter
        item['age'] = age[0:last_letter]
        print "age", item['age']

        # # 获取年龄编号
        # age = tmp[1]
        # item['age_key'] = const.AGE.get(age, '1')
        # print "age_key", item['age_key']

        # 获取身高
        height = tmp[2]
        item['height'] = height[0:3]
        print "height", item['height']

        # 获取身高编号
        height = tmp[2]
        item['height_key'] = const.HEIGHT.get(height, '1')
        print "height_key", item['height_key']

        # 获取薪水编号
        salary = tmp[3]
        item['salary'] = const.SALARY.get(salary, '1')
        print "salary", item['salary']

        # 获取是否有房编号
        has_house = tmp[4]
        item['has_house'] = const.HAS_HOUSE.get(has_house, '1')
        print "has_house", item['has_house']

        # 获取兴趣、个性编号
        hobbies = u''
        personalitys = u''
        for sel in response.xpath("//ol[@class='hoby']"):
            lis = sel.xpath("li/text()").extract()
            
            for li in lis:
                tmp = const.FLAGS[li.strip()]
                # print "tmp", tmp
                if tmp[0] == '1':
                    hobbies += '%s,' % tmp[1]
                    # print "hobbies", hobbies
                elif tmp[0] == '2':
                    personalitys += '%s,' % tmp[1]
                    # print "personalitys", personalitys

        # print "hobbies", hobbies
        item['hobbies'] = hobbies
        print "hobbies", item['hobbies']
        # print "personalitys", personalitys
        item['personalitys'] = personalitys
        print "personalitys", item['personalitys']

        # 获取照片路径
        photos = []
        for sel in response.xpath("//ul[@class='block_photo']"):
            photos = sel.xpath("li/@data_url_full").extract()[-20:]

        item['photos'] = photos
        print "photos", item['photos']

        intro = sel.xpath("//ul[@class='requre']/li/p/text()").extract()[0].encode('utf-8')
        item['intro'] = intro.strip()
        print "intro", item['intro']

        sels = response.xpath("//div[@class='message']/ol/li")

        # 获取体重编号
        weight = sels[1].xpath("span/text()").extract()[0]
        item['weight'] = const.WEIGHT.get(weight, '21')
        print "weight", item['weight']

        # 获取学历编号
        education = sels[2].xpath("span/text()").extract()[0]
        item['education'] = const.EDUCATION.get(education, '3')
        print "education", item['education']


        # 获取是否想要小孩编号
        want_kids = sels[4].xpath("span/text()").extract()[0]
        item['want_kids'] = const.WANT_KIDS.get(want_kids, '1')
        print "want_kids", item['want_kids']

        # 获取喜欢异性类型编号
        style = sels[5].xpath("span/text()").extract()[0]
        item['isomerism_style'] = const.STYLE.get(style, '0')
        print "isomerism_style", item['isomerism_style']

        # 获取是否愿意与父母同住编号
        parents = sels[6].xpath("span/text()").extract()[0]
        item['accept_with_parents'] = const.PARENTS.get(parents, '1')
        print "accept_with_parents", item['accept_with_parents']

        # 获取职业编号
        occupation = sels[9].xpath("span/text()").extract()[0]
        item['occupation'] = const.OCCUPATION.get(occupation, '0')
        print "occupation", item['occupation']

        # 能否接受异地恋编号
        remote = sels[11].xpath("span/text()").extract()[0]
        item['accept_distance'] = const.REMOTE.get(remote, '1')
        print "accept_distance", item['accept_distance']

        # 能否接受婚前性行为编号
        sex = sels[12].xpath("span/text()").extract()[0]
        item['accept_premarital_sex'] = const.REMOTE.get(sex, '2')
        print "accept_premarital_sex", item['accept_premarital_sex']

        # 魅力部位
        virtue = sels[13].xpath("span/text()").extract()[0]
        item['glamour_place'] = const.VIRTUE.get(virtue, '0')
        print "glamour_place", item['glamour_place']

        data_handle = DataHandle(item)

class DataHandle():

    import sys 
    reload(sys) 
    sys.setdefaultencoding('utf8') 

    def __init__(self, item):
        self.mysql_engine = create_engine('mysql://jiaoyou:jiaoyou11_@laoshurds.mysql.rds.aliyuncs.com/jiaoyou')
        self.mysql_engine.connect()

        Session=sessionmaker(bind=self.mysql_engine)
        session = Session()

        # 新增user
        password = make_password()
        install_date = datetime.date.today()
        install_time = int(time.time())

        sql = """
            insert into user (password, install_date, install_time)
            values ('%s', '%s', %d) 
        """ % (password, install_date, install_time)

        session.execute(sql)

        # 返回新增user的id
        sql = """
            select id from user where install_time = %d
        """ % install_time

        cursor = session.execute(sql)
        user_obj = cursor.fetchall()
        for obj in user_obj:
            user_id = obj[0]
            print "user_id", user_id

        print "user_id", type(user_id)

        # 初始化用户账户
        sql = """
            insert into user_account (user_id, star_sets, user_type)
            values (%d, '%s', '%s')
        """ % (user_id, '0,0,0,0', '-1,-1,-1')

        session.execute(sql)

        # 下载用户头像
        icon = ''
        if item['icon'] != '/resources/skin/images/nohead_new.jpg':
            url = item['icon']
            filename = url[-26:]
            print "filename", filename
            path = '/Users/Young/workspace/scrapy/jimome/icons/%s' % filename

            urllib.urlretrieve(url, path)

            format = filename.split('.')[1]
            bucket = 'datinguser'
            log_time = str(time.time())
            log_time = log_time[0:10] + log_time[11:15]
            filename = "%s_%s.%s" % (user_id, log_time, format)

            # 上传头像到OSS
            oss = OssAPI("oss.aliyuncs.com", "CKNwNpaan7BD5sQX", "A2OxIpgSEIsxl9quDfgkKKyLK9vC2N")
            res = oss.put_object_from_file(bucket, 'avatar/'+filename, path)
            print "%s\n%s" % (res.status, res.read())
            icon = 'http://img.347.cc/avatar/%s' % filename

            # 添加到user_icon中
            url = 'http://img.347.cc/avatar/%s' % filename
            sql = """
                insert into user_icon (user_id, url, status)
                values (%d, %s, %s)
            """ % (user_id, url, '1')

        nick = ''
        if item['nick'] != u'男士' or item['nick'] != u'女士':
            nick = item['nick']
        
        intro = item['intro']

        gender = random.randint(1, 2)

        age = item['age']

        age_range = get_age_range(age)

        height = item['height']

        height_key = item['height_key']

        height_range = get_height_range(height)

        education = item['education']

        place = "%s,%s" % (item['province'], item['city'])

        occupation = item['occupation']

        salary = item['salary']

        photo_nums = len(item['photos'])

        personalitys = item['personalitys']

        hobbies = item['hobbies']

        # 初始化用户资料
        sql = """
            insert into user_profile(user_id, icon, nick, intro, gender, age, 
                age_range, height, height_key, height_range, weight, 
                weight_key, weight_range, education, place, occupation, 
                salary, photo_nums, personalitys, hobbies, love_state)
            values (%d, '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', 
                '%s', '%s', '%s', '%s', '%s', '%s', '%s', %d, '%s', '%s', '%s') 
        """ % (user_id, icon, nick, intro, gender, age, age_range, height, 
                height_key, height_range, '', '0', '0', education, place, 
                occupation, salary, photo_nums, personalitys, hobbies, '0')
        session.execute(sql)

        # 初始化用户详细
        sql = """
            insert into user_detail (user_id, has_house, glamour_place, want_kids,
                accept_distance, isomerism_style, accept_premarital_sex, accept_with_parents)
            values (%d, '%s', '%s', '%s', '%s', '%s', '%s', '%s') 
        """ % (user_id, item['has_house'], item['glamour_place'], item['want_kids'],
                item['accept_distance'], item['isomerism_style'], item['accept_premarital_sex'],
                item['accept_with_parents'])

        session.execute(sql)

        # 初始化用户征友
        sql = """
            insert into user_require (user_id, province, age_range, height_range, education, salary)
            values (%d, '%s', '%s', '%s', '%s', '%s') 
        """ % (user_id, '0', '0,0', '0,0', '0', '0')

        session.execute(sql)

        # 初始化用户设置
        sql = """
            insert into user_settings (user_id, filter_call, filter_no_icon, filter_other_province,
                filter_dismatch_age, filter_not_verified)
            values (%d, '%s', '%s', '%s', '%s', '%s')
        """ % (user_id, '0', '0', '0', '0', '0')

        session.execute(sql)

        # 下载用户照片
        urls = item['photos']
        paths = []
        if urls:
            print "urls", urls
            for url in urls:
                filename = url[-20:]
                path = '/Users/Young/workspace/scrapy/jimome/albums/%s' % filename
                print "path", path
                urllib.urlretrieve(url, path)
                paths.append(path)

            # 上传头像到OSS
            bucket = 'datinguser'
            for path in paths:
                log_time = str(time.time())
                log_time = log_time[0:10] + log_time[11:14]
                format = path.split('.')[1]
                filename = "%s_%s.%s" % (user_id, log_time, format)
                res = oss.put_object_from_file(bucket, 'album/'+filename, path)
                print "%s\n%s" % (res.status, res.read())

                # 添加到user_photo_log中
                url = 'http://img.347.cc/album/%s' % filename
                log_time = int(time.time())
                sql = """
                    insert into user_photo_log (user_id, url, status, time)
                    values (%d, '%s', '%s', %d)
                """ % (user_id, url, '1', log_time)

        session.commit()

def make_password():
    password = random.randint(100000, 999999)
    return password

def get_age_range(age):

    if not age:
        return ''
    if age == u'保密':
        return '0'
    print "get_age_range age", age
    age = int(age)

    if age < 18 or age > 65:
        return '0'

    age_dict = {}

    for i in xrange(18, 26):
        age_dict[i] = '1'
    for i in xrange(26, 36):
        age_dict[i] = '2'
    for i in xrange(36, 46):
        age_dict[i] = '3'
    for i in xrange(46, 56):
        age_dict[i] = '4'
    for i in xrange(56, 66):
        age_dict[i] = '5'

    return age_dict[age]

def get_height_range(height):

    if not height:
        return '0'
    if height == u'保密':
        return '0'

    print "get_height_range, height", height
    height = int(height)

    height_range = {}

    if height < 160:
        return '1'

    if height > 180:
        return '6'

    for i in xrange(160, 166):
        height_range[i] = '2'
    for i in xrange(166, 171):
        height_range[i] = '3'
    for i in xrange(171, 176):
        height_range[i] = '4'
    for i in xrange(176, 181):
        height_range[i] = '5'

    return height_range[height]



        
