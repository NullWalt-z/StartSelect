#CREATE database leftright;
LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES 		(1,'walter','lozier','WLozi','password',0,0),
								(2,'kc','manager','KMana','password1',1,1),
                                (3,'kc','gametech','KGame','password2',2,1),
                                (4,'dm','manager','DMana','password3',1,2),
                                (5,'dm','gametech','DGame','password4',2,2),
                                (6,'mn','manager','MMana','password5',1,3),
                                (7,'mn','gametech','MGame','password6',2,3);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;


LOCK TABLES `location` WRITE;
/*!40000 ALTER TABLE `location` DISABLE KEYS */;
INSERT INTO `location` VALUES 	(1,'Kansas City','101 SW Boulevard, Kansas City, MO 64111','Kansas-City'),
								(2,'Des Moines','500 E Locust St, Des Moines, IA 50309','Des-Moines'),
                                (3,'Minneapolis','3012 Lyndale Ave S, Minneapolis, MN 55408','Minneapolis');
/*!40000 ALTER TABLE `location` ENABLE KEYS */;
UNLOCK TABLES;


LOCK TABLES `brewery` WRITE;
/*!40000 ALTER TABLE `brewery` DISABLE KEYS */;
INSERT INTO `brewery` VALUES 	(1,'Boulevard', 'MO'),
								(2,'Emperial', 'MO'),
                                (3,'Cinder Block','MO'),
								(4,'Exile','IA'),
                                (5,'Fox','IA'),
								(6,'Firetrucker','IA'),
                                (7,'Pryes','MN'),
                                (8,'Surly','MN'),
                                (9,'Modist','MN');
/*!40000 ALTER TABLE `brewery` ENABLE KEYS */;
UNLOCK TABLES;


LOCK TABLES `beer` WRITE;
/*!40000 ALTER TABLE `beer` DISABLE KEYS */;
INSERT INTO `beer` VALUES 	(1,1,'Pale Ale',1,'Pale Ale',5.50,True,5.4,30,0),
							(2,1,'Biscuit',2,'English Brown', 5.50,True,5.2,20,0),
                            (3,1,'Block IPA',3,'IPA', 6.50, False,7.2,70,0),
                            (4,2,'Beatnik Sour',4,'Berliner Weisse',7.50,True,5.4,2,0),
                            (5,2,'Fox Tail',5,'English Red', 4.50, True,5.8,17,0),
                            (6,2,'Pumper Truck',6,'Porter',5.50,False,6.7,35,0),
                            (7,3,'Miraculum',7,'IPA',5.50,True,6.4,75,0),
                            (8,3,'+1',8,'Golden Ale',5.50,False,5.1,0,0),
                            (9,3,'Supra Deluxe',9,'Lager',4.50,True,5,0,0);
/*!40000 ALTER TABLE `beer` ENABLE KEYS */;
UNLOCK TABLES;



LOCK TABLES `publisher` WRITE;
/*!40000 ALTER TABLE `publisher` DISABLE KEYS */;
INSERT INTO `publisher` VALUES 	(1,'Capcom'),
								(2,'Midway'),
                                (3,'Atari'),
                                (4, 'Williams'),
                                (5, 'Sega');
/*!40000 ALTER TABLE `publisher` ENABLE KEYS */;
UNLOCK TABLES;

LOCK TABLES `genre` WRITE;
/*!40000 ALTER TABLE `genre` DISABLE KEYS */;
INSERT INTO `genre` VALUES 		(1,'Shooter'),
								(2,'Fighter'),
                                (3,'Pinball');
/*!40000 ALTER TABLE `genre` ENABLE KEYS */;
UNLOCK TABLES;


LOCK TABLES `arcade` WRITE;
/*!40000 ALTER TABLE `arcade` DISABLE KEYS */;
INSERT INTO `arcade` VALUES (1,1,'Mortal Kombat II',2,2,1993,2,0),
							(2,1,'Maximum Force/Area 51',3,1,1997,2,0),
                            (3,1,'Medieval Madness',4,3,1997,4,0),
                            (4,2,'Marvel vs Capcom',1,2,1998,2,0),
                            (5,2,'House of the Dead',5,1,1997,2,0),
                            (6,2,'Game of Thrones',4,3,2015,4,0),
                            (7,3,'Virtua Fighter',5,2,1993,1,0),
                            (8,3,'Terminator 2: Judgement Day',2,1,1991,2,0),
                            (9,3,'Addams Family',4,3,1992,4,0);
/*!40000 ALTER TABLE `arcade` ENABLE KEYS */;
UNLOCK TABLES;


LOCK TABLES `special` WRITE;
/*!40000 ALTER TABLE `special` DISABLE KEYS */;
INSERT INTO `special` VALUES 	(1,1,'Tue',2,'Dollar off all local (MO or KS) beers'),
								(2,1,'Fri',5,'BOGO tokens'),
								(4,2,'Mon',1,'3 dollar domestic tallboys'),
								(5,2,'Thur',4,'Industry Night - 5 dollar PBJs, 6 dollar premium tequila shots'),
								(7,3,'Sun',7,'25 dollar 6 pack and a pound'),
								(8,3,'Wed',3,'4 dollar well cocktails');
/*!40000 ALTER TABLE `special` ENABLE KEYS */;
UNLOCK TABLES;

