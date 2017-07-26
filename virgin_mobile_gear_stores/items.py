# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class StoreInfo(scrapy.Item):
    store_name = scrapy.Field()
    address = scrapy.Field()
    city = scrapy.Field()
    state = scrapy.Field()
    phone = scrapy.Field()
    product_phone = scrapy.Field()
    product_topup_card = scrapy.Field()
    product_broadband2go = scrapy.Field()

