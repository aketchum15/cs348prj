CREATE DATABASE  IF NOT EXISTS `db1` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `db1`;
-- MySQL dump 10.13  Distrib 8.0.31, for macos12 (x86_64)
--
-- Host: 35.222.185.10    Database: db1
-- ------------------------------------------------------
-- Server version	8.0.26-google

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
SET @MYSQLDUMP_TEMP_LOG_BIN = @@SESSION.SQL_LOG_BIN;
SET @@SESSION.SQL_LOG_BIN= 0;

--
-- GTID state at the beginning of the backup 
--

SET @@GLOBAL.GTID_PURGED=/*!80000 '+'*/ '44cdbc5f-53f6-11ed-b167-42010a800002:1-120145';

--
-- Table structure for table `Attendees`
--

DROP TABLE IF EXISTS `Attendees`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Attendees` (
  `attendee_id` int NOT NULL,
  `name` varchar(45) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `phone_number` int DEFAULT NULL,
  `payment_info` bigint DEFAULT NULL,
  PRIMARY KEY (`attendee_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Attendees`
--

LOCK TABLES `Attendees` WRITE;
/*!40000 ALTER TABLE `Attendees` DISABLE KEYS */;
INSERT INTO `Attendees` VALUES (201,'Neha Sunil','ns@gmail.com',346,4598010621685972),(202,'Adam Ketchum','ad@gmail.com',-278,4598011153763),(203,'Conner Claypool','cc@gmail.com',-782,4598015289100),(204,'Jasmine White','jw@gmail.com',-641,4598019458578),(205,'Rohit Sunil','rs@gmail.com',-8544,4598011019287),(206,'Samantha Corey','sc@gmail.com',-7236,4598013165839666),(207,'Kylie Phillips','kp@gmail.com',-8196,4283416333477790),(208,'Amanda Norris','an@gmail.com',-1010,4283058549446910),(209,'Luna Davidson','ld@gmail.com',-4712,4110448101101137),(210,'Jessica Stevens','js@gmail.com',-600,4283416176632);
/*!40000 ALTER TABLE `Attendees` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Owners`
--

DROP TABLE IF EXISTS `Owners`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Owners` (
  `owner_id` int NOT NULL,
  `num_owned_venues` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`owner_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Owners`
--

LOCK TABLES `Owners` WRITE;
/*!40000 ALTER TABLE `Owners` DISABLE KEYS */;
INSERT INTO `Owners` VALUES (1,'2'),(2,'1');
/*!40000 ALTER TABLE `Owners` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Performers`
--

DROP TABLE IF EXISTS `Performers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Performers` (
  `performer_id` int NOT NULL,
  `name` varchar(45) DEFAULT NULL,
  `num_crew_mems` int DEFAULT NULL,
  `ticket_price` int DEFAULT NULL,
  PRIMARY KEY (`performer_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Performers`
--

LOCK TABLES `Performers` WRITE;
/*!40000 ALTER TABLE `Performers` DISABLE KEYS */;
INSERT INTO `Performers` VALUES (1,'Taylor Swift',50,400),(2,'Harry Styles',50,300),(3,'Doja Cat',50,300),(4,'Kendrick Lamar',50,400),(5,'The Weekend',50,400),(6,'Justin Beiber',50,200),(7,'5 Seconds of Summer',50,200),(8,'Adele',50,400),(9,'Ariana Grande',50,300),(10,'Billie Eilish',50,200);
/*!40000 ALTER TABLE `Performers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Shows`
--

DROP TABLE IF EXISTS `Shows`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Shows` (
  `show_id` int NOT NULL,
  `performer_name` varchar(45) DEFAULT NULL,
  `venue_id` int DEFAULT NULL,
  `num_attendees` int DEFAULT NULL,
  `ticket_price` int DEFAULT NULL,
  PRIMARY KEY (`show_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Shows`
--

LOCK TABLES `Shows` WRITE;
/*!40000 ALTER TABLE `Shows` DISABLE KEYS */;
INSERT INTO `Shows` VALUES (10,'Taylor Swift',1,2000,400),(20,'Harry Styles',2,2000,300),(30,'Doja Cat',2,2000,300),(40,'Kendrick Lamar',1,2000,400),(50,'The Weekend',1,2000,400),(60,'Justin Beiber',3,1000,200),(70,'5 Seconds of Summer',3,1000,200),(80,'Adele',1,2000,400),(90,'Ariana Grande',1,2000,300),(100,'Billie Eilish',1,2000,200);
/*!40000 ALTER TABLE `Shows` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Tickets`
--

DROP TABLE IF EXISTS `Tickets`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Tickets` (
  `show_id` int DEFAULT NULL,
  `attendee_id` int DEFAULT NULL,
  `ticket_price` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Tickets`
--

LOCK TABLES `Tickets` WRITE;
/*!40000 ALTER TABLE `Tickets` DISABLE KEYS */;
INSERT INTO `Tickets` VALUES (10,1,400),(40,2,400),(10,1,400),(40,2,400),(10,3,400),(30,4,300),(40,5,400),(20,6,300),(70,7,200),(20,8,300),(10,9,400),(20,10,300);
/*!40000 ALTER TABLE `Tickets` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Venues`
--

DROP TABLE IF EXISTS `Venues`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Venues` (
  `venue_id` int NOT NULL,
  `owner_id` int DEFAULT NULL,
  PRIMARY KEY (`venue_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Venues`
--

LOCK TABLES `Venues` WRITE;
/*!40000 ALTER TABLE `Venues` DISABLE KEYS */;
INSERT INTO `Venues` VALUES (1,1),(2,1),(3,2);
/*!40000 ALTER TABLE `Venues` ENABLE KEYS */;
UNLOCK TABLES;
SET @@SESSION.SQL_LOG_BIN = @MYSQLDUMP_TEMP_LOG_BIN;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-10-31 18:44:06
