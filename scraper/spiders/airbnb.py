# -*- coding: utf-8 -*-
import scrapy
import json
from scraper.airbnb_listing_items import AirbnbListingItem
from urlparse import urlparse

URL_ROOT = "https://www.airbnb.com/"
URL_ROOM_ROOT = URL_ROOT + "rooms/"
URL_API_SEARCH_ROOT = 'https://api.airbnb.com/v2/search_results?client_id=3092nxybyb0otqw18e8nh5nty&locale=en-US&currency=CNY&_format=for_search_results_with_minimal_pricing&fetch_facets=true&ib=false&_limit=50'
SW_LAT = 39.442758
SW_LNG = 115.423412
NE_LAT = 41.060816
NE_LNG = 117.514625

def constuct_request_url(sw_lat, sw_lng, ne_lat, ne_lng, offset = 0):
    return URL_API_SEARCH_ROOT + '&sw_lat=' + str(sw_lat) + '&sw_lng=' + str(sw_lng) + '&ne_lat=' + str(ne_lat) + '&ne_lng=' + str(ne_lng) + '&_offset=' + str(offset)


class AirbnbSpider(scrapy.Spider):
    name = "airbnb"
    allowed_domains = ["airbnb.com"]
    start_urls = [constuct_request_url(SW_LAT, SW_LNG, NE_LAT, NE_LNG), ]

    def parse(self, response):
        # self.logger.warning(response.body)
        # sw_lat = ''
        # sw_lng = ''
        # ne_lat = ''
        # ne_lng = ''
        # offset = ''
        # limit = ''
        url = response.url
        query = urlparse(url).query
        params = query.split('&')
        for param in params:
            key = param.split('=')[0]
            value = param.split('=')[1]
            if key == 'sw_lat':
                sw_lat = float(value)
            elif key == 'sw_lng':
                sw_lng = float(value)
            elif key == 'ne_lat':
                ne_lat = float(value)
            elif key == 'ne_lng':
                ne_lng = float(value)
            elif key == '_offset':
                offset = value
            elif key == '_limit':
                limit = value
            else:
                pass

        results = json.loads(response.body)
        if 'error_code' in results:
            self.logger.error('error_code: %s', results['error_code'])
            self.logger.error('error_detail: %s', results['error_detail'])
        elif results['metadata']['listings_count'] < 1001:
            self.logger.info('Total listings =  %s', results['metadata']['listings_count'])
            for result in results['search_results']:
                yield scrapy.Request(URL_ROOM_ROOT + str(result['listing']['id']) + '?locale=en&currency=CNY', callback = self.parse_item)
            offset = results['metadata']['pagination']['next_offset']
            yield scrapy.Request(constuct_request_url(sw_lat, sw_lng, ne_lat, ne_lng, offset), callback = self.parse)
        else:
            mid_lat = (ne_lat + sw_lat) / 2.0
            mid_lng = (ne_lng + sw_lng) / 2.0
            yield scrapy.Request(constuct_request_url(sw_lat, sw_lng, mid_lat, mid_lng), callback = self.parse)
            yield scrapy.Request(constuct_request_url(sw_lat, mid_lng, mid_lat, ne_lng), callback = self.parse)
            yield scrapy.Request(constuct_request_url(mid_lat, mid_lng, ne_lat, ne_lng), callback = self.parse)
            yield scrapy.Request(constuct_request_url(mid_lat, sw_lng, ne_lat, mid_lng), callback = self.parse)

    def parse_item(self, response):
        listing = json.loads(response.xpath('//meta[@id="_bootstrap-listing"]/@content').extract_first())['listing']

        item = AirbnbListingItem()
        item['listing_id'] = listing['id']
        item['name'] = listing['name']
        item['host_id'] = listing['user']['id']
        item['star_rating'] = listing['star_rating'] if listing['star_rating'] else '0'
        item['visible_review_count'] = listing['visible_review_count'] if listing['visible_review_count'] else '0'
        item['summary'] = listing['summary']
        item['is_business_travel_ready'] = listing['is_business_travel_ready']
        item['instant_bookable'] = listing['instant_bookable']

        space_interface = listing['space_interface']
        item['accomodates'] = '0'
        item['bathrooms'] = '0'
        item['bedrooms'] = '0'
        item['beds'] = '0'
        item['checkin'] = ''
        item['checkout'] = ''
        item['property_type'] = ''
        item['room_type'] = ''
        item['bed_type'] = ''
        item['pet_owner'] = ''
        for space_attr in space_interface:
            if space_attr['label'] == 'Accommodates:':
                item['accomodates'] = space_attr['value']
            elif space_attr['label'] == 'Bathrooms:':
                item['bathrooms'] = space_attr['value']
            elif space_attr['label'] == 'Bedrooms:':
                item['bedrooms'] = space_attr['value']
            elif space_attr['label'] == 'Beds:':
                item['beds'] = space_attr['value']
            elif space_attr['label'] == 'Check In:':
                item['checkin'] = space_attr['value']
            elif space_attr['label'] == 'Check Out:':
                item['checkout'] = space_attr['value']
            elif space_attr['label'] == 'Property type:':
                item['property_type'] = space_attr['value']
            elif space_attr['label'] == 'Room type:':
                item['room_type'] = space_attr['value']
            elif space_attr['label'] == 'Bed type:':
                item['bed_type'] = space_attr['value']
            elif space_attr['label'] == 'Pet Owner:':
                item['pet_owner'] = space_attr['value']
            else:
                self.logger.warning('Missing space interface attribute: %s', space_attr['label'])

        price_interface = listing['price_interface']
        item['cancellation_policy'] = price_interface['cancellation_policy']['value'] if price_interface['cancellation_policy'] else ''
        item['cleaning_fee'] = price_interface['cleaning_fee']['value'][1:] if price_interface['cleaning_fee'] else ''
        item['extra_people'] = price_interface['extra_people']['value'] if price_interface['extra_people'] else ''
        item['monthly_discount'] = price_interface['monthly_discount']['value'][:-1] if price_interface['monthly_discount'] else ''
        # item['monthly_price'] = price_interface['monthly_price']['value'] if price_interface['monthly_price'] else ''
        if price_interface['monthly_price']:
            monthly_price = price_interface['monthly_price']['value']
            item['monthly_price'] = monthly_price[1:monthly_price.index(' ')]
        else:
            item['monthly_price'] = '0'
        item['permit'] = price_interface['permit']['value'] if price_interface['permit'] else ''
        item['security_deposit'] = price_interface['security_deposit']['value'][1:] if price_interface['security_deposit'] else ''
        item['weekly_discount'] = price_interface['weekly_discount']['value'][:-1] if price_interface['weekly_discount'] else ''
        # item['weekly_price'] = price_interface['weekly_price']['value'] if price_interface['weekly_price'] else ''
        if price_interface['weekly_price']:
            weekly_price = price_interface['weekly_price']['value']
            item['weekly_price'] = monthly_price[1:weekly_price.index(' ')]
        else:
            item['weekly_price'] = '0'
        # item['weekend_price'] = price_interface['weekend_price']['value'] if price_interface['weekend_price'] else ''
        if price_interface['weekend_price']:
            weekend_price = price_interface['weekend_price']['value']
            item['weekend_price'] = weekend_price[1:weekend_price.index(' ')]
        else:
            item['weekend_price'] = '0'

        item['description'] = listing['description']
        item['house_rules'] = listing['house_rules']
        item['building_rules'] = listing['building_rules']
        item['min_nights'] = listing['min_nights']

        guest_controls = listing['guest_controls']
        item['allows_children'] = guest_controls['allows_children']
        item['allows_infants'] = guest_controls['allows_infants']
        item['allows_pets'] = guest_controls['allows_pets']
        item['allows_smoking'] = guest_controls['allows_smoking']
        item['allows_events'] = guest_controls['allows_events']

        room_options = json.loads(response.xpath('//meta[@id="_bootstrap-room_options"]/@content').extract_first())['airEventData']

        item['price'] = room_options['price']
        item['saved_to_wishlist_count'] = room_options['saved_to_wishlist_count']
        item['response_rate_shown'] = room_options['response_rate_shown'] if room_options['response_rate_shown'] else '0'
        item['response_time_shown'] = room_options['response_time_shown'] if room_options['response_time_shown'] else '0'
        item['guest_satisfaction_overall'] = room_options['guest_satisfaction_overall'] if room_options['guest_satisfaction_overall'] else '0'
        item['accuracy_rating'] = room_options['accuracy_rating'] if room_options['accuracy_rating'] else '0'
        item['cleanliness_rating'] = room_options['cleanliness_rating'] if room_options['cleanliness_rating'] else '0'
        item['checkin_rating'] = room_options['checkin_rating'] if room_options['checkin_rating'] else '0'
        item['communication_rating'] = room_options['communication_rating'] if room_options['communication_rating'] else '0'
        item['location_rating'] = room_options['location_rating'] if room_options['location_rating'] else '0'
        item['value_rating'] = room_options['value_rating'] if room_options['value_rating'] else '0'
        item['picture_count'] = room_options['picture_count']
        item['lat'] = room_options['listing_lat']
        item['lng'] = room_options['listing_lng']
        item['url'] = response.url

        yield item



# https://www.airbnb.com/api/v2/calendar_months?key=d306zoyjsyarp7ifhu67rjxn52tv0t20&currency=CNY&locale=en&listing_id=13453979&month=11&year=2016&count=1&_format=with_conditions
