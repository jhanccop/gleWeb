-- MySQL dump 10.13  Distrib 8.0.30, for macos12.4 (arm64)
--
-- Host: localhost    Database: glev2
-- ------------------------------------------------------
-- Server version	8.0.30

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=85 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add well',7,'add_well'),(26,'Can change well',7,'change_well'),(27,'Can delete well',7,'delete_well'),(28,'Can view well',7,'view_well'),(29,'Can add Fluid Properties',8,'add_fluidproperties'),(30,'Can change Fluid Properties',8,'change_fluidproperties'),(31,'Can delete Fluid Properties',8,'delete_fluidproperties'),(32,'Can view Fluid Properties',8,'view_fluidproperties'),(33,'Can add completion',9,'add_completion'),(34,'Can change completion',9,'change_completion'),(35,'Can delete completion',9,'delete_completion'),(36,'Can view completion',9,'view_completion'),(37,'Can add setting',10,'add_setting'),(38,'Can change setting',10,'change_setting'),(39,'Can delete setting',10,'delete_setting'),(40,'Can view setting',10,'view_setting'),(41,'Can add Field',11,'add_field'),(42,'Can change Field',11,'change_field'),(43,'Can delete Field',11,'delete_field'),(44,'Can view Field',11,'view_field'),(45,'Can add Socker Rod Pump Data',12,'add_rodpumpdata'),(46,'Can change Socker Rod Pump Data',12,'change_rodpumpdata'),(47,'Can delete Socker Rod Pump Data',12,'delete_rodpumpdata'),(48,'Can view Socker Rod Pump Data',12,'view_rodpumpdata'),(49,'Can add ESP Event',13,'add_espevent'),(50,'Can change ESP Event',13,'change_espevent'),(51,'Can delete ESP Event',13,'delete_espevent'),(52,'Can view ESP Event',13,'view_espevent'),(53,'Can add Electric Submersible Pump Data',14,'add_espdata'),(54,'Can change Electric Submersible Pump Data',14,'change_espdata'),(55,'Can delete Electric Submersible Pump Data',14,'delete_espdata'),(56,'Can view Electric Submersible Pump Data',14,'view_espdata'),(57,'Can add Well Testing',15,'add_welltest'),(58,'Can change Well Testing',15,'change_welltest'),(59,'Can delete Well Testing',15,'delete_welltest'),(60,'Can view Well Testing',15,'view_welltest'),(61,'Can add Sample Test',16,'add_sampletest'),(62,'Can change Sample Test',16,'change_sampletest'),(63,'Can delete Sample Test',16,'delete_sampletest'),(64,'Can view Sample Test',16,'view_sampletest'),(65,'Can add Build Up Test',17,'add_builduptest'),(66,'Can change Build Up Test',17,'change_builduptest'),(67,'Can delete Build Up Test',17,'delete_builduptest'),(68,'Can view Build Up Test',17,'view_builduptest'),(69,'Can add deferment',18,'add_kpidata'),(70,'Can change deferment',18,'change_kpidata'),(71,'Can delete deferment',18,'delete_kpidata'),(72,'Can view deferment',18,'view_kpidata'),(73,'Can add failures',19,'add_failures'),(74,'Can change failures',19,'change_failures'),(75,'Can delete failures',19,'delete_failures'),(76,'Can view failures',19,'view_failures'),(77,'Can add user',20,'add_user'),(78,'Can change user',20,'change_user'),(79,'Can delete user',20,'delete_user'),(80,'Can view user',20,'view_user'),(81,'Can add company',21,'add_company'),(82,'Can change company',21,'change_company'),(83,'Can delete company',21,'delete_company'),(84,'Can view company',21,'view_company');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `company_company`
--

