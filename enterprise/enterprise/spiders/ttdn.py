# -*- coding: utf-8 -*-
import scrapy


class TtdnSpider(scrapy.Spider):
    name = "ttdn"
    allowed_domains = ["thongtindoanhnghiep.co"]
    start_urls = ['http://thongtindoanhnghiep.co/']

    def parse(self, response):
        pass
