# -*- coding: utf-8 -*-

import scrapy


class AirbnbPhotosItem(scrapy.Item):
    photo_id = scrapy.Field()
    url = scrapy.Field()
    sort_order = scrapy.Field()
    caption = scrapy.Field()
    is_professional = scrapy.Field()
    listing_id = scrapy.Field()