DROP TABLE IF EXISTS `company_company`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `company_company` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `DateCreate` datetime(6) NOT NULL,
  `CompanyName` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `LocationState` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `LocationCounty` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `CompanyName` (`CompanyName`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company_company`
--

LOCK TABLES `company_company` WRITE;
/*!40000 ALTER TABLE `company_company` DISABLE KEYS */;
INSERT INTO `company_company` VALUES (11,'2022-10-18 00:54:01.678000','Alpha Energy','New Mexico','Carlsbad'),(15,'2022-10-19 08:12:04.128936','GLE','Oklahoma','Oklahoma city');
/*!40000 ALTER TABLE `company_company` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=75 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (54,'2022-10-19 08:12:04.130276','15','GLE',1,'[{\"added\": {}}]',21,8),(55,'2022-10-19 10:02:08.807557','11','North01',1,'[{\"added\": {}}]',11,9),(56,'2022-10-19 10:03:10.234098','7','Well01',1,'[{\"added\": {}}]',7,9),(57,'2022-10-19 13:28:31.668490','12','south01',1,'[{\"added\": {}}]',11,9),(58,'2022-10-19 13:28:40.660097','12','south01',2,'[{\"changed\": {\"fields\": [\"Company\"]}}]',11,9),(59,'2022-10-19 13:29:15.555039','7','Well01',2,'[{\"changed\": {\"fields\": [\"FieldName\"]}}]',7,9),(60,'2022-10-19 14:20:38.747011','8','well02',1,'[{\"added\": {}}]',7,9),(61,'2022-10-19 14:21:12.121219','8','well02',2,'[{\"changed\": {\"fields\": [\"FieldName\"]}}]',7,9),(62,'2022-10-19 14:21:51.796781','13','West01',1,'[{\"added\": {}}]',11,9),(63,'2022-10-19 14:22:16.118431','9','well03',1,'[{\"added\": {}}]',7,9),(64,'2022-10-20 11:49:27.470922','5','well02',1,'[{\"added\": {}}]',18,9),(65,'2022-10-20 11:56:54.078721','6','Well01',1,'[{\"added\": {}}]',18,9),(66,'2022-10-20 12:12:22.312995','6','Well01',1,'[{\"added\": {}}]',19,9),(67,'2022-10-20 12:18:52.599788','6','Well01',2,'[]',19,9),(68,'2022-10-20 12:20:14.201740','7','well02',1,'[{\"added\": {}}]',19,9),(69,'2022-10-20 14:10:50.314708','3','setting object (3)',1,'[{\"added\": {}}]',10,9);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `model` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(21,'company','company'),(5,'contenttypes','contenttype'),(11,'field','field'),(19,'kpi','failures'),(18,'kpi','kpidata'),(17,'overview','builduptest'),(14,'overview','espdata'),(13,'overview','espevent'),(12,'overview','rodpumpdata'),(16,'overview','sampletest'),(15,'overview','welltest'),(6,'sessions','session'),(10,'settings','setting'),(20,'users','user'),(9,'well','completion'),(8,'well','fluidproperties'),(7,'well','well');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=129 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (93,'contenttypes','0001_initial','2022-10-18 17:14:01.389203'),(94,'contenttypes','0002_remove_content_type_name','2022-10-18 17:14:01.466490'),(95,'auth','0001_initial','2022-10-18 17:14:01.474289'),(96,'auth','0002_alter_permission_name_max_length','2022-10-18 17:14:01.494865'),(97,'auth','0003_alter_user_email_max_length','2022-10-18 17:14:01.498818'),(98,'auth','0004_alter_user_username_opts','2022-10-18 17:14:01.502822'),(99,'auth','0005_alter_user_last_login_null','2022-10-18 17:14:01.507075'),(100,'auth','0006_require_contenttypes_0002','2022-10-18 17:14:01.508421'),(101,'auth','0007_alter_validators_add_error_messages','2022-10-18 17:14:01.512176'),(102,'auth','0008_alter_user_username_max_length','2022-10-18 17:14:01.515865'),(103,'auth','0009_alter_user_last_name_max_length','2022-10-18 17:14:01.520643'),(104,'auth','0010_alter_group_name_max_length','2022-10-18 17:14:01.538838'),(105,'auth','0011_update_proxy_permissions','2022-10-18 17:14:01.544496'),(106,'auth','0012_alter_user_first_name_max_length','2022-10-18 17:14:01.549380'),(107,'users','0001_initial','2022-10-18 17:14:01.555169'),(108,'admin','0001_initial','2022-10-18 17:14:01.561812'),(109,'admin','0002_logentry_remove_auto_add','2022-10-18 17:14:01.567924'),(110,'admin','0003_logentry_add_action_flag_choices','2022-10-18 17:14:01.573994'),(111,'company','0001_initial','2022-10-18 17:14:01.577927'),(112,'field','0001_initial','2022-10-18 17:14:01.582257'),(113,'well','0001_initial','2022-10-18 17:14:01.601779'),(114,'kpi','0001_initial','2022-10-18 17:14:01.611752'),(115,'kpi','0002_initial','2022-10-18 17:14:01.642864'),(116,'overview','0001_initial','2022-10-18 17:14:01.649549'),(117,'overview','0002_initial','2022-10-18 17:14:01.744141'),(118,'sessions','0001_initial','2022-10-18 17:14:01.748053'),(119,'settings','0001_initial','2022-10-18 17:14:01.751675'),(120,'settings','0002_setting_pumpname','2022-10-18 17:14:01.767736'),(121,'users','0002_alter_user_companyname','2022-10-18 17:28:41.455289'),(122,'company','0002_alter_company_options','2022-10-19 09:52:34.062191'),(123,'well','0002_alter_well_company','2022-10-19 09:52:34.233044'),(124,'field','0002_alter_field_company','2022-10-19 09:57:24.079919'),(125,'well','0003_remove_well_company','2022-10-19 10:01:13.699870'),(126,'users','0003_alter_user_companyname','2022-10-19 10:24:42.215055'),(127,'kpi','0003_remove_kpidata_fieldname','2022-10-20 11:41:59.872966'),(128,'kpi','0004_remove_failures_fieldname','2022-10-20 12:11:46.870008');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('4xdwf407tn0s8jmgv9tohfqun7us05uq','.eJxVjMsOwiAQRf-FtSHClA64dN9vIDM8pGogKe3K-O_apAvd3nPOfQlP21r81tPi5yguworT78YUHqnuIN6p3poMra7LzHJX5EG7nFpMz-vh_h0U6uVbZ6USpQwxjI6RyTkM56AjaAZHqFU22ZiAkTFbQ4SoGEat7eAGGDSI9wcJYzff:1otVY7:yW_Rz-STYtvKXeDBDCtd7Foi6ETP9UQpDOBZ9eD1jYw','2022-11-25 09:02:31.962753'),('fs2hz0wlbtu5azlwh0a0669j77x53pmj','e30:1olbxb:nLvsxq4cKxxYA9dPsQ5X3p1VY7PVFe6C6knCkE-kisE','2022-11-03 15:16:11.868777'),('kth0v6w37drfio2u1i0klemwpjnkp1ep','.eJxVjMsOwiAQRf-FtSHClA64dN9vIDM8pGogKe3K-O_apAvd3nPOfQlP21r81tPi5yguworT78YUHqnuIN6p3poMra7LzHJX5EG7nFpMz-vh_h0U6uVbZ6USpQwxjI6RyTkM56AjaAZHqFU22ZiAkTFbQ4SoGEat7eAGGDSI9wcJYzff:1olc70:aj4JUqVtWvsKPL-7gvFMpY4ZjTpTWIfrurMG-RREfos','2022-11-03 15:25:54.849812'),('nrtyz7af31ipkht4rfzk3qpfs7yxlq85','.eJxVjDsOwyAQRO9CHSF7F7GQMn3OgFg-wUkEkrErK3ePLblINN28N7MJ59eluLWn2U1RXIUVl9-OfXileoD49PXRZGh1mSeWhyJP2uW9xfS-ne7fQfG97GvNaTREI6esDSHvsUgxBx6APFgMSgNk7U0GzAiRVBgosKEUUSsjPl_k3De6:1p0DO6:mAe2VaBaQiOVnZX0ZjV4coLbcYzA16_54P4GmDJWr6U','2022-12-13 21:03:54.134363');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `field_field`
--

DROP TABLE IF EXISTS `field_field`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `field_field` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `DateCreated` datetime(6) NOT NULL,
  `FieldName` varchar(100) NOT NULL,
  `Company_id` bigint NOT NULL,
  `LocationState` varchar(100) NOT NULL,
  `LocationCounty` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `FieldName` (`FieldName`),
  KEY `field_field_Company_id_aa9b5f33` (`Company_id`),
  CONSTRAINT `field_field_Company_id_aa9b5f33_fk_company_company_id` FOREIGN KEY (`Company_id`) REFERENCES `company_company` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `field_field`
--

LOCK TABLES `field_field` WRITE;
/*!40000 ALTER TABLE `field_field` DISABLE KEYS */;
INSERT INTO `field_field` VALUES (11,'2022-10-19 10:02:08.806552','North01',11,'New Mexico','Carlsbad'),(12,'2022-10-19 13:28:31.659545','south01',15,'New Mexico','Carlsbad'),(13,'2022-10-19 14:21:51.795880','West01',15,'New Mexico','Carlsbad');
/*!40000 ALTER TABLE `field_field` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `kpi_failures`
--

DROP TABLE IF EXISTS `kpi_failures`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `kpi_failures` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `DateCreate` datetime(6) NOT NULL,
  `DateFailure` datetime(6) NOT NULL,
  `FailureDiagnosis` varchar(50) DEFAULT NULL,
  `PullOut` datetime(6) NOT NULL,
  `RunLife` double DEFAULT NULL,
  `PumpName_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `kpi_failures_PumpName_id_3ddeee28_fk_well_well_id` (`PumpName_id`),
  CONSTRAINT `kpi_failures_PumpName_id_3ddeee28_fk_well_well_id` FOREIGN KEY (`PumpName_id`) REFERENCES `well_well` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `kpi_failures`
--

LOCK TABLES `kpi_failures` WRITE;
/*!40000 ALTER TABLE `kpi_failures` DISABLE KEYS */;
INSERT INTO `kpi_failures` VALUES (6,'2022-10-20 12:12:22.311537','2022-10-20 12:12:06.000000','Gas interference','2022-10-20 12:12:19.000000',12,7),(7,'2022-10-20 12:20:14.200507','2022-10-20 12:19:55.000000','Gas lock','2022-10-20 12:20:10.000000',12,8);
/*!40000 ALTER TABLE `kpi_failures` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `kpi_kpidata`
--

DROP TABLE IF EXISTS `kpi_kpidata`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `kpi_kpidata` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `DateCreate` datetime(6) NOT NULL,
  `StopHours` double DEFAULT NULL,
  `Deferment` double DEFAULT NULL,
  `RunLife` double DEFAULT NULL,
  `PumpName_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `kpi_kpidata_PumpName_id_31416c7e_fk_well_well_id` (`PumpName_id`),
  CONSTRAINT `kpi_kpidata_PumpName_id_31416c7e_fk_well_well_id` FOREIGN KEY (`PumpName_id`) REFERENCES `well_well` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `kpi_kpidata`
--

LOCK TABLES `kpi_kpidata` WRITE;
/*!40000 ALTER TABLE `kpi_kpidata` DISABLE KEYS */;
INSERT INTO `kpi_kpidata` VALUES (5,'2022-10-20 11:49:27.466278',24,12,12,8),(6,'2022-10-20 11:56:54.077489',12,34,12,7);
/*!40000 ALTER TABLE `kpi_kpidata` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `overview_builduptest`
--

DROP TABLE IF EXISTS `overview_builduptest`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `overview_builduptest` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `DateCreate` datetime(6) NOT NULL,
  `DateStart` datetime(6) NOT NULL,
  `DateEnd` datetime(6) NOT NULL,
  `Duration` double DEFAULT NULL,
  `DataVector` varchar(50) DEFAULT NULL,
  `Permeability` double DEFAULT NULL,
  `Skin` double DEFAULT NULL,
  `Iterated` double DEFAULT NULL,
  `Extrapolated` double DEFAULT NULL,
  `PumpName_id` bigint NOT NULL,
  `UserAuthor_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `overview_builduptest_PumpName_id_6433aee8_fk_well_well_id` (`PumpName_id`),
  KEY `overview_builduptest_UserAuthor_id_f3e483b0_fk_auth_user_id` (`UserAuthor_id`),
  CONSTRAINT `overview_builduptest_PumpName_id_6433aee8_fk_well_well_id` FOREIGN KEY (`PumpName_id`) REFERENCES `well_well` (`id`),
  CONSTRAINT `overview_builduptest_UserAuthor_id_f3e483b0_fk_auth_user_id` FOREIGN KEY (`UserAuthor_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `overview_builduptest`
--

LOCK TABLES `overview_builduptest` WRITE;
/*!40000 ALTER TABLE `overview_builduptest` DISABLE KEYS */;
/*!40000 ALTER TABLE `overview_builduptest` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `overview_espdata`
--

DROP TABLE IF EXISTS `overview_espdata`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `overview_espdata` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `DateCreate` datetime(6) NOT NULL,
  `MotorCurrent` double DEFAULT NULL,
  `MotorVoltage` double DEFAULT NULL,
  `MotorPower` double DEFAULT NULL,
  `MotorTemperature` double DEFAULT NULL,
  `MotorFrequency` double DEFAULT NULL,
  `HeadPressure` double DEFAULT NULL,
  `HeadTemperature` double DEFAULT NULL,
  `CasingPressure` double DEFAULT NULL,
  `FlowlinePressure` double DEFAULT NULL,
  `PumpIntakePressure` double DEFAULT NULL,
  `PumpName_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `overview_espdata_PumpName_id_6bcf8849_fk_well_well_id` (`PumpName_id`),
  CONSTRAINT `overview_espdata_PumpName_id_6bcf8849_fk_well_well_id` FOREIGN KEY (`PumpName_id`) REFERENCES `well_well` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `overview_espdata`
--

LOCK TABLES `overview_espdata` WRITE;
/*!40000 ALTER TABLE `overview_espdata` DISABLE KEYS */;
/*!40000 ALTER TABLE `overview_espdata` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `overview_espevent`
--

DROP TABLE IF EXISTS `overview_espevent`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `overview_espevent` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `DateCreate` datetime(6) NOT NULL,
  `WellEvent` varchar(50) NOT NULL,
  `WellDiagnosis` varchar(50) NOT NULL,
  `FrequencySetPoint` double DEFAULT NULL,
  `PumpName_id` bigint NOT NULL,
  `ChokeOpeningSetpoint` double DEFAULT NULL,
  `EI` double DEFAULT NULL,
  `WellPrediction` double DEFAULT NULL,
  `WellRecomendation` varchar(50) DEFAULT NULL,
  `WellTripAttendant` varchar(50) DEFAULT NULL,
  `TTT` double DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `overview_espevent_PumpName_id_e8cbc435_fk_well_well_id` (`PumpName_id`),
  CONSTRAINT `overview_espevent_PumpName_id_e8cbc435_fk_well_well_id` FOREIGN KEY (`PumpName_id`) REFERENCES `well_well` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `overview_espevent`
--

LOCK TABLES `overview_espevent` WRITE;
/*!40000 ALTER TABLE `overview_espevent` DISABLE KEYS */;
/*!40000 ALTER TABLE `overview_espevent` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `overview_rodpumpdata`
--

DROP TABLE IF EXISTS `overview_rodpumpdata`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `overview_rodpumpdata` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `DateCreate` datetime(6) NOT NULL,
  `LoadPump` longtext,
  `Position` longtext,
  `Acceleration` longtext,
  `HeadPressure` double DEFAULT NULL,
  `HeadTemperature` double DEFAULT NULL,
  `CasingPressure` double DEFAULT NULL,
  `ChokeOpening` double DEFAULT NULL,
  `SPM` double DEFAULT NULL,
  `Diagnosis` varchar(181) NOT NULL,
  `PumpFill` double DEFAULT NULL,
  `PumpName_id` bigint NOT NULL,
  `Recomendation` varchar(112) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `overview_rodpumpdata_PumpName_id_f35505a9_fk_well_well_id` (`PumpName_id`),
  CONSTRAINT `overview_rodpumpdata_PumpName_id_f35505a9_fk_well_well_id` FOREIGN KEY (`PumpName_id`) REFERENCES `well_well` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `overview_rodpumpdata`
--

LOCK TABLES `overview_rodpumpdata` WRITE;
/*!40000 ALTER TABLE `overview_rodpumpdata` DISABLE KEYS */;
INSERT INTO `overview_rodpumpdata` VALUES (29,'2022-11-22 17:18:39.147860','-0.116863,-0.133492,-0.13224, -0.131204, -0.115662, -0.108361, -0.100633, -0.062337, -0.039234, -0.014274, 0.00671, 0.027603, 0.040257, 0.048467, 0.063063, 0.075082, 0.091043, 0.123612, 0.204957, 0.303319, 0.422977, 0.554067, 0.57552, 0.580881, 0.655107, 0.722934, 0.772274, 0.823984, 0.9098, 0.975054, 0.949615, 0.960195, 1.072513, 1.1637, 1.247615, 1.36905, 1.526718, 1.662537, 1.78626, 1.919013, 2.026537, 2.133305, 2.27201, 2.335151, 2.389074, 2.492409, 2.575076, 2.62982, 2.666933, 2.74732, 2.891879, 2.996248, 3.113507, 3.328443, 3.555255, 3.816204, 4.059807, 4.140088, 4.191977, 4.315909, 4.43777, 4.508986, 4.590649, 4.713305, 4.787735, 4.733293, 4.68655, 4.788833, 4.853186, 4.903371, 4.986526, 5.025222, 5.032483, 4.971216, 4.946202, 4.985578, 5.008294, 5.023204, 5.066891, 5.089863, 5.060068, 5.004624, 4.999466, 5.051386, 5.064309, 5.015946, 5.005263, 4.966937, 4.903968, 4.852128, 4.844595, 4.870957, 4.885206, 4.902094, 4.924288, 4.939092, 4.929774, 4.930195, 4.972487, 5.006593, 5.013516, 5.010544, 5.022108, 5.042478, 5.040546, 5.063276, 5.099872, 5.136432, 5.152356, 5.175439, 5.187413, 5.1899, 5.194599, 5.215748, 5.249594, 5.261498, 5.262021, 5.263415, 5.275979, 5.296831, 5.316024, 5.340149, 5.381562, 5.404564, 5.410508, 5.419314, 5.401795, 5.384694, 5.390037, 5.396556, 5.395159, 5.398235, 5.395992, 5.400695, 5.384497, 5.358325, 5.352825, 5.346692, 5.327323, 5.31823, 5.282331, 5.236778, 5.197974, 5.161954, 5.140222, 5.100017, 5.030208, 4.975104, 4.951023, 4.933447, 4.897051, 4.832115, 4.740756, 4.616214, 4.417002, 4.231369, 4.029758, 3.840071, 3.745493, 3.667772, 3.551997, 3.423431, 3.294296, 3.177836, 3.07198, 2.993942, 2.943498, 2.867029, 2.713833, 2.540338, 2.303189, 2.032418, 1.77198, 1.553593, 1.321204, 1.093537, 0.889326, 0.758311, 0.693733, 0.663141, 0.589784, 0.558461, 0.565224, 0.532775, 0.45245, 0.404684, 0.380894, 0.376953, 0.286674, 0.189594, 0.150912, 0.145161, 0.125557, 0.143676, 0.105723, 0.042924, 0.037458, 0.023245, 0.027845, 0.051173, 0.081284, 0.117357, 0.104659, 0.077682, 0.072141, 0.075356, 0.081818, 0.092105, 0.098849, 0.120668, 0.125864, 0.079007, 0.055041, 0.038585, 0.034783, 0.029436, 0.027255, 0.014687, 0.001993, -0.02913, -0.031009, -0.029013, -0.043331, -0.050122, -0.052471, -0.077431, -0.118426, -0.143725, -0.131978, -0.120166, -0.131359, -0.142375, -0.131526, -0.146644, -0.166109, -0.172841, -0.167503, -0.152027, -0.161415, -0.153014, -0.148339, -0.146669, -0.143002, -0.132851, -0.110045, -0.102658, -0.096116, -0.091049, -0.095275, -0.106433, -0.113105\"','\"0.04696, 0.060031, 0.079042, 0.115401, 0.159684, 0.19812, 0.238613, 0.289096, 0.355159, 0.439904, 0.542453, 0.661167, 0.796733, 0.957953, 1.150849, 1.372066, 1.614834, 1.870671, 2.12619, 2.358641, 2.557099, 2.741857, 2.923539, 3.11604, 3.345561, 3.577955, 3.776526, 3.991497, 4.254172, 4.503221, 4.710185, 4.927365, 5.161163, 5.396766, 5.672657, 6.001985, 6.368487, 6.732653, 7.061894, 7.372165, 7.673087, 7.969105, 8.266402, 8.5511, 8.835779, 9.168452, 9.549031, 9.926271, 10.306865, 10.72625, 11.141196, 11.540488, 11.959191, 12.386089, 12.778565, 13.11407, 13.413944, 13.701654, 13.996627, 14.303143, 14.57956, 14.818189, 15.096488, 15.440366, 15.779655, 16.108357, 16.515929, 17.016933, 17.579355, 18.233001, 19.027673, 19.969298, 21.04261, 22.243177, 23.547016, 24.9196, 26.342116, 27.813896, 29.343269, 30.912118, 32.466403, 33.99022, 35.512763, 37.019282, 38.461369, 39.844133, 41.181323, 42.458958, 43.65841, 44.775395, 45.813865, 46.777226, 47.683649, 48.548373, 49.36883, 50.14125, 50.872326, 51.580898, 52.291061, 52.998433, 53.69423, 54.392479, 55.105417, 55.818987, 56.522053, 57.22335, 57.931166, 58.646727, 59.377991, 60.12647, 60.877364, 61.623896, 62.366041, 63.098769, 63.80822, 64.483327, 65.117887, 65.716219, 66.282345, 66.803456, 67.269606, 67.686847, 68.059215, 68.379455, 68.641795, 68.851737, 69.013658, 69.135135, 69.234447, 69.312466, 69.355301, 69.369851, 69.371591, 69.355422, 69.316678, 69.267685, 69.219739, 69.175377, 69.138379, 69.111324, 69.090763, 69.070993, 69.046687, 69.000877, 68.917757, 68.800829, 68.665767, 68.520494, 68.348382, 68.115815, 67.816819, 67.484216, 67.116629, 66.69549, 66.265672, 65.89248, 65.572073, 65.271273, 64.981655, 64.6835, 64.355074, 64.018599, 63.684274, 63.319148, 62.920628, 62.522046, 62.133493, 61.75364, 61.383951, 60.987636, 60.530086, 60.024902, 59.500077, 58.984662, 58.493192, 58.018688, 57.563945, 57.120413, 56.648024, 56.114232, 55.507938, 54.827561, 54.084603, 53.270811, 52.370202, 51.406075, 50.387205, 49.270543, 48.032543, 46.681701, 45.20939, 43.628195, 41.989862, 40.307922, 38.570419, 36.814008, 35.086345, 33.394293, 31.741101, 30.140778, 28.59958, 27.126005, 25.736867, 24.431502, 23.196817, 22.034265, 20.951536, 19.952434, 19.039826, 18.204188, 17.425289, 16.701542, 16.031156, 15.388455, 14.747599, 14.112445, 13.497327, 12.894693, 12.286401, 11.664127, 11.025681, 10.37237, 9.707193, 9.036829, 8.364888, 7.688724, 7.008339, 6.338435, 5.691125, 5.055856, 4.430145, 3.837008, 3.289672, 2.7806, 2.311001, 1.892386, 1.528571, 1.218469, 0.961298, 0.751376, 0.578266, 0.428129, 0.300177, 0.198106, 0.122823, 0.068528, 0.028874, 0.007145, 0.0, 0.006872, 0.027494\"','0',125,87,145,0.8,6.45,'Full pump',95,9,'Good work area');
/*!40000 ALTER TABLE `overview_rodpumpdata` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `overview_sampletest`
--

DROP TABLE IF EXISTS `overview_sampletest`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `overview_sampletest` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `DateCreate` datetime(6) NOT NULL,
  `DateTest` datetime(6) NOT NULL,
  `WaterCut` double DEFAULT NULL,
  `SandPercentage` double DEFAULT NULL,
  `EmultionPercentage` double DEFAULT NULL,
  `PumpName_id` bigint NOT NULL,
  `UserAuthor_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `overview_sampletest_PumpName_id_08afbd93_fk_well_well_id` (`PumpName_id`),
  KEY `overview_sampletest_UserAuthor_id_8d92efd0_fk_auth_user_id` (`UserAuthor_id`),
  CONSTRAINT `overview_sampletest_PumpName_id_08afbd93_fk_well_well_id` FOREIGN KEY (`PumpName_id`) REFERENCES `well_well` (`id`),
  CONSTRAINT `overview_sampletest_UserAuthor_id_8d92efd0_fk_auth_user_id` FOREIGN KEY (`UserAuthor_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `overview_sampletest`
--

LOCK TABLES `overview_sampletest` WRITE;
/*!40000 ALTER TABLE `overview_sampletest` DISABLE KEYS */;
/*!40000 ALTER TABLE `overview_sampletest` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `overview_welltest`
--

DROP TABLE IF EXISTS `overview_welltest`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `overview_welltest` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `DateCreate` datetime(6) NOT NULL,
  `DateStart` date NOT NULL,
  `DateEnd` date NOT NULL,
  `Duration` double DEFAULT NULL,
  `OilRate` double DEFAULT NULL,
  `WaterRate` double DEFAULT NULL,
  `GasRate` double DEFAULT NULL,
  `PumpName_id` bigint NOT NULL,
  `UserAuthor_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `overview_welltest_PumpName_id_6135ddae_fk_well_well_id` (`PumpName_id`),
  KEY `overview_welltest_UserAuthor_id_d016f0df_fk_auth_user_id` (`UserAuthor_id`),
  CONSTRAINT `overview_welltest_PumpName_id_6135ddae_fk_well_well_id` FOREIGN KEY (`PumpName_id`) REFERENCES `well_well` (`id`),
  CONSTRAINT `overview_welltest_UserAuthor_id_d016f0df_fk_auth_user_id` FOREIGN KEY (`UserAuthor_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `overview_welltest`
--

LOCK TABLES `overview_welltest` WRITE;
/*!40000 ALTER TABLE `overview_welltest` DISABLE KEYS */;
INSERT INTO `overview_welltest` VALUES (1,'2022-10-20 14:26:36.035545','2022-10-20','2022-10-20',24,234,12,122,7,8),(2,'2022-10-20 14:27:29.875700','2022-10-20','2022-10-20',12,1223,122,11,8,8);
/*!40000 ALTER TABLE `overview_welltest` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `settings_setting`
--

DROP TABLE IF EXISTS `settings_setting`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `settings_setting` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `DateCreated` datetime(6) NOT NULL,
  `PumpName_id` bigint NOT NULL,
  `Available` tinyint(1) NOT NULL,
  `IpAddress` varchar(100) NOT NULL,
  `ControlMode` varchar(10) NOT NULL,
  `ControlSetPoint` double DEFAULT NULL,
  `ControlSetPointChokeValve` double DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `PumpName` (`PumpName_id`),
  UNIQUE KEY `IpAddress` (`IpAddress`),
  CONSTRAINT `settings_setting_PumpName_id_558af12b_fk_well_well_id` FOREIGN KEY (`PumpName_id`) REFERENCES `well_well` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `settings_setting`
--

LOCK TABLES `settings_setting` WRITE;
/*!40000 ALTER TABLE `settings_setting` DISABLE KEYS */;
INSERT INTO `settings_setting` VALUES (3,'2022-10-20 14:10:50.313622',7,1,'10.10.10.122','Amperage',0.9,0.9),(4,'2023-09-17 15:49:07.102000',9,1,'10.10.50.12','Frequency',0.98,0.6);
/*!40000 ALTER TABLE `settings_setting` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_user`
--

DROP TABLE IF EXISTS `users_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users_user` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `password` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `UserName` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Email` varchar(254) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Name` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `LastName` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `CompanyName_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `UserName` (`UserName`),
  KEY `users_user_CompanyName_id_637d17b1` (`CompanyName_id`),
  CONSTRAINT `users_user_CompanyName_id_637d17b1_fk_company_company_id` FOREIGN KEY (`CompanyName_id`) REFERENCES `company_company` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_user`
--

LOCK TABLES `users_user` WRITE;
/*!40000 ALTER TABLE `users_user` DISABLE KEYS */;
INSERT INTO `users_user` VALUES (8,'pbkdf2_sha256$260000$BR7WiDt7XaibASY57NODPz$dvSMvEfUuMN8q4gsfyx4v5jKW6C1tyZ4+U+uXKR1Z64=','2022-11-29 20:54:29.527208',1,'gle_developer','jhanccop@gmail.com','Joel','Hancco',1,11),(9,'pbkdf2_sha256$260000$Upt3qTqyU7LZx3kggZ8pcS$AW+vW9YnhJqAWX0zL3/nBSEtTK8+GWTlT/0TKbDQiic=','2022-11-29 21:03:54.132494',1,'user01','user01@gmail.com','user01','nn',1,15);
/*!40000 ALTER TABLE `users_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_user_groups`
--

DROP TABLE IF EXISTS `users_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users_user_groups` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` bigint NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_user_groups_user_id_group_id_b88eab82_uniq` (`user_id`,`group_id`),
  KEY `users_user_groups_group_id_9afc8d0e_fk_auth_group_id` (`group_id`),
  CONSTRAINT `users_user_groups_group_id_9afc8d0e_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `users_user_groups_user_id_5f6f5a90_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_user_groups`
--

LOCK TABLES `users_user_groups` WRITE;
/*!40000 ALTER TABLE `users_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `users_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_user_user_permissions`
--

DROP TABLE IF EXISTS `users_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users_user_user_permissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` bigint NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_user_user_permissions_user_id_permission_id_43338c45_uniq` (`user_id`,`permission_id`),
  KEY `users_user_user_perm_permission_id_0b93982e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `users_user_user_perm_permission_id_0b93982e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `users_user_user_permissions_user_id_20aca447_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_user_user_permissions`
--

LOCK TABLES `users_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `users_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `users_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `well_completion`
--

DROP TABLE IF EXISTS `well_completion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `well_completion` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `DateCreate` datetime(6) NOT NULL,
  `TransformerInputVoltage` double DEFAULT NULL,
  `TransformerOutputVoltage` double DEFAULT NULL,
  `TransformerPower` double DEFAULT NULL,
  `AmbientTemperature` double DEFAULT NULL,
  `ESPumpType` varchar(100) NOT NULL,
  `StateType` varchar(50) NOT NULL,
  `Downthrust` double DEFAULT NULL,
  `Upthrust` double DEFAULT NULL,
  `SetDepth` double DEFAULT NULL,
  `NumberOfStages` double DEFAULT NULL,
  `BestEfficiencyPoint` double DEFAULT NULL,
  `MotorType` varchar(100) NOT NULL,
  `NominalCurrent` double DEFAULT NULL,
  `NominalFrequency` double DEFAULT NULL,
  `TemperatureResistance` varchar(50) NOT NULL,
  `NominalVoltage` double DEFAULT NULL,
  `NominalPower` double DEFAULT NULL,
  `IdleCurrent` double DEFAULT NULL,
  `TubingDiameter` double DEFAULT NULL,
  `CasingDiameter` double DEFAULT NULL,
  `LinerDiameter` double DEFAULT NULL,
  `TubingDepth` double DEFAULT NULL,
  `CasingDepth` double DEFAULT NULL,
  `LinerDepth` double DEFAULT NULL,
  `SaparatorType` varchar(50) NOT NULL,
  `PumpName_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `well_completion_PumpName_id_cf3c6c6b_fk_well_well_id` (`PumpName_id`),
  CONSTRAINT `well_completion_PumpName_id_cf3c6c6b_fk_well_well_id` FOREIGN KEY (`PumpName_id`) REFERENCES `well_well` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `well_completion`
--

LOCK TABLES `well_completion` WRITE;
/*!40000 ALTER TABLE `well_completion` DISABLE KEYS */;
/*!40000 ALTER TABLE `well_completion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `well_fluidproperties`
--

DROP TABLE IF EXISTS `well_fluidproperties`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `well_fluidproperties` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `DateCreate` datetime(6) NOT NULL,
  `API` double DEFAULT NULL,
  `Viscosity` double DEFAULT NULL,
  `BurblePoint` double DEFAULT NULL,
  `DewPoint` double DEFAULT NULL,
  `PumpName_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `well_fluidproperties_PumpName_id_136ce9c7_fk_well_well_id` (`PumpName_id`),
  CONSTRAINT `well_fluidproperties_PumpName_id_136ce9c7_fk_well_well_id` FOREIGN KEY (`PumpName_id`) REFERENCES `well_well` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `well_fluidproperties`
--

LOCK TABLES `well_fluidproperties` WRITE;
/*!40000 ALTER TABLE `well_fluidproperties` DISABLE KEYS */;
/*!40000 ALTER TABLE `well_fluidproperties` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `well_well`
--

DROP TABLE IF EXISTS `well_well`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `well_well` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `DateCreate` datetime(6) NOT NULL,
  `PumpName` varchar(100) NOT NULL,
  `FieldName_id` bigint NOT NULL,
  `Location` varchar(100) NOT NULL,
  `InstallationDate` date NOT NULL,
  `InstallationComment` longtext NOT NULL,
  `PumpType` varchar(50) NOT NULL,
  `UserAuthor_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `PumpName` (`PumpName`),
  KEY `well_well_UserAuthor_id_a92f2128_fk_auth_user_id` (`UserAuthor_id`),
  KEY `well_well_Field_id_dfd074aa` (`FieldName_id`),
  CONSTRAINT `well_well_FieldName_id_c727fda5_fk_field_field_id` FOREIGN KEY (`FieldName_id`) REFERENCES `field_field` (`id`),
  CONSTRAINT `well_well_UserAuthor_id_a92f2128_fk_auth_user_id` FOREIGN KEY (`UserAuthor_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `well_well`
--

LOCK TABLES `well_well` WRITE;
/*!40000 ALTER TABLE `well_well` DISABLE KEYS */;
INSERT INTO `well_well` VALUES (7,'2022-10-19 10:03:10.232676','Well01',12,'coordenates','2022-10-19','Well','Sucker Rod Pump',9),(8,'2022-10-19 14:20:38.745922','well02',12,'MMM','2022-10-19','fff','Electrical Submersible Pump',9),(9,'2022-10-19 14:22:16.116727','well03',13,'mmmmh','2022-10-19','rooo','Sucker Rod Pump',8);
/*!40000 ALTER TABLE `well_well` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-11-29 22:23:42
