CREATE DATABASE  IF NOT EXISTS 'cs454' /*!40100 DEFAULT CHARACTER SET latin1 */;
USE 'cs454';
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
-- Table structure for table `base_vehicles`
--

DROP TABLE IF EXISTS `base_vehicles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `base_vehicles` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `description` text,
  `weight` double NOT NULL DEFAULT '0',
  `armor` double NOT NULL DEFAULT '0',
  `control` double NOT NULL DEFAULT '0',
  `speed` double NOT NULL DEFAULT '0',
  `health` double NOT NULL DEFAULT '0',
  `acceleration` double NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `dd_game_rankings`
--

DROP TABLE IF EXISTS `dd_game_rankings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dd_game_rankings` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `game_id` int(11) NOT NULL,
  `player_id` int(11) NOT NULL,
  `ranking` int(2) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `game_id_idx` (`game_id`),
  KEY `player_id_idx` (`player_id`),
  CONSTRAINT `dd_game_ranking_game_id` FOREIGN KEY (`game_id`) REFERENCES `games` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `dd_game_ranking_player_id` FOREIGN KEY (`player_id`) REFERENCES `players` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `friend_relationships`
--

DROP TABLE IF EXISTS `friend_relationships`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `friend_relationships` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `player_id` int(11) NOT NULL,
  `friend_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `friend_relationship_player_id` (`player_id`),
  KEY `friend_relationship_friend_id` (`friend_id`),
  CONSTRAINT `friend_relationship_friend_id` FOREIGN KEY (`friend_id`) REFERENCES `players` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `friend_relationship_player_id` FOREIGN KEY (`player_id`) REFERENCES `players` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `games`
--

DROP TABLE IF EXISTS `games`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `games` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type` int(11) NOT NULL DEFAULT '0' COMMENT 'The type of game that is being player (ex. 1 = dd | 2 = rr)\n',
  `time_started` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `map_name` varchar(255) NOT NULL,
  `room_name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `player_powerups`
--

DROP TABLE IF EXISTS `player_powerups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `player_powerups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `powerup_id` int(11) NOT NULL,
  `player_id` int(11) NOT NULL,
  `quantity` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `player_powerups_type_id_idx` (`powerup_id`),
  KEY `player_powerups_player_idx` (`player_id`),
  CONSTRAINT `player_powerups_id` FOREIGN KEY (`powerup_id`) REFERENCES `powerups` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `player_powerups_player` FOREIGN KEY (`player_id`) REFERENCES `players` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `player_vehicles`
--

DROP TABLE IF EXISTS `player_vehicles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `player_vehicles` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `base_id` int(11) NOT NULL,
  `player_id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `color_r` int(11) DEFAULT NULL,
  `color_g` int(11) DEFAULT NULL,
  `color_b` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `player_vehicle_id` (`base_id`),
  KEY `player_vehicle_player` (`player_id`),
  CONSTRAINT `player_vehicle_id` FOREIGN KEY (`base_id`) REFERENCES `base_vehicles` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `player_vehicle_player` FOREIGN KEY (`player_id`) REFERENCES `players` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `players`
--

DROP TABLE IF EXISTS `players`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `players` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(255) NOT NULL,
  `user_password` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  UNIQUE KEY `user_name_UNIQUE` (`user_name`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `powerups`
--

DROP TABLE IF EXISTS `powerups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `powerups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `description` text,
  `duration` double NOT NULL,
  `damage` double NOT NULL DEFAULT '0',
  `armor` double NOT NULL DEFAULT '0',
  `health` double NOT NULL DEFAULT '0',
  `acceleration` double NOT NULL DEFAULT '0',
  `can_make_immune` tinyint(1) NOT NULL DEFAULT '0',
  `can_blind` tinyint(1) NOT NULL DEFAULT '0',
  `can_toggle` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `rr_game_rankings`
--

DROP TABLE IF EXISTS `rr_game_rankings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rr_game_rankings` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `game_id` int(11) NOT NULL,
  `player_id` int(11) NOT NULL,
  `ranking` int(2) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `game_id_idx` (`game_id`),
  KEY `player_id_idx` (`player_id`),
  CONSTRAINT `rr_game_rankings_id` FOREIGN KEY (`game_id`) REFERENCES `games` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `rr_game_rankings_player` FOREIGN KEY (`player_id`) REFERENCES `players` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `upgrades`
--

DROP TABLE IF EXISTS `upgrades`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `upgrades` (
  `id` int(11) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `description` text,
  `armor` double NOT NULL DEFAULT '0',
  `health` double NOT NULL DEFAULT '0',
  `acceleration` double NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `vehicle_upgrade_relationships`
--

DROP TABLE IF EXISTS `vehicle_upgrade_relationships`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vehicle_upgrade_relationships` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `player_vehicle_id` int(11) NOT NULL,
  `upgrade_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `vp_relationship_idx` (`player_vehicle_id`),
  KEY `vp_relationship_powerup_idx` (`upgrade_id`),
  CONSTRAINT `vu_upgrade` FOREIGN KEY (`upgrade_id`) REFERENCES `upgrades` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `vu_vehicle` FOREIGN KEY (`player_vehicle_id`) REFERENCES `player_vehicles` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-11-18 19:53:44
