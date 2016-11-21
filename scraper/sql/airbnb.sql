CREATE TABLE `amenities` (
  `id` int(11) NOT NULL,
  `name` varchar(256) DEFAULT NULL,
  `tag` varchar(64) DEFAULT NULL,
  `is_business_ready_feature` tinyint(4) DEFAULT NULL,
  `is_safety_feature` tinyint(4) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `amenities` VALUES (1,'TV','tv','',0,0);
INSERT INTO `amenities` VALUES (2,'Cable TV','cable','',0,0);
INSERT INTO `amenities` VALUES (3,'Internet','internet','',0,0);
INSERT INTO `amenities` VALUES (4,'Wireless Internet','wireless_internet','Continuous access in the listing',0,0);
INSERT INTO `amenities` VALUES (5,'Air conditioning','ac','',0,0);
INSERT INTO `amenities` VALUES (6,'Wheelchair accessible','wheelchair_accessible','Easy access to the building and listing for guests in wheelchairs',0,0);
INSERT INTO `amenities` VALUES (7,'Pool','pool','Private or Shared',0,0);
INSERT INTO `amenities` VALUES (8,'Kitchen','kitchen','Space where guests can cook their own meals',0,0);
INSERT INTO `amenities` VALUES (9,'Free parking on premises','free_parking','',0,0);
INSERT INTO `amenities` VALUES (10,'Paid parking off premises','paid_parking','',0,0);
INSERT INTO `amenities` VALUES (11,'Smoking allowed','allows_smoking','',0,0);
INSERT INTO `amenities` VALUES (12,'Pets allowed','allows_pets','',0,0);
INSERT INTO `amenities` VALUES (14,'Doorman','doorman','',0,0);
INSERT INTO `amenities` VALUES (15,'Gym','gym','Free, in the building or nearby',0,0);
INSERT INTO `amenities` VALUES (16,'Breakfast','breakfast','Breakfast is provided.',0,0);
INSERT INTO `amenities` VALUES (21,'Elevator in building','elevator','',0,0);
INSERT INTO `amenities` VALUES (23,'Free parking on street','street_parking','',0,0);
INSERT INTO `amenities` VALUES (25,'Hot tub','jacuzzi','',0,0);
INSERT INTO `amenities` VALUES (27,'Indoor fireplace','fireplace','',0,0);
INSERT INTO `amenities` VALUES (28,'Buzzer/wireless intercom','buzzer','',0,0);
INSERT INTO `amenities` VALUES (30,'Heating','heating','Central heating or a heater in the listing',0,0);
INSERT INTO `amenities` VALUES (31,'Family/kid friendly','family_friendly','',0,0);
INSERT INTO `amenities` VALUES (32,'Suitable for events','event_friendly','The listing can accommodate a gathering of 25 or more attendees',0,0);
INSERT INTO `amenities` VALUES (33,'Washer','washer','In the building, free or for a fee',0,0);
INSERT INTO `amenities` VALUES (34,'Dryer','dryer','In the building, free or for a fee',0,0);
INSERT INTO `amenities` VALUES (35,'Smoke detector','smoke_detector','',0,1);
INSERT INTO `amenities` VALUES (36,'Carbon monoxide detector','carbon_monoxide_detector','',0,1);
INSERT INTO `amenities` VALUES (37,'First aid kit','first_aid_kit','',0,1);
INSERT INTO `amenities` VALUES (38,'Safety card','safety_card','',0,1);
INSERT INTO `amenities` VALUES (39,'Fire extinguisher','fire_extinguisher','',0,1);
INSERT INTO `amenities` VALUES (40,'Essentials','essentials','Towels, bed sheets, soap, and toilet paper',0,0);
INSERT INTO `amenities` VALUES (41,'Shampoo','shampoo','',0,0);
INSERT INTO `amenities` VALUES (44,'Hangers','hangers','',1,0);
INSERT INTO `amenities` VALUES (45,'Hair dryer','hair-dryer','',1,0);
INSERT INTO `amenities` VALUES (46,'Iron','iron','',1,0);
INSERT INTO `amenities` VALUES (47,'Laptop friendly workspace','laptop-friendly','A table or desk with space for a laptop and a chair that’s comfortable to work in',1,0);
INSERT INTO `amenities` VALUES (51,'Self Check-In','self_checkin','',0,0);

CREATE TABLE `listing` (
  `id` bigint(20) NOT NULL,
  `name` varchar(256) DEFAULT NULL,
  `host_id` bigint(20) DEFAULT NULL,
  `star_rating` tinyint(4) DEFAULT NULL,
  `visible_review_count` int(11) DEFAULT NULL,
  `summary` varchar(2048) DEFAULT '',
  `is_business_travel_ready` tinyint(4) DEFAULT NULL,
  `instant_bookable` tinyint(4) DEFAULT NULL,
  `city` varchar(32) DEFAULT NULL,
  `accomodates` varchar(16) DEFAULT NULL,
  `bathrooms` varchar(16) DEFAULT NULL,
  `bedrooms` varchar(16) DEFAULT NULL,
  `beds` varchar(16) DEFAULT NULL,
  `checkin` varchar(64) DEFAULT NULL,
  `checkout` varchar(32) DEFAULT NULL,
  `property_type` varchar(32) DEFAULT NULL,
  `room_type` varchar(32) DEFAULT NULL,
  `bed_type` varchar(32) DEFAULT NULL,
  `pet_owner` varchar(32) DEFAULT NULL,
  `cancellation_policy` varchar(32) DEFAULT NULL,
  `cleaning_fee` int(11) DEFAULT NULL,
  `extra_people` varchar(64) DEFAULT NULL,
  `monthly_discount` int(11) DEFAULT NULL,
  `monthly_price` int(11) DEFAULT NULL,
  `permit` varchar(32) DEFAULT NULL,
  `security_deposit` int(11) DEFAULT NULL,
  `weekly_discount` int(11) DEFAULT NULL,
  `weekly_price` int(11) DEFAULT NULL,
  `weekend_price` int(11) DEFAULT NULL,
  `description` text,
  `house_rules` text,
  `building_rules` text,
  `min_nights` tinyint(4) DEFAULT NULL,
  `allows_children` tinyint(4) DEFAULT NULL,
  `allows_infants` tinyint(4) DEFAULT NULL,
  `allows_pets` tinyint(4) DEFAULT NULL,
  `allows_smoking` tinyint(4) DEFAULT NULL,
  `allows_events` tinyint(4) DEFAULT NULL,
  `price_usd` int(11) DEFAULT NULL,
  `saved_to_wishlist_count` int(11) DEFAULT NULL,
  `response_rate_shown` tinyint(4) DEFAULT NULL,
  `response_time_shown` int(11) DEFAULT NULL,
  `guest_satisfaction_overall` tinyint(4) DEFAULT NULL,
  `accuracy_rating` tinyint(4) DEFAULT NULL,
  `cleanliness_rating` tinyint(4) DEFAULT NULL,
  `checkin_rating` tinyint(4) DEFAULT NULL,
  `communication_rating` tinyint(4) DEFAULT NULL,
  `location_rating` tinyint(4) DEFAULT NULL,
  `value_rating` tinyint(4) DEFAULT NULL,
  `picture_count` int(4) DEFAULT NULL,
  `lat` double DEFAULT NULL,
  `lng` double DEFAULT NULL,
  `url` varchar(2048) DEFAULT NULL,
  `create_time` bigint(20) DEFAULT NULL,
  `update_time` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
