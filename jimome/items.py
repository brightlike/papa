# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class JimomeItem(scrapy.Item):
    # define the fields for your item here like:

    icon = scrapy.Field()
    nick = scrapy.Field()

    province = scrapy.Field()
    city = scrapy.Field()
    age = scrapy.Field()
    height = scrapy.Field()
    salary = scrapy.Field()
    has_house = scrapy.Field()

    hobbies = scrapy.Field()
    pesonalitys = scrapy.Field()

    photos = scrapy.Field()
    intro = scrapy.Field()

    weight = scrapy.Field()
    education = scrapy.Field()
    occupation = scrapy.Field()

    want_kids = scrapy.Field()
    accept_distance = scrapy.Field()
    isomerism_style = scrapy.Field()
    accept_premarital_sex = scrapy.Field()
    accept_with_parents = scrapy.Field()
    glamour_place = scrapy.Field()

    

    
