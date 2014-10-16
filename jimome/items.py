# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JimomeItem(scrapy.Item):
    # define the fields for your item here like:
    nick = scrapy.Field()
    place = scrapy.Field()
    age = scrapy.Field()
    height = scrapy.Field()
    salary = scrapy.Field()
    has_house = scrapy.Field()
    flags = scrapy.Field()
    icon_url = scrapy.Field()
    icon = scrapy.Field()

    photo_url = scrapy.Field()
    photo = scrapy.Field()

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

    province = scrapy.Field()
    age_range = scrapy.Field()
    height_range = scrapy.Field()
    require_education = scrapy.Field()
    require_salary = scrapy.Field()
    

    
