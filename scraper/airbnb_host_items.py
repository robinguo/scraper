# -*- coding: utf-8 -*-

import scrapy


class AirbnbHostItem(scrapy.Item):
    host_id = scrapy.Field()
    host_name = scrapy.Field()
    is_super_host = scrapy.Field()
