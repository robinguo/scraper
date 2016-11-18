# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from datetime import datetime
from twisted.enterprise import adbapi
from scraper.airbnb_listing_items import AirbnbListingItem
import time

class AirbnbListingPipeline(object):
    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        dbargs = dict(
            host = settings['MYSQL_HOST'],
            db = settings['MYSQL_DB'],
            user = settings['MYSQL_USER'],
            passwd = settings['MYSQL_PASSWD'],
            charset = 'utf8',
            use_unicode = True,
        )
        dbpool = adbapi.ConnectionPool('MySQLdb', **dbargs)
        return cls(dbpool)

    def process_item(self, item, spider):
        if isinstance(item, AirbnbListingItem):
            for key,value in item.items():
                if type(value) is list or type(value) is dict:
                    spider.logger.warning('%s not parsed correctly: %s', key, value)
            d = self.dbpool.runInteraction(self._do_upsert, item, spider)
            d.addErrback(self._handle_error, item, spider)
            # at the end return the item in case of success or failure
            d.addBoth(lambda _: item)
            return d
        return item

    def _do_upsert(self, conn, item, spider):
        conn.execute('SELECT EXISTS (SELECT 1 FROM listing WHERE id = %s)', (item['listing_id'],))
        ret = conn.fetchone()[0]

        if ret:
            conn.execute('''
                UPDATE lisiting SET name = %s, host_id = %s, star_rating = %s,
                visible_review_count =%s, summary = %s, is_business_travel_ready = %s,
                instant_bookable = %s, accomodates = %s, bathrooms = %s, bedrooms = %s,
                beds = %s , checkin = %s, checkout = %s, property_type = %s,
                room_type = %s, bed_type = %s, pet_owner = %s, cancellation_policy = %s,
                cleaning_fee = %s, extra_people = %s, monthly_discount = %s,
                monthly_price = %s, permit = %s, security_deposit = %s,
                weekly_discount = %s, weekly_price = %s, weekend_price = %s,
                description = %s, house_rules = %s, min_nights = %s, allows_children = %s,
                allows_infants = %s, allows_pets = %s, allows_smoking = %s,
                allows_events = %s, price_usd = %s, saved_to_wishlist_count = %s,
                response_rate_shown = %s, response_time_shown = %s,
                guest_satisfaction_overall = %s, accuracy_rating = %s,
                cleanliness_rating = %s, checkin_rating = %s, communication_rating = %s,
                location_rating = %s, value_rating = %s, picture_count = %s, lat = %s,
                lng = %s, url = %s, update_time = %s
                WHERE id = %s
            ''', (item['name'], item['host_id'],
             item['star_rating'], item['visible_review_count'],
             item['summary'], item['is_business_travel_ready'],
             item['instant_bookable'], item['accomodates'],
             item['bathrooms'], item['bedrooms'], item['beds'],
             item['checkin'], item['checkout'],
             item['property_type'], item['room_type'], item['bed_type'],
             item['pet_owner'], item['cancellation_policy'],
             item['cleaning_fee'], item['extra_people'],
             item['monthly_discount'], item['monthly_price'],
             item['permit'], item['security_deposit'],
             item['weekly_discount'], item['weekly_price'],
             item['weekend_price'], item['description'],
             item['house_rules'],
             item['min_nights'], item['allows_children'],
             item['allows_infants'], item['allows_pets'],
             item['allows_smoking'], item['allows_events'],
             item['price'], item['saved_to_wishlist_count'],
             item['response_rate_shown'], item['response_time_shown'],
             item['guest_satisfaction_overall'], item['accuracy_rating'],
             item['cleanliness_rating'], item['checkin_rating'],
             item['communication_rating'], item['location_rating'],
             item['value_rating'], item['picture_count'], item['lat'],
             item['lng'], item['url'], int(time.time()), item['listing_id']))
            spider.logger.info('Listing updated: %s', item['listing_id'])
        else:
            conn.execute('''INSERT INTO listing (
                                    id, name, host_id, star_rating, visible_review_count,
                                    summary, is_business_travel_ready, instant_bookable,
                                    accomodates, bathrooms, bedrooms, beds, checkin,
                                    checkout, property_type, room_type, bed_type,
                                    pet_owner, cancellation_policy, cleaning_fee, extra_people,
                                    monthly_discount, monthly_price, permit, security_deposit,
                                    weekly_discount, weekly_price, weekend_price, description,
                                    house_rules, min_nights, allows_children,
                                    allows_infants, allows_pets, allows_smoking, allows_events,
                                    price_usd, saved_to_wishlist_count, response_rate_shown,
                                    response_time_shown, guest_satisfaction_overall,
                                    accuracy_rating, cleanliness_rating, checkin_rating,
                                    communication_rating, location_rating, value_rating,
                                    picture_count, lat, lng, url, create_time, update_time)
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                                    %s, %s, %s, %s, %s, %s, %s, %s, %s)''',
                            (item['listing_id'], item['name'], item['host_id'],
                             item['star_rating'], item['visible_review_count'],
                             item['summary'], item['is_business_travel_ready'],
                             item['instant_bookable'], item['accomodates'],
                             item['bathrooms'], item['bedrooms'], item['beds'],
                             item['checkin'], item['checkout'],
                             item['property_type'], item['room_type'], item['bed_type'],
                             item['pet_owner'], item['cancellation_policy'],
                             item['cleaning_fee'], item['extra_people'],
                             item['monthly_discount'], item['monthly_price'],
                             item['permit'], item['security_deposit'],
                             item['weekly_discount'], item['weekly_price'],
                             item['weekend_price'], item['description'],
                             item['house_rules'],
                             item['min_nights'], item['allows_children'],
                             item['allows_infants'], item['allows_pets'],
                             item['allows_smoking'], item['allows_events'],
                             item['price'], item['saved_to_wishlist_count'],
                             item['response_rate_shown'], item['response_time_shown'],
                             item['guest_satisfaction_overall'], item['accuracy_rating'],
                             item['cleanliness_rating'], item['checkin_rating'],
                             item['communication_rating'], item['location_rating'],
                             item['value_rating'], item['picture_count'], item['lat'],
                             item['lng'], item['url'], int(time.time()), int(time.time())))
            spider.logger.info('Listing inserted: %s', item['listing_id'])

    def _handle_error(self, failure, item, spider):
        spider.logger.error(failure)
