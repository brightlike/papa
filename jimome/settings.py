# -*- coding: utf-8 -*-

# Scrapy settings for jimome project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'jimome'

SPIDER_MODULES = ['jimome.spiders']
NEWSPIDER_MODULE = 'jimome.spiders'

# ITEM_PIPELINES = {'scrapy.contrib.pipeline.images.ImagesPipeline': 1}
# IMAGES_STORE = '/path/to/valid/dir'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'jimome (+http://www.yourdomain.com)'
