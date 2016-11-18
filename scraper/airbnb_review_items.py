# -*- coding: utf-8 -*-

import scrapy


class AirbnbReviewItem(scrapy.Item):
    review_id = scrapy.Field()
    comments = scrapy.Field()
    response = scrapy.Field()
    create_month = scrapy.Field()
    create_year = scrapy.Field()
    reviewer_id = scrapy.Field()
    reviewee_id = scrapy.Field()
    listing_id = scrapy.Field()
    
