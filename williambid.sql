-- MySQL dump 10.13  Distrib 5.6.30, for debian-linux-gnu (i686)
--
-- Host: localhost    Database: williambid
-- ------------------------------------------------------
-- Server version	5.6.30-1

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_0e939a4f` (`group_id`),
  KEY `auth_group_permissions_8373b171` (`permission_id`),
  CONSTRAINT `auth_group_permissi_permission_id_23962d04_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_58c48ba9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_417f1b1c` (`content_type_id`),
  CONSTRAINT `auth_permissi_content_type_id_51277a81_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add tipo subasta',7,'add_tiposubasta'),(20,'Can change tipo subasta',7,'change_tiposubasta'),(21,'Can delete tipo subasta',7,'delete_tiposubasta'),(22,'Can add content',8,'add_content'),(23,'Can change content',8,'change_content'),(24,'Can delete content',8,'delete_content'),(25,'Can edit untranslated fields',8,'can_edit_untranslated_fields_of_content'),(26,'Can add articulo',9,'add_articulo'),(27,'Can change articulo',9,'change_articulo'),(28,'Can delete articulo',9,'delete_articulo'),(29,'Can add paquete bid',10,'add_paquetebid'),(30,'Can change paquete bid',10,'change_paquetebid'),(31,'Can delete paquete bid',10,'delete_paquetebid'),(32,'Can add venta',11,'add_venta'),(33,'Can change venta',11,'change_venta'),(34,'Can delete venta',11,'delete_venta'),(35,'Can add venta articulo',12,'add_ventaarticulo'),(36,'Can change venta articulo',12,'change_ventaarticulo'),(37,'Can delete venta articulo',12,'delete_ventaarticulo'),(38,'Can add venta paquete bid',13,'add_ventapaquetebid'),(39,'Can change venta paquete bid',13,'change_ventapaquetebid'),(40,'Can delete venta paquete bid',13,'delete_ventapaquetebid'),(41,'Can add subasta',14,'add_subasta'),(42,'Can change subasta',14,'change_subasta'),(43,'Can delete subasta',14,'delete_subasta'),(44,'Can add robot',15,'add_robot'),(45,'Can change robot',15,'change_robot'),(46,'Can delete robot',15,'delete_robot'),(47,'Can add tipo membresia',16,'add_tipomembresia'),(48,'Can change tipo membresia',16,'change_tipomembresia'),(49,'Can delete tipo membresia',16,'delete_tipomembresia'),(50,'Can add membresia',17,'add_membresia'),(51,'Can change membresia',17,'change_membresia'),(52,'Can delete membresia',17,'delete_membresia'),(53,'Can add tipo usuario',18,'add_tipousuario'),(54,'Can change tipo usuario',18,'change_tipousuario'),(55,'Can delete tipo usuario',18,'delete_tipousuario'),(56,'Can add perfil usuario',19,'add_perfilusuario'),(57,'Can change perfil usuario',19,'change_perfilusuario'),(58,'Can delete perfil usuario',19,'delete_perfilusuario'),(59,'Can add banco usuario',20,'add_bancousuario'),(60,'Can change banco usuario',20,'change_bancousuario'),(61,'Can delete banco usuario',20,'delete_bancousuario'),(62,'Can add historial transacciones',21,'add_historialtransacciones'),(63,'Can change historial transacciones',21,'change_historialtransacciones'),(64,'Can delete historial transacciones',21,'delete_historialtransacciones'),(65,'Can add mensaje',22,'add_mensaje'),(66,'Can change mensaje',22,'change_mensaje'),(67,'Can delete mensaje',22,'delete_mensaje'),(68,'Can add invitacion',23,'add_invitacion'),(69,'Can change invitacion',23,'change_invitacion'),(70,'Can delete invitacion',23,'delete_invitacion'),(71,'Can add tipo reto',24,'add_tiporeto'),(72,'Can change tipo reto',24,'change_tiporeto'),(73,'Can delete tipo reto',24,'delete_tiporeto'),(74,'Can add reto',25,'add_reto'),(75,'Can change reto',25,'change_reto'),(76,'Can delete reto',25,'delete_reto'),(77,'Can add estado reto usuario',26,'add_estadoretousuario'),(78,'Can change estado reto usuario',26,'change_estadoretousuario'),(79,'Can delete estado reto usuario',26,'delete_estadoretousuario'),(80,'Can add plan compensacion',27,'add_plancompensacion'),(81,'Can change plan compensacion',27,'change_plancompensacion'),(82,'Can delete plan compensacion',27,'delete_plancompensacion'),(83,'Can add beneficios',28,'add_beneficios'),(84,'Can change beneficios',28,'change_beneficios'),(85,'Can delete beneficios',28,'delete_beneficios'),(86,'Can add advertisement tool',29,'add_advertisementtool'),(87,'Can change advertisement tool',29,'change_advertisementtool'),(88,'Can delete advertisement tool',29,'delete_advertisementtool'),(89,'Can add auto puja',30,'add_autopuja'),(90,'Can change auto puja',30,'change_autopuja'),(91,'Can delete auto puja',30,'delete_autopuja'),(92,'Can add shoppingg cart',31,'add_shoppinggcart'),(93,'Can change shoppingg cart',31,'change_shoppinggcart'),(94,'Can delete shoppingg cart',31,'delete_shoppinggcart'),(95,'Can add subasta vendida',32,'add_subastavendida'),(96,'Can change subasta vendida',32,'change_subastavendida'),(97,'Can delete subasta vendida',32,'delete_subastavendida'),(98,'Can add PayPal IPN',33,'add_paypalipn'),(99,'Can change PayPal IPN',33,'change_paypalipn'),(100,'Can delete PayPal IPN',33,'delete_paypalipn');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$12000$55W34OMevFJT$6F4Z4uU7ev8QL/R+dn/1C+KHOsatKqy/3Y0jwNyrzhQ=','2016-10-06 18:49:27',1,'admin','','','admin@uci.cu',1,1,'2016-05-07 23:49:32'),(7,'pbkdf2_sha256$12000$55W34OMevFJT$6F4Z4uU7ev8QL/R+dn/1C+KHOsatKqy/3Y0jwNyrzhQ=','2016-10-03 22:58:19',0,'addiaz','','','addiaz@uci.cu',0,1,'2016-05-09 23:20:06'),(8,'','2016-09-28 23:59:57',0,'rulico','','','',0,1,'2016-09-28 23:59:57'),(9,'','2016-09-29 00:00:06',0,'kavitat','','','',0,1,'2016-09-29 00:00:06'),(10,'','2016-09-29 00:00:16',0,'lememu','','','',0,1,'2016-09-29 00:00:16'),(11,'','2016-09-29 00:00:26',0,'virure','','','',0,1,'2016-09-29 00:00:26'),(12,'','2016-09-29 00:00:36',0,'jigaki','','','',0,1,'2016-09-29 00:00:36'),(13,'pbkdf2_sha256$12000$OCMGc0KgId27$EqKhh0n5rG6x1OchUzeL8NwvTdJM/1ZivP2yIgsw+QA=','2016-09-30 20:13:47',0,'briseida','','','briseida.bussott@nauta.cu',0,1,'2016-09-30 20:13:47');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_e8701ad4` (`user_id`),
  KEY `auth_user_groups_0e939a4f` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_30a071c9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_24702650_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_e8701ad4` (`user_id`),
  KEY `auth_user_user_permissions_8373b171` (`permission_id`),
  CONSTRAINT `auth_user_user_perm_permission_id_3d7071f0_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_7cd7acb6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `back_office_advertisementtool`
--

DROP TABLE IF EXISTS `back_office_advertisementtool`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `back_office_advertisementtool` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(200) NOT NULL,
  `description` longtext NOT NULL,
  `tool_file` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `back_office_advertisementtool`
--

LOCK TABLES `back_office_advertisementtool` WRITE;
/*!40000 ALTER TABLE `back_office_advertisementtool` DISABLE KEYS */;
INSERT INTO `back_office_advertisementtool` VALUES (1,'fgg','dfgdfgdg','static/tools/2016/05/10/Learning_Python.pdf');
/*!40000 ALTER TABLE `back_office_advertisementtool` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `back_office_bancousuario`
--

DROP TABLE IF EXISTS `back_office_bancousuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `back_office_bancousuario` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `usuario_id` int(11) NOT NULL,
  `tipo_plan` int(11) NOT NULL,
  `monto_total` double NOT NULL,
  PRIMARY KEY (`id`),
  KEY `back_office_bancousuario_c69e2c81` (`usuario_id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `back_office_bancousuario`
--

LOCK TABLES `back_office_bancousuario` WRITE;
/*!40000 ALTER TABLE `back_office_bancousuario` DISABLE KEYS */;
INSERT INTO `back_office_bancousuario` VALUES (1,1,4,1624.8),(2,2,4,660.4),(3,3,4,579.6),(4,4,4,330),(5,5,4,330),(6,6,4,330),(7,1,2,69955.44),(8,7,4,442),(9,1,12,94137.8435),(10,1,9,6217000),(11,8,4,191.2),(12,9,4,95.6),(13,10,4,95.6),(14,11,4,95.6),(15,12,4,95.6),(16,8,2,1092.77),(17,1,14,8524.0415),(18,13,4,46);
/*!40000 ALTER TABLE `back_office_bancousuario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `back_office_beneficios`
--

DROP TABLE IF EXISTS `back_office_beneficios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `back_office_beneficios` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `beneficio_total_empresa` int(11) NOT NULL,
  `beneficio_total_empresa_socios_VIP_PRO` int(11) NOT NULL,
  `facturacion_global` int(11) NOT NULL,
  `distribuido` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `back_office_beneficios`
--

LOCK TABLES `back_office_beneficios` WRITE;
/*!40000 ALTER TABLE `back_office_beneficios` DISABLE KEYS */;
/*!40000 ALTER TABLE `back_office_beneficios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `back_office_estadoretousuario`
--

DROP TABLE IF EXISTS `back_office_estadoretousuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `back_office_estadoretousuario` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `reto_id` int(11) NOT NULL,
  `usuario_id` int(11) NOT NULL,
  `cantidad_personas` int(11) DEFAULT NULL,
  `dinero_paquetes_de_pujas` double DEFAULT NULL,
  `cantidad_de_paquetes_de_pujas` int(11) DEFAULT NULL,
  `ganador` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `back_office_estadoretousuario_bacfab2b` (`reto_id`),
  KEY `back_office_estadoretousuario_c69e2c81` (`usuario_id`),
  CONSTRAINT `reto_id_refs_id_ddd61983` FOREIGN KEY (`reto_id`) REFERENCES `back_office_reto` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `back_office_estadoretousuario`
--

LOCK TABLES `back_office_estadoretousuario` WRITE;
/*!40000 ALTER TABLE `back_office_estadoretousuario` DISABLE KEYS */;
/*!40000 ALTER TABLE `back_office_estadoretousuario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `back_office_historialtransacciones`
--

DROP TABLE IF EXISTS `back_office_historialtransacciones`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `back_office_historialtransacciones` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cuenta_id` int(11) NOT NULL,
  `cantidad` double NOT NULL,
  `deposito` tinyint(1) NOT NULL,
  `fecha` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `back_office_historialtransacciones_d3f603f8` (`cuenta_id`),
  CONSTRAINT `cuenta_id_refs_id_83f115d3` FOREIGN KEY (`cuenta_id`) REFERENCES `back_office_bancousuario` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `back_office_historialtransacciones`
--

LOCK TABLES `back_office_historialtransacciones` WRITE;
/*!40000 ALTER TABLE `back_office_historialtransacciones` DISABLE KEYS */;
/*!40000 ALTER TABLE `back_office_historialtransacciones` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `back_office_invitacion`
--

DROP TABLE IF EXISTS `back_office_invitacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `back_office_invitacion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `de_usuario_id` int(11) NOT NULL,
  `para` varchar(50) NOT NULL,
  `para_correo` varchar(75) NOT NULL,
  `url` varchar(200) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `back_office_invitacion_2db5027c` (`de_usuario_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `back_office_invitacion`
--

LOCK TABLES `back_office_invitacion` WRITE;
/*!40000 ALTER TABLE `back_office_invitacion` DISABLE KEYS */;
/*!40000 ALTER TABLE `back_office_invitacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `back_office_membresia`
--

DROP TABLE IF EXISTS `back_office_membresia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `back_office_membresia` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tipo_membresia_id` int(11) NOT NULL,
  `numero_bids_mensuales` int(11) NOT NULL,
  `posibilidad_pack_anual_con_descuento` tinyint(1) NOT NULL,
  `accionista_de_empresa` tinyint(1) NOT NULL,
  `precio` double NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `tipo_membresia_id` (`tipo_membresia_id`),
  CONSTRAINT `tipo_membresia_id_refs_id_0a6f7678` FOREIGN KEY (`tipo_membresia_id`) REFERENCES `back_office_tipomembresia` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `back_office_membresia`
--

LOCK TABLES `back_office_membresia` WRITE;
/*!40000 ALTER TABLE `back_office_membresia` DISABLE KEYS */;
INSERT INTO `back_office_membresia` VALUES (1,1,0,0,1,0),(2,2,10,1,1,10),(3,3,25,1,1,20),(4,4,50,1,1,30),(5,5,100,1,1,50),(6,6,250,1,1,100),(7,7,500,1,1,150),(8,8,1000,1,1,300),(9,9,2000,1,1,500);
/*!40000 ALTER TABLE `back_office_membresia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `back_office_mensaje`
--

DROP TABLE IF EXISTS `back_office_mensaje`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `back_office_mensaje` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `de_usuario_id` int(11) NOT NULL,
  `para_usuario_id` int(11) NOT NULL,
  `mensaje` longtext NOT NULL,
  `leido` tinyint(1) NOT NULL,
  `fecha_enviado` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `back_office_mensaje_2db5027c` (`de_usuario_id`),
  KEY `back_office_mensaje_0d1f0fe3` (`para_usuario_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `back_office_mensaje`
--

LOCK TABLES `back_office_mensaje` WRITE;
/*!40000 ALTER TABLE `back_office_mensaje` DISABLE KEYS */;
INSERT INTO `back_office_mensaje` VALUES (1,1,7,'Mensaje de prueba',1,'2016-09-27 20:58:01');
/*!40000 ALTER TABLE `back_office_mensaje` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `back_office_perfilusuario`
--

DROP TABLE IF EXISTS `back_office_perfilusuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `back_office_perfilusuario` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `usuario_id` int(11) NOT NULL,
  `padre_id` int(11) DEFAULT NULL,
  `tipo_usuario_id` int(11) NOT NULL,
  `membresia_id` int(11) NOT NULL,
  `fecha_obtuvo_membresia` datetime NOT NULL,
  `direccion` longtext NOT NULL,
  `ciudad` varchar(100) NOT NULL,
  `provincia` varchar(100) NOT NULL,
  `pais` varchar(100) NOT NULL,
  `telefono` longtext NOT NULL,
  `seudonimo` varchar(100) NOT NULL,
  `whatsapp_id` varchar(100) NOT NULL,
  `skype_id` varchar(100) NOT NULL,
  `cantidad_de_puntos` int(11) NOT NULL,
  `cantidad_de_bids` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `usuario_id` (`usuario_id`),
  UNIQUE KEY `seudonimo` (`seudonimo`),
  KEY `back_office_perfilusuario_b475db24` (`padre_id`),
  KEY `back_office_perfilusuario_b74f55c2` (`tipo_usuario_id`),
  KEY `back_office_perfilusuario_9e785f44` (`membresia_id`),
  CONSTRAINT `membresia_id_refs_id_b5147a87` FOREIGN KEY (`membresia_id`) REFERENCES `back_office_membresia` (`id`),
  CONSTRAINT `padre_id_refs_id_b61580a6` FOREIGN KEY (`padre_id`) REFERENCES `back_office_perfilusuario` (`id`),
  CONSTRAINT `tipo_usuario_id_refs_id_b6fcdeeb` FOREIGN KEY (`tipo_usuario_id`) REFERENCES `back_office_tipousuario` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `back_office_perfilusuario`
--

LOCK TABLES `back_office_perfilusuario` WRITE;
/*!40000 ALTER TABLE `back_office_perfilusuario` DISABLE KEYS */;
INSERT INTO `back_office_perfilusuario` VALUES (1,1,NULL,8,9,'2016-10-06 19:39:23','Test Dir','Gtmo','Gtmo','Cuba','054232332','Admin','adminwhatsapp','adminskype',1,936),(7,7,1,1,1,'2016-10-06 19:39:23','Calle5','Gtmo','Gtmo','Cuba','054232332','lcol88','assdfdf','dsfsdf',1,3),(8,8,1,1,3,'2016-10-06 18:39:06','','','','','','rulico','','',50,0),(9,9,1,1,2,'2016-10-06 18:39:06','','','','','','kavitat','','',20,0),(10,10,1,1,2,'2016-09-29 00:05:01','','','','','','lememu','','',0,0),(11,11,8,1,5,'2016-09-29 00:05:01','','','','','','virure','','',0,0),(12,12,9,1,3,'2016-09-29 00:05:01','','','','','','jigaki','','',0,0),(13,13,7,1,1,'2016-09-30 20:14:08','Calle5','Gtmo','Gtmo','Cuba','054232332','brissi','asdsad','dasdasd',0,0);
/*!40000 ALTER TABLE `back_office_perfilusuario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `back_office_plancompensacion`
--

DROP TABLE IF EXISTS `back_office_plancompensacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `back_office_plancompensacion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `num_plan` int(11) NOT NULL,
  `descripcion` longtext NOT NULL,
  `requisito` tinyint(1) NOT NULL,
  `tipo_usuario_id` int(11) DEFAULT NULL,
  `membresia_minima_id` int(11) DEFAULT NULL,
  `cantidad_de_usuarios_en_red` int(11) DEFAULT NULL,
  `cantidad_de_dinero` double DEFAULT NULL,
  `cantidad_de_puntos` int(11) DEFAULT NULL,
  `title` varchar(50),
  PRIMARY KEY (`id`),
  KEY `back_office_plancompensacion_b74f55c2` (`tipo_usuario_id`),
  KEY `back_office_plancompensacion_52edb915` (`membresia_minima_id`),
  CONSTRAINT `membresia_minima_id_refs_id_1011e996` FOREIGN KEY (`membresia_minima_id`) REFERENCES `back_office_tipomembresia` (`id`),
  CONSTRAINT `tipo_usuario_id_refs_id_f420cf6b` FOREIGN KEY (`tipo_usuario_id`) REFERENCES `back_office_tipousuario` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `back_office_plancompensacion`
--

LOCK TABLES `back_office_plancompensacion` WRITE;
/*!40000 ALTER TABLE `back_office_plancompensacion` DISABLE KEYS */;
INSERT INTO `back_office_plancompensacion` VALUES (1,1,'MEMBRESIAS EN LA RED 2,4,6,10,15,20',1,1,1,0,0,0,'MEMBRESIAS EN LA RED 2,4,6,10,15,20'),(2,2,'BINARIO HIBRIDO',1,1,2,2,0,50,'BINARIO HIBRIDO'),(3,3,'PLAN UNILEVEL DE VENTA DIRECTA DE PUJAS',1,1,1,0,0,0,'PLAN UNILEVEL DE VENTA DIRECTA DE PUJAS'),(4,4,'BINARIO POR DERRAME EMPRESA MENSUAL',1,1,2,0,0,0,'BINARIO POR DERRAME EMPRESA MENSUAL'),(5,5,'BONOS DE LOGRO (RETOS)',1,1,1,0,0,0,'BONOS DE LOGRO (RETOS)'),(6,6,'BENEFICIO A MEMBRESIAS DE PAGO',1,1,2,0,0,0,'BENEFICIO A MEMBRESIAS DE PAGO'),(7,7,'BENEFICIO VIP Y VIP WINNER',1,1,8,0,0,0,'BENEFICIO VIP Y VIP WINNER'),(8,8,'FONDO GLOBAL DE LIDERAZGO',1,1,1,0,100000,0,'FONDO GLOBAL DE LIDERAZGO'),(9,9,'BONO 1000',1,1,1,0,20000,0,'BONO 1000'),(10,10,'BONO 31',1,1,1,0,15000,0,'BONO 31'),(11,11,'PLAN DE AUTOENRIQUECIMIENTO\r\n',1,1,1,0,0,0,'PLAN DE AUTOENRIQUECIMIENTO\r\n'),(12,12,'BONO DE IGUALACIÓN EN LA RED 2,4,6,10,15',1,4,1,0,0,0,'BONO DE IGUALACIÓN EN LA RED 2,4,6,10,15'),(13,13,'BONO DE IGUALACIÓN PLAN UNILEVEL',1,4,1,0,0,0,'BONO DE IGUALACIÓN PLAN UNILEVEL'),(14,14,'BONO DE IGUALACIÓN DEL BINARIO HIBRIDO',1,4,1,0,0,0,'BONO DE IGUALACIÓN DEL BINARIO HIBRIDO');
/*!40000 ALTER TABLE `back_office_plancompensacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `back_office_reto`
--

DROP TABLE IF EXISTS `back_office_reto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `back_office_reto` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tipo_reto_id` int(11) NOT NULL,
  `personas` int(11) DEFAULT NULL,
  `membresia_id` int(11) DEFAULT NULL,
  `tiempo` datetime DEFAULT NULL,
  `dinero_pujas` double DEFAULT NULL,
  `dinero` double NOT NULL,
  `terminado` tinyint(1) NOT NULL,
  `cerrado` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `back_office_reto_dd3160ef` (`tipo_reto_id`),
  KEY `back_office_reto_9e785f44` (`membresia_id`),
  CONSTRAINT `membresia_id_refs_id_8ddcc278` FOREIGN KEY (`membresia_id`) REFERENCES `back_office_tipomembresia` (`id`),
  CONSTRAINT `tipo_reto_id_refs_id_f5d8f4be` FOREIGN KEY (`tipo_reto_id`) REFERENCES `back_office_tiporeto` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `back_office_reto`
--

LOCK TABLES `back_office_reto` WRITE;
/*!40000 ALTER TABLE `back_office_reto` DISABLE KEYS */;
INSERT INTO `back_office_reto` VALUES (1,1,30,4,'2016-05-20 00:00:00',0,40,1,0),(2,2,NULL,5,'2016-05-18 00:00:00',0,70,1,0);
/*!40000 ALTER TABLE `back_office_reto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `back_office_tipomembresia`
--

DROP TABLE IF EXISTS `back_office_tipomembresia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `back_office_tipomembresia` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `back_office_tipomembresia`
--

LOCK TABLES `back_office_tipomembresia` WRITE;
/*!40000 ALTER TABLE `back_office_tipomembresia` DISABLE KEYS */;
INSERT INTO `back_office_tipomembresia` VALUES (1,'Free'),(2,'Junior'),(3,'Amateur'),(4,'Semi-Profesional'),(5,'Profesional'),(6,'Player'),(7,'Player-Pro'),(8,'VIP'),(9,'VIP Winner');
/*!40000 ALTER TABLE `back_office_tipomembresia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `back_office_tiporeto`
--

DROP TABLE IF EXISTS `back_office_tiporeto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `back_office_tiporeto` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `descripcion` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `back_office_tiporeto`
--

LOCK TABLES `back_office_tiporeto` WRITE;
/*!40000 ALTER TABLE `back_office_tiporeto` DISABLE KEYS */;
INSERT INTO `back_office_tiporeto` VALUES (1,'Si consigues registrar a un total de X personas con membresias X antes de XFecha ganaras X $'),(2,'Si consigues hacer que los usuarios de tu primera generacion pasen a una membresia X antes de XFecha ganaras X $'),(3,'Si consigues vender X dinero en pujas, ganaras X $');
/*!40000 ALTER TABLE `back_office_tiporeto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `back_office_tipousuario`
--

DROP TABLE IF EXISTS `back_office_tipousuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `back_office_tipousuario` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `back_office_tipousuario`
--

LOCK TABLES `back_office_tipousuario` WRITE;
/*!40000 ALTER TABLE `back_office_tipousuario` DISABLE KEYS */;
INSERT INTO `back_office_tipousuario` VALUES (1,'Team Trainer'),(2,'Team Leader'),(3,'Team Coordinator'),(4,'National Director'),(5,'International Director'),(6,'National Vicepresident'),(7,'International Vicepresident'),(8,'Team President');
/*!40000 ALTER TABLE `back_office_tipousuario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_417f1b1c` (`content_type_id`),
  KEY `django_admin_log_e8701ad4` (`user_id`),
  CONSTRAINT `django_admin__content_type_id_5151027a_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_1c5f563_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=43 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2016-05-08 01:05:27','1','Plan de compensacion: 1',1,'',27,1),(2,'2016-05-08 01:06:44','2','Plan de compensacion: 2',1,'',27,1),(3,'2016-05-08 01:07:57','3','Plan de compensacion: 3',1,'',27,1),(4,'2016-05-08 01:08:18','4','Plan de compensacion: 4',1,'',27,1),(5,'2016-05-08 01:09:41','5','Plan de compensacion: 5',1,'',27,1),(6,'2016-05-08 01:12:49','6','Plan de compensacion: 6',1,'',27,1),(7,'2016-05-08 01:13:21','7','Plan de compensacion: 7',1,'',27,1),(8,'2016-05-08 01:14:03','8','Plan de compensacion: 8',1,'',27,1),(9,'2016-05-08 01:14:52','9','Plan de compensacion: 9',1,'',27,1),(10,'2016-05-08 01:15:17','10','Plan de compensacion: 10',1,'',27,1),(11,'2016-05-08 01:15:31','11','Plan de compensacion: 11',1,'',27,1),(12,'2016-05-08 01:16:39','12','Plan de compensacion: 12',1,'',27,1),(13,'2016-05-08 01:16:51','13','Plan de compensacion: 13',1,'',27,1),(14,'2016-05-08 01:17:21','14','Plan de compensacion: 14',1,'',27,1),(15,'2016-05-08 01:18:07','13','Plan de compensacion: 13',2,'Modificado/a tipo_usuario.',27,1),(16,'2016-05-08 01:18:15','12','Plan de compensacion: 12',2,'Modificado/a tipo_usuario.',27,1),(17,'2016-05-08 14:54:03','9','Plan de compensacion: 9',2,'Modificado/a cantidad_de_dinero.',27,1),(18,'2016-05-08 14:54:24','10','Plan de compensacion: 10',2,'Modificado/a cantidad_de_dinero.',27,1),(19,'2016-05-08 14:58:54','10','Plan de compensacion: 10',2,'Modificado/a descripcion.',27,1),(20,'2016-05-08 14:59:05','9','Plan de compensacion: 9',2,'Modificado/a descripcion.',27,1),(21,'2016-05-08 14:59:14','8','Plan de compensacion: 8',2,'Modificado/a descripcion.',27,1),(22,'2016-05-08 15:00:02','7','Plan de compensacion: 7',2,'Modificado/a descripcion.',27,1),(23,'2016-05-08 15:00:35','6','Plan de compensacion: 6',2,'Modificado/a descripcion.',27,1),(24,'2016-05-08 15:00:39','5','Plan de compensacion: 5',2,'No ha cambiado ningún campo.',27,1),(25,'2016-05-08 15:01:03','1','Plan de compensacion: 1',2,'Modificado/a descripcion.',27,1),(26,'2016-05-08 15:15:39','7','Plan de compensacion: 7',2,'Modificado/a descripcion.',27,1),(27,'2016-05-10 01:56:11','1','AdvertisementTool object',1,'',29,1),(28,'2016-05-10 02:13:38','1','Si consigues registrar a un total de X personas con membresias X antes de XFecha ganaras X $',1,'',25,1),(29,'2016-05-10 02:15:11','2','Si consigues hacer que los usuarios de tu primera generacion pasen a una membresia X antes de XFecha ganaras X $',1,'',25,1),(30,'2016-08-24 21:32:41','1','Pullas',1,'',9,1),(31,'2016-08-24 22:03:43','1','Pullas',1,'',9,1),(32,'2016-08-25 12:01:02','2','Tennis',1,'',9,1),(33,'2016-08-25 13:24:45','3','30, 5.0',1,'',10,1),(34,'2016-09-30 00:29:43','4','Chair',1,'',9,1),(35,'2016-09-30 00:46:14','50','Subasta de Chair',1,'',14,1),(36,'2016-09-30 00:51:12','51','Subasta de Chair',1,'',14,1),(37,'2016-09-30 01:03:40','52','Subasta de Chair',1,'',14,1),(38,'2016-09-30 01:12:00','53','Subasta de Chair',1,'',14,1),(39,'2016-09-30 01:12:28','54','Subasta de Chair',1,'',14,1),(40,'2016-09-30 01:21:23','55','Subasta de Chair',1,'',14,1),(41,'2016-09-30 01:25:48','56','Subasta de Chair',1,'',14,1),(42,'2016-09-30 01:28:41','57','Subasta de Chair',1,'',14,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_3ec8c61c_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'log entry','admin','logentry'),(2,'permission','auth','permission'),(3,'group','auth','group'),(4,'user','auth','user'),(5,'content type','contenttypes','contenttype'),(6,'session','sessions','session'),(7,'tipo subasta','williambid','tiposubasta'),(8,'content','williambid','content'),(9,'articulo','williambid','articulo'),(10,'paquete bid','williambid','paquetebid'),(11,'venta','williambid','venta'),(12,'venta articulo','williambid','ventaarticulo'),(13,'venta paquete bid','williambid','ventapaquetebid'),(14,'subasta','williambid','subasta'),(15,'robot','williambid','robot'),(16,'tipo membresia','back_office','tipomembresia'),(17,'membresia','back_office','membresia'),(18,'tipo usuario','back_office','tipousuario'),(19,'perfil usuario','back_office','perfilusuario'),(20,'banco usuario','back_office','bancousuario'),(21,'historial transacciones','back_office','historialtransacciones'),(22,'mensaje','back_office','mensaje'),(23,'invitacion','back_office','invitacion'),(24,'tipo reto','back_office','tiporeto'),(25,'reto','back_office','reto'),(26,'estado reto usuario','back_office','estadoretousuario'),(27,'plan compensacion','back_office','plancompensacion'),(28,'beneficios','back_office','beneficios'),(29,'advertisement tool','back_office','advertisementtool'),(30,'auto puja','williambid','autopuja'),(31,'shoppingg cart','williambid','shoppinggcart'),(32,'subasta vendida','williambid','subastavendida'),(33,'PayPal IPN','ipn','paypalipn');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2016-08-24 21:59:26'),(2,'auth','0001_initial','2016-08-24 21:59:26'),(3,'admin','0001_initial','2016-08-24 21:59:26'),(4,'sessions','0001_initial','2016-08-24 21:59:26'),(5,'back_office','0001_initial','2016-09-27 22:43:17'),(6,'back_office','0002_auto_20160928_1855','2016-09-28 18:55:29'),(7,'williambid','0001_initial','2016-09-28 18:55:29'),(8,'back_office','0003_membresia_precio','2016-09-30 18:36:31'),(9,'ipn','0001_initial','2016-10-03 21:51:02'),(10,'ipn','0002_paypalipn_mp_id','2016-10-03 21:51:03'),(11,'ipn','0003_auto_20141117_1647','2016-10-03 21:51:04'),(12,'ipn','0004_auto_20150612_1826','2016-10-03 21:51:18'),(13,'ipn','0005_auto_20151217_0948','2016-10-03 21:51:19'),(14,'ipn','0006_auto_20160108_1112','2016-10-03 21:51:20'),(15,'ipn','0007_auto_20160219_1135','2016-10-03 21:51:21');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('06d5lf9tdlw652vhj4em29s496otk3gd','YTIzMmMxNjljZTk4ZmI1MDdhYzFhMjhiYjAyMmY0ODczYWFmNjEyNzp7fQ==','2016-09-09 13:31:56'),('26sbgcemcenal27segn5lmklvk6wdpw7','Mzg2ZjRkYTQ4YzNjNGQ2OGUyNDUwNTE2MjM4NjkxMGIzNGEzNmI2NDp7Il9hdXRoX3VzZXJfaGFzaCI6ImNmNjcwOWY2MTczZjBkYmIxZTEwZTBhM2E1OTY2MGZlMzQ4MDg2ODEiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9','2016-10-20 18:49:27'),('2sp518kdrtpq1v8j9hwp2tbjq9t1wm5o','YTIzMmMxNjljZTk4ZmI1MDdhYzFhMjhiYjAyMmY0ODczYWFmNjEyNzp7fQ==','2016-10-12 20:54:10'),('3n4k1dz1kau2v6eko73cc44xsrzr8zdi','YTIzMmMxNjljZTk4ZmI1MDdhYzFhMjhiYjAyMmY0ODczYWFmNjEyNzp7fQ==','2016-09-09 13:31:56'),('7wqop381xk21maqevpqjgrorzygtj89o','YTIzMmMxNjljZTk4ZmI1MDdhYzFhMjhiYjAyMmY0ODczYWFmNjEyNzp7fQ==','2016-10-14 00:52:07'),('909bne4rmiadekm0m3tgumm07lmg5vxc','YTIzMmMxNjljZTk4ZmI1MDdhYzFhMjhiYjAyMmY0ODczYWFmNjEyNzp7fQ==','2016-10-20 18:49:27'),('a6zvymsawfctj3skdkl7i13b3u1wzibr','YTIzMmMxNjljZTk4ZmI1MDdhYzFhMjhiYjAyMmY0ODczYWFmNjEyNzp7fQ==','2016-10-20 18:49:27'),('agxxl6ehlykcipl82i5ufb57dsf5uwbh','Mzg2ZjRkYTQ4YzNjNGQ2OGUyNDUwNTE2MjM4NjkxMGIzNGEzNmI2NDp7Il9hdXRoX3VzZXJfaGFzaCI6ImNmNjcwOWY2MTczZjBkYmIxZTEwZTBhM2E1OTY2MGZlMzQ4MDg2ODEiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9','2016-07-19 18:12:27'),('aki1su6xlmmzyj12gstm4chpnywqtnmx','YTIzMmMxNjljZTk4ZmI1MDdhYzFhMjhiYjAyMmY0ODczYWFmNjEyNzp7fQ==','2016-10-14 20:14:32'),('b8a8b0ajfurb8r2wrrx8o6mwfj8jmols','YTIzMmMxNjljZTk4ZmI1MDdhYzFhMjhiYjAyMmY0ODczYWFmNjEyNzp7fQ==','2016-10-20 18:49:27'),('k2aepc66kln2sqxl4xugp6n7lw80be4f','YTIzMmMxNjljZTk4ZmI1MDdhYzFhMjhiYjAyMmY0ODczYWFmNjEyNzp7fQ==','2016-10-14 00:52:07'),('kd1z0jm79uubesto1lehyaqbqdpqo0dt','YTIzMmMxNjljZTk4ZmI1MDdhYzFhMjhiYjAyMmY0ODczYWFmNjEyNzp7fQ==','2016-10-12 20:54:10'),('l4hyo2hxyjex62g2n2cmg8w4mybpnive','YTIzMmMxNjljZTk4ZmI1MDdhYzFhMjhiYjAyMmY0ODczYWFmNjEyNzp7fQ==','2016-10-14 20:14:32'),('mjcz4nffrfu8167fn1yxfco2ttdew98q','YTIzMmMxNjljZTk4ZmI1MDdhYzFhMjhiYjAyMmY0ODczYWFmNjEyNzp7fQ==','2016-10-14 20:14:32'),('mobasiu0bvynpe3c3usnu0hhxrr562n3','YTIzMmMxNjljZTk4ZmI1MDdhYzFhMjhiYjAyMmY0ODczYWFmNjEyNzp7fQ==','2016-09-09 13:31:56'),('owhfnwa1ghzmax70jwjfwlg90txxsdm7','ZjE1NTM2YTc5YTdiZjQ0MWRjZmE5ODc4ODhjYmY5MmZlMTY5ZGI3NDp7Il9hdXRoX3VzZXJfaGFzaCI6ImNmNjcwOWY2MTczZjBkYmIxZTEwZTBhM2E1OTY2MGZlMzQ4MDg2ODEiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjd9','2016-09-12 18:21:46'),('qwouwlshl28e6mztfxcp5usm6hfou3ay','YjJjYjU3MjhlMTU1ZmJhNWE4ODgxZTcyOTAyZTBkMmUzNmIxZWQ2Zjp7InNoYXJlcl9wYXJlbnQiOiJhZGRpYXoiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6ImNmNjcwOWY2MTczZjBkYmIxZTEwZTBhM2E1OTY2MGZlMzQ4MDg2ODEiLCJfYXV0aF91c2VyX2lkIjo3LCJfc2Vzc2lvbl9leHBpcnkiOjB9','2016-10-14 20:14:32'),('u31iu6la981mmodpnbe01lkhplzncjtw','YTIzMmMxNjljZTk4ZmI1MDdhYzFhMjhiYjAyMmY0ODczYWFmNjEyNzp7fQ==','2016-10-14 00:52:07'),('v1trlumpbfh4vg9tut41812nodn1kcrc','YTIzMmMxNjljZTk4ZmI1MDdhYzFhMjhiYjAyMmY0ODczYWFmNjEyNzp7fQ==','2016-05-21 23:49:54'),('vv7zl8et25mdykfceryaxc108oem6p2j','Mzg2ZjRkYTQ4YzNjNGQ2OGUyNDUwNTE2MjM4NjkxMGIzNGEzNmI2NDp7Il9hdXRoX3VzZXJfaGFzaCI6ImNmNjcwOWY2MTczZjBkYmIxZTEwZTBhM2E1OTY2MGZlMzQ4MDg2ODEiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9','2016-05-24 01:14:30'),('wev45t86dsy8oy3jvwxjrs0v3h25kktl','Mzg2ZjRkYTQ4YzNjNGQ2OGUyNDUwNTE2MjM4NjkxMGIzNGEzNmI2NDp7Il9hdXRoX3VzZXJfaGFzaCI6ImNmNjcwOWY2MTczZjBkYmIxZTEwZTBhM2E1OTY2MGZlMzQ4MDg2ODEiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9','2016-10-14 01:02:11'),('wzv67rqitwxlgchi4zfg2amufhbj8xez','YTIzMmMxNjljZTk4ZmI1MDdhYzFhMjhiYjAyMmY0ODczYWFmNjEyNzp7fQ==','2016-10-14 00:52:07'),('z5vwatmvnm1azvgk5oitlmwd96pjzh43','YTIzMmMxNjljZTk4ZmI1MDdhYzFhMjhiYjAyMmY0ODczYWFmNjEyNzp7fQ==','2016-10-12 20:54:10');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `paypal_ipn`
--

DROP TABLE IF EXISTS `paypal_ipn`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `paypal_ipn` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `business` varchar(127) NOT NULL,
  `charset` varchar(255),
  `custom` varchar(256),
  `notify_version` decimal(64,2) DEFAULT NULL,
  `parent_txn_id` varchar(19) NOT NULL,
  `receiver_email` varchar(254),
  `receiver_id` varchar(255),
  `residence_country` varchar(2) NOT NULL,
  `test_ipn` tinyint(1) NOT NULL,
  `txn_id` varchar(255),
  `txn_type` varchar(255),
  `verify_sign` varchar(255) NOT NULL,
  `address_country` varchar(64) NOT NULL,
  `address_city` varchar(40) NOT NULL,
  `address_country_code` varchar(64) NOT NULL,
  `address_name` varchar(128) NOT NULL,
  `address_state` varchar(40) NOT NULL,
  `address_status` varchar(255),
  `address_street` varchar(200) NOT NULL,
  `address_zip` varchar(20) NOT NULL,
  `contact_phone` varchar(20) NOT NULL,
  `first_name` varchar(64) NOT NULL,
  `last_name` varchar(64) NOT NULL,
  `payer_business_name` varchar(127) NOT NULL,
  `payer_email` varchar(127) NOT NULL,
  `payer_id` varchar(13) NOT NULL,
  `auth_amount` decimal(64,2) DEFAULT NULL,
  `auth_exp` varchar(28) NOT NULL,
  `auth_id` varchar(19) NOT NULL,
  `auth_status` varchar(255),
  `exchange_rate` decimal(64,16) DEFAULT NULL,
  `invoice` varchar(127) NOT NULL,
  `item_name` varchar(127) NOT NULL,
  `item_number` varchar(127) NOT NULL,
  `mc_currency` varchar(32) NOT NULL,
  `mc_fee` decimal(64,2) DEFAULT NULL,
  `mc_gross` decimal(64,2) DEFAULT NULL,
  `mc_handling` decimal(64,2) DEFAULT NULL,
  `mc_shipping` decimal(64,2) DEFAULT NULL,
  `memo` varchar(255) NOT NULL,
  `num_cart_items` int(11) DEFAULT NULL,
  `option_name1` varchar(64) NOT NULL,
  `option_name2` varchar(64) NOT NULL,
  `payer_status` varchar(255),
  `payment_date` datetime DEFAULT NULL,
  `payment_gross` decimal(64,2) DEFAULT NULL,
  `payment_status` varchar(255),
  `payment_type` varchar(255),
  `pending_reason` varchar(255),
  `protection_eligibility` varchar(255),
  `quantity` int(11) DEFAULT NULL,
  `reason_code` varchar(255),
  `remaining_settle` decimal(64,2) DEFAULT NULL,
  `settle_amount` decimal(64,2) DEFAULT NULL,
  `settle_currency` varchar(32) NOT NULL,
  `shipping` decimal(64,2) DEFAULT NULL,
  `shipping_method` varchar(255) NOT NULL,
  `tax` decimal(64,2) DEFAULT NULL,
  `transaction_entity` varchar(255),
  `auction_buyer_id` varchar(64) NOT NULL,
  `auction_closing_date` datetime DEFAULT NULL,
  `auction_multi_item` int(11) DEFAULT NULL,
  `for_auction` decimal(64,2) DEFAULT NULL,
  `amount` decimal(64,2) DEFAULT NULL,
  `amount_per_cycle` decimal(64,2) DEFAULT NULL,
  `initial_payment_amount` decimal(64,2) DEFAULT NULL,
  `next_payment_date` datetime DEFAULT NULL,
  `outstanding_balance` decimal(64,2) DEFAULT NULL,
  `payment_cycle` varchar(255),
  `period_type` varchar(255),
  `product_name` varchar(255),
  `product_type` varchar(255),
  `profile_status` varchar(255),
  `recurring_payment_id` varchar(255),
  `rp_invoice_id` varchar(127) NOT NULL,
  `time_created` datetime DEFAULT NULL,
  `amount1` decimal(64,2) DEFAULT NULL,
  `amount2` decimal(64,2) DEFAULT NULL,
  `amount3` decimal(64,2) DEFAULT NULL,
  `mc_amount1` decimal(64,2) DEFAULT NULL,
  `mc_amount2` decimal(64,2) DEFAULT NULL,
  `mc_amount3` decimal(64,2) DEFAULT NULL,
  `password` varchar(24) NOT NULL,
  `period1` varchar(255),
  `period2` varchar(255),
  `period3` varchar(255),
  `reattempt` varchar(1) NOT NULL,
  `recur_times` int(11) DEFAULT NULL,
  `recurring` varchar(1) NOT NULL,
  `retry_at` datetime DEFAULT NULL,
  `subscr_date` datetime DEFAULT NULL,
  `subscr_effective` datetime DEFAULT NULL,
  `subscr_id` varchar(19) NOT NULL,
  `username` varchar(64) NOT NULL,
  `case_creation_date` datetime DEFAULT NULL,
  `case_id` varchar(255),
  `case_type` varchar(255),
  `receipt_id` varchar(255),
  `currency_code` varchar(32) NOT NULL,
  `handling_amount` decimal(64,2) DEFAULT NULL,
  `transaction_subject` varchar(256),
  `ipaddress` char(39),
  `flag` tinyint(1) NOT NULL,
  `flag_code` varchar(16) NOT NULL,
  `flag_info` longtext NOT NULL,
  `query` longtext NOT NULL,
  `response` longtext NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `from_view` varchar(6) DEFAULT NULL,
  `mp_id` varchar(128),
  `option_selection1` varchar(200) NOT NULL,
  `option_selection2` varchar(200) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `paypal_ipn_8e113603` (`txn_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `paypal_ipn`
--

LOCK TABLES `paypal_ipn` WRITE;
/*!40000 ALTER TABLE `paypal_ipn` DISABLE KEYS */;
/*!40000 ALTER TABLE `paypal_ipn` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `robots`
--

DROP TABLE IF EXISTS `robots`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `robots` (
  `id_robot` int(11) NOT NULL AUTO_INCREMENT,
  `usuario_id` int(11) NOT NULL,
  `subasta_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_robot`),
  UNIQUE KEY `usuario_id` (`usuario_id`),
  UNIQUE KEY `subasta_id` (`subasta_id`),
  CONSTRAINT `subasta_id_refs_id_9277c5be` FOREIGN KEY (`subasta_id`) REFERENCES `williambid_subasta` (`id`),
  CONSTRAINT `usuario_id_refs_id_2d79d63d` FOREIGN KEY (`usuario_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `robots`
--

LOCK TABLES `robots` WRITE;
/*!40000 ALTER TABLE `robots` DISABLE KEYS */;
INSERT INTO `robots` VALUES (1,8,NULL),(2,9,NULL),(3,10,NULL),(4,11,NULL),(5,12,NULL);
/*!40000 ALTER TABLE `robots` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `williambid_articulo`
--

DROP TABLE IF EXISTS `williambid_articulo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `williambid_articulo` (
  `content_ptr_id` int(11) NOT NULL,
  `imagen` varchar(100) NOT NULL,
  `cantidad_de_articulos` int(11) NOT NULL,
  `precio` double NOT NULL,
  `pujas_automaticas` tinyint(1) NOT NULL,
  PRIMARY KEY (`content_ptr_id`),
  CONSTRAINT `content_ptr_id_refs_id_15c42207` FOREIGN KEY (`content_ptr_id`) REFERENCES `williambid_content` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `williambid_articulo`
--

LOCK TABLES `williambid_articulo` WRITE;
/*!40000 ALTER TABLE `williambid_articulo` DISABLE KEYS */;
INSERT INTO `williambid_articulo` VALUES (1,'static/media/img/articulos/2016/08/24/pullas_PoMK521.jpg',34,21,1),(2,'static/media/img/articulos/2016/08/25/tennis.jpg',25,45,1),(4,'static/media/img/articulos/2016/09/30/sillon.jpg',21,26,0);
/*!40000 ALTER TABLE `williambid_articulo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `williambid_autopuja`
--

DROP TABLE IF EXISTS `williambid_autopuja`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `williambid_autopuja` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `usuario_id` int(11) NOT NULL,
  `cantidad_pujas` int(11) NOT NULL,
  `articulo_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `williambid_autopuja_c69e2c81` (`usuario_id`),
  KEY `williambid_autopuja_1818f191` (`articulo_id`),
  CONSTRAINT `articulo_id_refs_content_ptr_id_e9118234` FOREIGN KEY (`articulo_id`) REFERENCES `williambid_articulo` (`content_ptr_id`),
  CONSTRAINT `usuario_id_refs_id_d7ecfe60` FOREIGN KEY (`usuario_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `williambid_autopuja`
--

LOCK TABLES `williambid_autopuja` WRITE;
/*!40000 ALTER TABLE `williambid_autopuja` DISABLE KEYS */;
INSERT INTO `williambid_autopuja` VALUES (2,1,0,1);
/*!40000 ALTER TABLE `williambid_autopuja` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `williambid_content`
--

DROP TABLE IF EXISTS `williambid_content`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `williambid_content` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre_en_us` varchar(30) DEFAULT NULL,
  `nombre_es_es` varchar(30) DEFAULT NULL,
  `descripcion_en_us` varchar(50) DEFAULT NULL,
  `descripcion_es_es` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `williambid_content`
--

LOCK TABLES `williambid_content` WRITE;
/*!40000 ALTER TABLE `williambid_content` DISABLE KEYS */;
INSERT INTO `williambid_content` VALUES (1,'Pullas','Pullas','Pullas','Pullas'),(2,'Tennis','Tennis','Tennis','Tennis'),(3,'30x1','30x1','30x1','30x1'),(4,'Chair','Silla','Chair','Silla');
/*!40000 ALTER TABLE `williambid_content` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `williambid_paquetebid`
--

DROP TABLE IF EXISTS `williambid_paquetebid`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `williambid_paquetebid` (
  `content_ptr_id` int(11) NOT NULL,
  `cantidad_de_bids` int(11) NOT NULL,
  `precio` double NOT NULL,
  PRIMARY KEY (`content_ptr_id`),
  CONSTRAINT `content_ptr_id_refs_id_d2961be6` FOREIGN KEY (`content_ptr_id`) REFERENCES `williambid_content` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `williambid_paquetebid`
--

LOCK TABLES `williambid_paquetebid` WRITE;
/*!40000 ALTER TABLE `williambid_paquetebid` DISABLE KEYS */;
INSERT INTO `williambid_paquetebid` VALUES (3,30,5);
/*!40000 ALTER TABLE `williambid_paquetebid` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `williambid_shoppinggcart`
--

DROP TABLE IF EXISTS `williambid_shoppinggcart`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `williambid_shoppinggcart` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `usuario_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `usuario_id` (`usuario_id`),
  CONSTRAINT `usuario_id_refs_id_d3b79a79` FOREIGN KEY (`usuario_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `williambid_shoppinggcart`
--

LOCK TABLES `williambid_shoppinggcart` WRITE;
/*!40000 ALTER TABLE `williambid_shoppinggcart` DISABLE KEYS */;
INSERT INTO `williambid_shoppinggcart` VALUES (2,1),(1,7),(3,13);
/*!40000 ALTER TABLE `williambid_shoppinggcart` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `williambid_subasta`
--

DROP TABLE IF EXISTS `williambid_subasta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `williambid_subasta` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `contenido_id` int(11) NOT NULL,
  `tipo_subasta_id` int(11) NOT NULL,
  `fecha_inicio` datetime NOT NULL,
  `tiempo_regresivo` time NOT NULL,
  `fecha_expiracion` datetime DEFAULT NULL,
  `precio_actual` double NOT NULL,
  `gana_robot` tinyint(1) NOT NULL,
  `membresia_minima_id` int(11) DEFAULT NULL,
  `estado` int(11) NOT NULL,
  `ganador_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `williambid_subasta_09f63960` (`contenido_id`),
  KEY `williambid_subasta_2e74af73` (`tipo_subasta_id`),
  KEY `williambid_subasta_52edb915` (`membresia_minima_id`),
  KEY `williambid_subasta_b4d3e69f` (`ganador_id`),
  CONSTRAINT `contenido_id_refs_id_947493fa` FOREIGN KEY (`contenido_id`) REFERENCES `williambid_content` (`id`),
  CONSTRAINT `ganador_id_refs_id_a4fad395` FOREIGN KEY (`ganador_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `membresia_minima_id_refs_id_cf9ed601` FOREIGN KEY (`membresia_minima_id`) REFERENCES `back_office_tipomembresia` (`id`),
  CONSTRAINT `tipo_subasta_id_refs_id_e9c7925a` FOREIGN KEY (`tipo_subasta_id`) REFERENCES `williambid_tiposubasta` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=68 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `williambid_subasta`
--

LOCK TABLES `williambid_subasta` WRITE;
/*!40000 ALTER TABLE `williambid_subasta` DISABLE KEYS */;
INSERT INTO `williambid_subasta` VALUES (31,3,1,'2016-09-29 11:59:02','00:01:00','2016-09-29 12:00:02',4.5,1,NULL,3,NULL),(32,1,1,'2016-09-29 11:59:03','00:01:00','2016-09-29 00:01:36',17.88,1,NULL,3,1),(33,2,1,'2016-09-29 11:59:57','00:01:00','2016-09-29 01:24:54',38.27,1,NULL,3,8),(34,1,1,'2016-09-29 12:01:36','00:01:00','2016-09-29 00:03:21',17.88,1,NULL,3,1),(35,1,1,'2016-09-29 12:04:02','00:01:00','2016-09-29 00:06:06',17.88,1,NULL,3,1),(36,1,1,'2016-09-29 12:09:29','00:01:00','2016-09-29 00:11:03',17.88,1,NULL,3,1),(37,1,1,'2016-09-29 12:14:11','00:01:00','2016-09-29 00:17:00',17.94,1,NULL,3,1),(38,1,1,'2016-09-29 12:20:55','00:01:00','2016-09-29 00:22:04',17.86,1,NULL,3,1),(39,1,1,'2016-09-29 12:24:36','00:01:00','2016-09-29 00:26:45',17.88,1,NULL,3,1),(40,1,1,'2016-09-29 12:43:26','00:01:00','2016-09-29 00:47:25',17.94,1,NULL,3,1),(41,1,1,'2016-09-29 12:49:15','00:01:00','2016-09-29 00:52:24',18,1,NULL,3,1),(42,1,1,'2016-09-29 12:56:51','00:01:00','2016-09-29 01:00:05',17.94,1,NULL,3,1),(43,1,1,'2016-09-29 13:06:12','00:01:00','2016-09-29 01:08:36',17.9,1,NULL,3,1),(44,1,1,'2016-09-29 13:16:18','00:01:00','2016-09-29 01:21:31',17.91,1,NULL,3,8),(45,1,1,'2016-09-29 13:21:30','00:01:00','2016-09-29 13:22:30',17.85,1,NULL,3,NULL),(46,2,1,'2016-09-29 13:25:01','00:01:00','2016-09-29 13:26:01',38.25,1,NULL,3,NULL),(47,3,1,'2016-09-30 11:39:39','00:01:00','2016-09-30 11:40:39',4.5,1,NULL,3,NULL),(48,1,1,'2016-09-30 11:39:39','00:01:00','2016-09-30 11:40:39',17.85,1,NULL,3,NULL),(49,2,1,'2016-09-30 11:39:48','00:01:00','2016-09-30 11:40:48',38.25,1,NULL,3,NULL),(50,4,2,'2016-09-30 00:42:36','00:01:00','2016-09-30 00:43:36',22.1,0,1,3,NULL),(51,4,2,'2016-10-12 00:00:00','00:01:00','2016-09-30 00:53:17',22.12,0,1,3,7),(52,4,3,'2016-09-30 01:03:20','00:01:00','2016-09-30 01:04:55',22.11,0,1,3,7),(53,4,3,'2016-09-30 01:03:20','00:01:00','2016-09-30 01:04:20',22.1,0,1,3,NULL),(54,4,3,'2016-09-30 06:00:00','00:01:00','2016-09-30 01:16:25',22.16,0,1,3,8),(55,4,4,'2016-09-30 06:00:00','00:01:00','2016-09-30 01:22:34',22.11,0,1,3,7),(56,4,4,'2016-09-30 06:00:00','00:01:00','2016-09-30 01:27:30',22.12,0,1,3,8),(57,4,4,'2016-09-30 06:00:00','00:01:00','2016-09-30 01:29:52',26.01,0,1,3,7),(58,1,1,'2016-10-01 06:42:59','00:01:00','2016-10-01 06:43:59',17.85,1,NULL,3,NULL),(59,2,1,'2016-10-01 06:43:47','00:01:00','2016-10-01 06:44:47',38.25,1,NULL,3,NULL),(60,3,1,'2016-10-01 06:44:56','00:01:00','2016-10-01 06:45:56',4.5,1,NULL,3,NULL),(61,3,1,'2016-10-05 01:22:45','00:01:00','2016-10-05 01:23:45',4.5,1,NULL,3,NULL),(62,1,1,'2016-10-05 01:22:45','00:01:00','2016-10-05 01:23:45',17.85,1,NULL,3,NULL),(63,2,1,'2016-10-05 01:22:54','00:01:00','2016-10-05 01:23:54',38.25,1,NULL,3,NULL),(64,1,1,'2016-10-06 07:15:11','00:01:00','2016-10-06 07:16:11',17.85,1,NULL,3,NULL),(65,1,1,'2016-10-07 06:38:07','00:01:00','2016-10-07 06:39:07',17.85,1,NULL,2,NULL),(66,2,1,'2016-10-07 06:38:16','00:01:00','2016-10-07 06:39:16',38.25,1,NULL,2,NULL),(67,3,1,'2016-10-07 06:49:20','00:01:00','2016-10-07 06:50:20',4.5,1,NULL,2,NULL);
/*!40000 ALTER TABLE `williambid_subasta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `williambid_subastavendida`
--

DROP TABLE IF EXISTS `williambid_subastavendida`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `williambid_subastavendida` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `subasta_id` int(11) NOT NULL,
  `shoping_cart_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `subasta_id` (`subasta_id`),
  KEY `williambid_subastavendida_8806825e` (`shoping_cart_id`),
  CONSTRAINT `shoping_cart_id_refs_id_e2b38d65` FOREIGN KEY (`shoping_cart_id`) REFERENCES `williambid_shoppinggcart` (`id`),
  CONSTRAINT `subasta_id_refs_id_00fbc5ba` FOREIGN KEY (`subasta_id`) REFERENCES `williambid_subasta` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `williambid_subastavendida`
--

LOCK TABLES `williambid_subastavendida` WRITE;
/*!40000 ALTER TABLE `williambid_subastavendida` DISABLE KEYS */;
/*!40000 ALTER TABLE `williambid_subastavendida` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `williambid_tiposubasta`
--

DROP TABLE IF EXISTS `williambid_tiposubasta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `williambid_tiposubasta` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `descripcion` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `williambid_tiposubasta`
--

LOCK TABLES `williambid_tiposubasta` WRITE;
/*!40000 ALTER TABLE `williambid_tiposubasta` DISABLE KEYS */;
INSERT INTO `williambid_tiposubasta` VALUES (1,'Oportunity','Oportunity'),(2,'Hot Bid','Hot Bid'),(3,'Special','Special'),(4,'Premium','Premium');
/*!40000 ALTER TABLE `williambid_tiposubasta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `williambid_venta`
--

DROP TABLE IF EXISTS `williambid_venta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `williambid_venta` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `a_usuario` int(11) NOT NULL,
  `precio` double NOT NULL,
  `fecha_creacion` datetime NOT NULL,
  `en_red_de_usuario_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `williambid_venta_8d35d038` (`en_red_de_usuario_id`),
  CONSTRAINT `en_red_de_usuario_id_refs_id_44c2c06f` FOREIGN KEY (`en_red_de_usuario_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `williambid_venta`
--

LOCK TABLES `williambid_venta` WRITE;
/*!40000 ALTER TABLE `williambid_venta` DISABLE KEYS */;
/*!40000 ALTER TABLE `williambid_venta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `williambid_ventaarticulo`
--

DROP TABLE IF EXISTS `williambid_ventaarticulo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `williambid_ventaarticulo` (
  `venta_ptr_id` int(11) NOT NULL,
  `articulo_id` int(11) NOT NULL,
  PRIMARY KEY (`venta_ptr_id`),
  KEY `williambid_ventaarticulo_1818f191` (`articulo_id`),
  CONSTRAINT `articulo_id_refs_content_ptr_id_8c9c5971` FOREIGN KEY (`articulo_id`) REFERENCES `williambid_articulo` (`content_ptr_id`),
  CONSTRAINT `venta_ptr_id_refs_id_5dc41db1` FOREIGN KEY (`venta_ptr_id`) REFERENCES `williambid_venta` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `williambid_ventaarticulo`
--

LOCK TABLES `williambid_ventaarticulo` WRITE;
/*!40000 ALTER TABLE `williambid_ventaarticulo` DISABLE KEYS */;
/*!40000 ALTER TABLE `williambid_ventaarticulo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `williambid_ventapaquetebid`
--

DROP TABLE IF EXISTS `williambid_ventapaquetebid`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `williambid_ventapaquetebid` (
  `venta_ptr_id` int(11) NOT NULL,
  `paquete_id` int(11) NOT NULL,
  PRIMARY KEY (`venta_ptr_id`),
  KEY `williambid_ventapaquetebid_54ff6362` (`paquete_id`),
  CONSTRAINT `paquete_id_refs_content_ptr_id_07d50d3c` FOREIGN KEY (`paquete_id`) REFERENCES `williambid_paquetebid` (`content_ptr_id`),
  CONSTRAINT `venta_ptr_id_refs_id_06f9448a` FOREIGN KEY (`venta_ptr_id`) REFERENCES `williambid_venta` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `williambid_ventapaquetebid`
--

LOCK TABLES `williambid_ventapaquetebid` WRITE;
/*!40000 ALTER TABLE `williambid_ventapaquetebid` DISABLE KEYS */;
/*!40000 ALTER TABLE `williambid_ventapaquetebid` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-10-19  9:11:48
