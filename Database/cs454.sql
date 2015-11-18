CREATE DATABASE  IF NOT EXISTS `cs454` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `cs454`;
-- MySQL dump 10.13  Distrib 5.6.24, for Win64 (x86_64)
--
-- Host: superlunchvote.com    Database: cs454
-- ------------------------------------------------------
-- Server version	5.6.27-0ubuntu0.15.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Dumping data for table `base_vehicles`
--

LOCK TABLES `base_vehicles` WRITE;
/*!40000 ALTER TABLE `base_vehicles` DISABLE KEYS */;
/*!40000 ALTER TABLE `base_vehicles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `dd_game_rankings`
--

LOCK TABLES `dd_game_rankings` WRITE;
/*!40000 ALTER TABLE `dd_game_rankings` DISABLE KEYS */;
/*!40000 ALTER TABLE `dd_game_rankings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `friend_relationships`
--

LOCK TABLES `friend_relationships` WRITE;
/*!40000 ALTER TABLE `friend_relationships` DISABLE KEYS */;
INSERT INTO `friend_relationships` VALUES (1,3,1),(6,3,4),(7,2,1),(8,4,4),(9,1,2),(10,2,1),(11,1,3),(12,4,2),(13,7,5),(14,1,7),(15,7,2),(16,1,7),(17,8,2),(18,3,8),(19,8,6),(20,4,8),(21,9,3),(22,7,9),(23,9,4),(24,1,9),(25,10,7),(26,2,10),(27,10,1),(28,8,10),(29,11,4),(30,3,11),(31,11,6),(32,6,11),(33,12,7),(34,10,12),(35,12,10),(36,2,12);
/*!40000 ALTER TABLE `friend_relationships` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `games`
--

LOCK TABLES `games` WRITE;
/*!40000 ALTER TABLE `games` DISABLE KEYS */;
/*!40000 ALTER TABLE `games` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `player_powerups`
--

LOCK TABLES `player_powerups` WRITE;
/*!40000 ALTER TABLE `player_powerups` DISABLE KEYS */;
/*!40000 ALTER TABLE `player_powerups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `player_vehicles`
--

LOCK TABLES `player_vehicles` WRITE;
/*!40000 ALTER TABLE `player_vehicles` DISABLE KEYS */;
/*!40000 ALTER TABLE `player_vehicles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `players`
--

LOCK TABLES `players` WRITE;
/*!40000 ALTER TABLE `players` DISABLE KEYS */;
INSERT INTO `players` VALUES (1,'','password'),(2,'YdlhUWepVbLBO4SivkwNyAfDzPrx2xQCcJEt6aRIFog8ZjX9mHT71uq53MnKG0','password'),(3,'MHAT3R47qjtgakINFZuopxSvzJPf1YO2bDxcemnUG9Q5Ly0idBlW8VKhCw6rXE','password'),(4,'bwOJkT2oQNj9xFuqBDAV7zniPxS68Cd5g1yK4RhrUZGcHLp0EMvtfI3YlamXWe','password'),(5,'odUPzV2iNxebY9HGl6QTZaW3v4rDO0q7gSBj5ChwnREK8pAfkXMutcLIxmyF1J','password'),(6,'OrPjY9L3KmC5dD2tScvVeQw4HiAzI7FlE0Tkq8WZnJyoMXbaRuNxfg1xBph6GU','password'),(7,'y8ec9EYBL0uHlz3G4nJXRxZb5r2AUfmpjKTdvNIaokVhSiwPQMqDg1WFxOC7t6','password'),(8,'ZV6KDPujL8G3oA2Ux4ygRx1E9rdabl5BTCYWv7zInHwNJS0cXhifpMqkmtQeOF','password'),(9,'xC58xcJdI7akF2S6MnKlhVwQGzDPeOmq9j31gYbfE0ovtrZWNuyRH4piUALXBT','password'),(10,'tFTHjwX6pZOhuzNmESk5AReWvd1LDMir0bCx4Kqo9l8an23fxUYGQPcVy7IJBg','password'),(11,'v3aYJx24wi6trnQ7UpPDMm81zGxjyCdoVhLbSENKZHuTgIkWXq95Ac0fleFROB','password'),(12,'WblUIJSTm51tLjnMaQgV7zpwx8XrxAFE2DeG046RYiKyBC9NuoHdPhfcqOZ3vk','password');
/*!40000 ALTER TABLE `players` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `powerups`
--

LOCK TABLES `powerups` WRITE;
/*!40000 ALTER TABLE `powerups` DISABLE KEYS */;
/*!40000 ALTER TABLE `powerups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `rr_game_rankings`
--

LOCK TABLES `rr_game_rankings` WRITE;
/*!40000 ALTER TABLE `rr_game_rankings` DISABLE KEYS */;
/*!40000 ALTER TABLE `rr_game_rankings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `upgrades`
--

LOCK TABLES `upgrades` WRITE;
/*!40000 ALTER TABLE `upgrades` DISABLE KEYS */;
/*!40000 ALTER TABLE `upgrades` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `vehicle_upgrade_relationships`
--

LOCK TABLES `vehicle_upgrade_relationships` WRITE;
/*!40000 ALTER TABLE `vehicle_upgrade_relationships` DISABLE KEYS */;
/*!40000 ALTER TABLE `vehicle_upgrade_relationships` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-11-17 22:16:10
