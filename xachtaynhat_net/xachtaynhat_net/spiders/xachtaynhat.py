# -*- coding: utf-8 -*-
import scrapy
from xachtaynhat_net.items import XachtaynhatNetItem

class XachtaynhatSpider(scrapy.Spider):
    name = "xachtaynhat"
    allowed_domains = ["xachtaynhat.net"]
    start_urls = ['https://xachtaynhat.net/']

    def parse(self, response):
	PRODUCT_SELECTOR = '.product'
	for p in response.css(PRODUCT_SELECTOR):
            link = p.xpath('./a[1]/@href').extract()
            title = p.xpath('.//strong/text()').extract()
            price = p.css('.price').xpath('.//span[1]/text()').extract()

	    item = XachtaynhatNetItem()
	    item["title"] = title
	    item["product_link"] = link
	    item["price"]=price
	    yield item
