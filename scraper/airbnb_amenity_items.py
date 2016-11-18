# -*- coding: utf-8 -*-

import scrapy


class AirbnbAmenityItem(scrapy.Item):
    amenity_id = scrapy.Field()
    is_business_ready_feature = scrapy.Field()
    is_present = scrapy.Field()
    is_safety_feature = scrapy.Field()
    name = scrapy.Field()
    tag = scrapy.Field()
