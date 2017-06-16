# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class EnterpriseItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    tax_number = scrapy.Field()
    name = scrapy.Field()
    address1 = scrapy.Field()
    address2 = scrapy.Field()
    address3 = scrapy.Field()
    city = scrapy.Field()
    start_date = scrapy.Field()
    key_sector = scrapy.Field()
    owner = scrapy.Field()
    phone = scrapy.Field()
    email = scrapy.Field()
