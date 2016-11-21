# -*- coding: utf-8 -*-

import scrapy


class AirbnbListingItem(scrapy.Item):
    listing_id = scrapy.Field()
    name = scrapy.Field()
    host_id = scrapy.Field()
    star_rating = scrapy.Field()
    visible_review_count = scrapy.Field()
    summary = scrapy.Field()
    is_business_travel_ready = scrapy.Field()
    instant_bookable = scrapy.Field()
    city = scrapy.Field()

    # space interface
    accomodates = scrapy.Field()
    bathrooms = scrapy.Field()
    bedrooms = scrapy.Field()
    beds = scrapy.Field()
    checkin = scrapy.Field()
    checkout = scrapy.Field()
    property_type = scrapy.Field()
    room_type = scrapy.Field()
    bed_type = scrapy.Field()
    pet_owner = scrapy.Field()

    #price interface
    cancellation_policy = scrapy.Field()
    cleaning_fee = scrapy.Field()
    extra_people = scrapy.Field()
    monthly_discount = scrapy.Field()
    monthly_price = scrapy.Field()
    permit = scrapy.Field()
    security_deposit = scrapy.Field()
    weekly_discount = scrapy.Field()
    weekly_price = scrapy.Field()
    weekend_price = scrapy.Field()

    description = scrapy.Field()
    house_rules = scrapy.Field()
    building_rules = scrapy.Field()
    min_nights = scrapy.Field()

    # guest control
    allows_children = scrapy.Field()
    allows_infants = scrapy.Field()
    allows_pets = scrapy.Field()
    allows_smoking = scrapy.Field()
    allows_events = scrapy.Field()

    # TODO: Amenities

    # TODO: Reviews

    # TODO: Host

    # TODO: Photos

    # From room_options
    price = scrapy.Field()
    saved_to_wishlist_count = scrapy.Field()
    response_rate_shown = scrapy.Field()
    response_time_shown = scrapy.Field()
    guest_satisfaction_overall = scrapy.Field()
    accuracy_rating = scrapy.Field()
    cleanliness_rating = scrapy.Field()
    checkin_rating = scrapy.Field()
    communication_rating = scrapy.Field()
    location_rating = scrapy.Field()
    value_rating = scrapy.Field()
    picture_count = scrapy.Field()
    lat = scrapy.Field()
    lng = scrapy.Field()
    url = scrapy.Field()
