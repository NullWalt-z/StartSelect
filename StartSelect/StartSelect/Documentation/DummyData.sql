LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `location` VALUES 	(1,'walter', 'lozier','WLozi',0,0),
								(2,'kc','manager','KMana',1,1),
                                (3,'kc' , 'gametech','KGame',2,1),
                                (4,'dm','manager','DMana',1,2),
                                (5,'dm' , 'gametech','DGame',2,2),
                                (6,'mn','manager','MMana',1,3),
                                (7,'mn' , 'gametech','MGame',2,3);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

LOCK TABLES `location` WRITE;
/*!40000 ALTER TABLE `location` DISABLE KEYS */;
INSERT INTO `location` VALUES 	(1,'Kansas City', '101 SW Boulevard, Kansas City, MO 64111'),
								(2,'Des Moines','500 E Locust St, Des Moines, IA 50309'),
                                (3,'Minneapolis' , '3012 Lyndale Ave S, Minneapolis, MN 55408');
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
                                (8,'Surly','MN')
                                (9,'Modist','MN');
/*!40000 ALTER TABLE `brewery` ENABLE KEYS */;
UNLOCK TABLES;


LOCK TABLES `beer` WRITE;
/*!40000 ALTER TABLE `beer` DISABLE KEYS */;
INSERT INTO `beer` VALUES 	('1234567887654321','2018-01-01 00:00:00',100.20,1),
							('1111222233334444','2017-08-20 00:00:00', 238.92,4),
                            ('2222333344445555','2017-08-20 11:00:00', 16.34, 3),
                            ('8765432112345678','2018-01-01 00:00:00',100.20,1),
                            ('3111345029309203','2017-08-20 10:00:00', 250.00, 2)
                            (),
                            (),
                            (),
                            (),;
/*!40000 ALTER TABLE `beer` ENABLE KEYS */;
UNLOCK TABLES;

DROP TABLE IF EXISTS `Store`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Store` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `Name` varchar(80) DEFAULT NULL,
  `Location` varchar(80) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;


LOCK TABLES `Store` WRITE;
/*!40000 ALTER TABLE `Store` DISABLE KEYS */;
INSERT INTO `Store` VALUES (1,'The Bunker', 'Kansas City, MO'),(2,'Normal Human', 'Kansas City, MO'),(3,'Raygun','New York, New York'),(4, 'No Other Pub', 'Kansas City, MO'),(5, 'McFaddens', 'New York, New York'),(6,'UMKC Career Fair', 'Kansas City, MO');
/*!40000 ALTER TABLE `Store` ENABLE KEYS */;
UNLOCK TABLES;

DROP TABLE IF EXISTS `Rule`;
/*!40101 SET @saved_cs_client     =@@character_set_client */;
CREATE TABLE `Rule` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ownerID` int (11) DEFAULT NULL,
  `name` varchar(20) DEFAULT NULL,
  `heuristics` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`)
  )
  ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
  /*40101 SET character_set_client = @saved_cs_client */


LOCK TABLES `Rule` WRITE;
/*!40000 ALTER TABLE `Rule` DISABLE KEYS */;
INSERT INTO `Rule` VALUES (1,1,'Out Of Town', 'Amount,100,3'),(2,1,'Day Off', 'Day,Tue'),(2,1,'100 On Weekends', 'Amount,100,1;&&;(Day,Sat;or;Day,Sun)');
/*!40000 ALTER TABLE `Rule` ENABLE KEYS */;
UNLOCK TABLES;

