/*
Navicat MySQL Data Transfer

Source Server         : MyHost
Source Server Version : 50630
Source Host           : localhost:3306
Source Database       : williambid

Target Server Type    : MYSQL
Target Server Version : 50630
File Encoding         : 65001

Date: 2017-02-20 23:22:52
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `auth_group`
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of auth_group
-- ----------------------------

-- ----------------------------
-- Table structure for `auth_group_permissions`
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
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

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for `auth_permission`
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_417f1b1c` (`content_type_id`),
  CONSTRAINT `auth_permissi_content_type_id_51277a81_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=107 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES ('1', 'Can add log entry', '1', 'add_logentry');
INSERT INTO `auth_permission` VALUES ('2', 'Can change log entry', '1', 'change_logentry');
INSERT INTO `auth_permission` VALUES ('3', 'Can delete log entry', '1', 'delete_logentry');
INSERT INTO `auth_permission` VALUES ('4', 'Can add permission', '2', 'add_permission');
INSERT INTO `auth_permission` VALUES ('5', 'Can change permission', '2', 'change_permission');
INSERT INTO `auth_permission` VALUES ('6', 'Can delete permission', '2', 'delete_permission');
INSERT INTO `auth_permission` VALUES ('7', 'Can add group', '3', 'add_group');
INSERT INTO `auth_permission` VALUES ('8', 'Can change group', '3', 'change_group');
INSERT INTO `auth_permission` VALUES ('9', 'Can delete group', '3', 'delete_group');
INSERT INTO `auth_permission` VALUES ('10', 'Can add user', '4', 'add_user');
INSERT INTO `auth_permission` VALUES ('11', 'Can change user', '4', 'change_user');
INSERT INTO `auth_permission` VALUES ('12', 'Can delete user', '4', 'delete_user');
INSERT INTO `auth_permission` VALUES ('13', 'Can add content type', '5', 'add_contenttype');
INSERT INTO `auth_permission` VALUES ('14', 'Can change content type', '5', 'change_contenttype');
INSERT INTO `auth_permission` VALUES ('15', 'Can delete content type', '5', 'delete_contenttype');
INSERT INTO `auth_permission` VALUES ('16', 'Can add session', '6', 'add_session');
INSERT INTO `auth_permission` VALUES ('17', 'Can change session', '6', 'change_session');
INSERT INTO `auth_permission` VALUES ('18', 'Can delete session', '6', 'delete_session');
INSERT INTO `auth_permission` VALUES ('19', 'Can add tipo subasta', '7', 'add_tiposubasta');
INSERT INTO `auth_permission` VALUES ('20', 'Can change tipo subasta', '7', 'change_tiposubasta');
INSERT INTO `auth_permission` VALUES ('21', 'Can delete tipo subasta', '7', 'delete_tiposubasta');
INSERT INTO `auth_permission` VALUES ('22', 'Can add content', '8', 'add_content');
INSERT INTO `auth_permission` VALUES ('23', 'Can change content', '8', 'change_content');
INSERT INTO `auth_permission` VALUES ('24', 'Can delete content', '8', 'delete_content');
INSERT INTO `auth_permission` VALUES ('25', 'Can edit untranslated fields', '8', 'can_edit_untranslated_fields_of_content');
INSERT INTO `auth_permission` VALUES ('26', 'Can add articulo', '9', 'add_articulo');
INSERT INTO `auth_permission` VALUES ('27', 'Can change articulo', '9', 'change_articulo');
INSERT INTO `auth_permission` VALUES ('28', 'Can delete articulo', '9', 'delete_articulo');
INSERT INTO `auth_permission` VALUES ('29', 'Can add paquete bid', '10', 'add_paquetebid');
INSERT INTO `auth_permission` VALUES ('30', 'Can change paquete bid', '10', 'change_paquetebid');
INSERT INTO `auth_permission` VALUES ('31', 'Can delete paquete bid', '10', 'delete_paquetebid');
INSERT INTO `auth_permission` VALUES ('32', 'Can add venta', '11', 'add_venta');
INSERT INTO `auth_permission` VALUES ('33', 'Can change venta', '11', 'change_venta');
INSERT INTO `auth_permission` VALUES ('34', 'Can delete venta', '11', 'delete_venta');
INSERT INTO `auth_permission` VALUES ('35', 'Can add venta articulo', '12', 'add_ventaarticulo');
INSERT INTO `auth_permission` VALUES ('36', 'Can change venta articulo', '12', 'change_ventaarticulo');
INSERT INTO `auth_permission` VALUES ('37', 'Can delete venta articulo', '12', 'delete_ventaarticulo');
INSERT INTO `auth_permission` VALUES ('38', 'Can add venta paquete bid', '13', 'add_ventapaquetebid');
INSERT INTO `auth_permission` VALUES ('39', 'Can change venta paquete bid', '13', 'change_ventapaquetebid');
INSERT INTO `auth_permission` VALUES ('40', 'Can delete venta paquete bid', '13', 'delete_ventapaquetebid');
INSERT INTO `auth_permission` VALUES ('41', 'Can add subasta', '14', 'add_subasta');
INSERT INTO `auth_permission` VALUES ('42', 'Can change subasta', '14', 'change_subasta');
INSERT INTO `auth_permission` VALUES ('43', 'Can delete subasta', '14', 'delete_subasta');
INSERT INTO `auth_permission` VALUES ('44', 'Can add robot', '15', 'add_robot');
INSERT INTO `auth_permission` VALUES ('45', 'Can change robot', '15', 'change_robot');
INSERT INTO `auth_permission` VALUES ('46', 'Can delete robot', '15', 'delete_robot');
INSERT INTO `auth_permission` VALUES ('47', 'Can add tipo membresia', '16', 'add_tipomembresia');
INSERT INTO `auth_permission` VALUES ('48', 'Can change tipo membresia', '16', 'change_tipomembresia');
INSERT INTO `auth_permission` VALUES ('49', 'Can delete tipo membresia', '16', 'delete_tipomembresia');
INSERT INTO `auth_permission` VALUES ('50', 'Can add membresia', '17', 'add_membresia');
INSERT INTO `auth_permission` VALUES ('51', 'Can change membresia', '17', 'change_membresia');
INSERT INTO `auth_permission` VALUES ('52', 'Can delete membresia', '17', 'delete_membresia');
INSERT INTO `auth_permission` VALUES ('53', 'Can add tipo usuario', '18', 'add_tipousuario');
INSERT INTO `auth_permission` VALUES ('54', 'Can change tipo usuario', '18', 'change_tipousuario');
INSERT INTO `auth_permission` VALUES ('55', 'Can delete tipo usuario', '18', 'delete_tipousuario');
INSERT INTO `auth_permission` VALUES ('56', 'Can add perfil usuario', '19', 'add_perfilusuario');
INSERT INTO `auth_permission` VALUES ('57', 'Can change perfil usuario', '19', 'change_perfilusuario');
INSERT INTO `auth_permission` VALUES ('58', 'Can delete perfil usuario', '19', 'delete_perfilusuario');
INSERT INTO `auth_permission` VALUES ('59', 'Can add banco usuario', '20', 'add_bancousuario');
INSERT INTO `auth_permission` VALUES ('60', 'Can change banco usuario', '20', 'change_bancousuario');
INSERT INTO `auth_permission` VALUES ('61', 'Can delete banco usuario', '20', 'delete_bancousuario');
INSERT INTO `auth_permission` VALUES ('62', 'Can add historial transacciones', '21', 'add_historialtransacciones');
INSERT INTO `auth_permission` VALUES ('63', 'Can change historial transacciones', '21', 'change_historialtransacciones');
INSERT INTO `auth_permission` VALUES ('64', 'Can delete historial transacciones', '21', 'delete_historialtransacciones');
INSERT INTO `auth_permission` VALUES ('65', 'Can add mensaje', '22', 'add_mensaje');
INSERT INTO `auth_permission` VALUES ('66', 'Can change mensaje', '22', 'change_mensaje');
INSERT INTO `auth_permission` VALUES ('67', 'Can delete mensaje', '22', 'delete_mensaje');
INSERT INTO `auth_permission` VALUES ('68', 'Can add invitacion', '23', 'add_invitacion');
INSERT INTO `auth_permission` VALUES ('69', 'Can change invitacion', '23', 'change_invitacion');
INSERT INTO `auth_permission` VALUES ('70', 'Can delete invitacion', '23', 'delete_invitacion');
INSERT INTO `auth_permission` VALUES ('71', 'Can add tipo reto', '24', 'add_tiporeto');
INSERT INTO `auth_permission` VALUES ('72', 'Can change tipo reto', '24', 'change_tiporeto');
INSERT INTO `auth_permission` VALUES ('73', 'Can delete tipo reto', '24', 'delete_tiporeto');
INSERT INTO `auth_permission` VALUES ('74', 'Can add reto', '25', 'add_reto');
INSERT INTO `auth_permission` VALUES ('75', 'Can change reto', '25', 'change_reto');
INSERT INTO `auth_permission` VALUES ('76', 'Can delete reto', '25', 'delete_reto');
INSERT INTO `auth_permission` VALUES ('77', 'Can add estado reto usuario', '26', 'add_estadoretousuario');
INSERT INTO `auth_permission` VALUES ('78', 'Can change estado reto usuario', '26', 'change_estadoretousuario');
INSERT INTO `auth_permission` VALUES ('79', 'Can delete estado reto usuario', '26', 'delete_estadoretousuario');
INSERT INTO `auth_permission` VALUES ('80', 'Can add plan compensacion', '27', 'add_plancompensacion');
INSERT INTO `auth_permission` VALUES ('81', 'Can change plan compensacion', '27', 'change_plancompensacion');
INSERT INTO `auth_permission` VALUES ('82', 'Can delete plan compensacion', '27', 'delete_plancompensacion');
INSERT INTO `auth_permission` VALUES ('83', 'Can add beneficios', '28', 'add_beneficios');
INSERT INTO `auth_permission` VALUES ('84', 'Can change beneficios', '28', 'change_beneficios');
INSERT INTO `auth_permission` VALUES ('85', 'Can delete beneficios', '28', 'delete_beneficios');
INSERT INTO `auth_permission` VALUES ('86', 'Can add advertisement tool', '29', 'add_advertisementtool');
INSERT INTO `auth_permission` VALUES ('87', 'Can change advertisement tool', '29', 'change_advertisementtool');
INSERT INTO `auth_permission` VALUES ('88', 'Can delete advertisement tool', '29', 'delete_advertisementtool');
INSERT INTO `auth_permission` VALUES ('89', 'Can add auto puja', '30', 'add_autopuja');
INSERT INTO `auth_permission` VALUES ('90', 'Can change auto puja', '30', 'change_autopuja');
INSERT INTO `auth_permission` VALUES ('91', 'Can delete auto puja', '30', 'delete_autopuja');
INSERT INTO `auth_permission` VALUES ('92', 'Can add shoppingg cart', '31', 'add_shoppinggcart');
INSERT INTO `auth_permission` VALUES ('93', 'Can change shoppingg cart', '31', 'change_shoppinggcart');
INSERT INTO `auth_permission` VALUES ('94', 'Can delete shoppingg cart', '31', 'delete_shoppinggcart');
INSERT INTO `auth_permission` VALUES ('95', 'Can add subasta vendida', '32', 'add_subastavendida');
INSERT INTO `auth_permission` VALUES ('96', 'Can change subasta vendida', '32', 'change_subastavendida');
INSERT INTO `auth_permission` VALUES ('97', 'Can delete subasta vendida', '32', 'delete_subastavendida');
INSERT INTO `auth_permission` VALUES ('98', 'Can add PayPal IPN', '33', 'add_paypalipn');
INSERT INTO `auth_permission` VALUES ('99', 'Can change PayPal IPN', '33', 'change_paypalipn');
INSERT INTO `auth_permission` VALUES ('100', 'Can delete PayPal IPN', '33', 'delete_paypalipn');
INSERT INTO `auth_permission` VALUES ('101', 'Can add user x delivered profit', '34', 'add_userxdeliveredprofit');
INSERT INTO `auth_permission` VALUES ('102', 'Can change user x delivered profit', '34', 'change_userxdeliveredprofit');
INSERT INTO `auth_permission` VALUES ('103', 'Can delete user x delivered profit', '34', 'delete_userxdeliveredprofit');
INSERT INTO `auth_permission` VALUES ('104', 'Can add william paypal transaction', '35', 'add_williampaypaltransaction');
INSERT INTO `auth_permission` VALUES ('105', 'Can change william paypal transaction', '35', 'change_williampaypaltransaction');
INSERT INTO `auth_permission` VALUES ('106', 'Can delete william paypal transaction', '35', 'delete_williampaypaltransaction');

-- ----------------------------
-- Table structure for `auth_user`
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
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
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of auth_user
-- ----------------------------
INSERT INTO `auth_user` VALUES ('1', 'pbkdf2_sha256$12000$55W34OMevFJT$6F4Z4uU7ev8QL/R+dn/1C+KHOsatKqy/3Y0jwNyrzhQ=', '2017-02-18 15:29:38', '1', 'admin', '', '', 'admin@uci.cu', '1', '1', '2016-05-07 23:49:32');
INSERT INTO `auth_user` VALUES ('7', 'pbkdf2_sha256$12000$55W34OMevFJT$6F4Z4uU7ev8QL/R+dn/1C+KHOsatKqy/3Y0jwNyrzhQ=', '2016-11-22 16:20:34', '0', 'addiaz', '', '', 'addiaz@uci.cu', '0', '1', '2016-05-09 23:20:06');
INSERT INTO `auth_user` VALUES ('8', '', '2016-09-28 23:59:57', '0', 'rulico', '', '', '', '0', '1', '2016-09-28 23:59:57');
INSERT INTO `auth_user` VALUES ('9', '', '2016-09-29 00:00:06', '0', 'kavitat', '', '', '', '0', '1', '2016-09-29 00:00:06');
INSERT INTO `auth_user` VALUES ('10', '', '2016-09-29 00:00:16', '0', 'lememu', '', '', '', '0', '1', '2016-09-29 00:00:16');
INSERT INTO `auth_user` VALUES ('11', '', '2016-09-29 00:00:26', '0', 'virure', '', '', '', '0', '1', '2016-09-29 00:00:26');
INSERT INTO `auth_user` VALUES ('12', '', '2016-09-29 00:00:36', '0', 'jigaki', '', '', '', '0', '1', '2016-09-29 00:00:36');
INSERT INTO `auth_user` VALUES ('13', 'pbkdf2_sha256$12000$OCMGc0KgId27$EqKhh0n5rG6x1OchUzeL8NwvTdJM/1ZivP2yIgsw+QA=', '2016-09-30 20:13:47', '0', 'briseida', '', '', 'briseida.bussott@nauta.cu', '0', '1', '2016-09-30 20:13:47');
INSERT INTO `auth_user` VALUES ('14', '', '2016-11-22 16:19:53', '0', 'dadumih', '', '', '', '0', '1', '2016-11-22 16:19:53');
INSERT INTO `auth_user` VALUES ('15', '', '2016-11-22 16:20:02', '0', 'hevuf', '', '', '', '0', '1', '2016-11-22 16:20:02');
INSERT INTO `auth_user` VALUES ('16', '', '2016-11-22 16:20:12', '0', 'befatag', '', '', '', '0', '1', '2016-11-22 16:20:12');
INSERT INTO `auth_user` VALUES ('17', '', '2016-11-22 16:20:22', '0', 'jikudo', '', '', '', '0', '1', '2016-11-22 16:20:22');
INSERT INTO `auth_user` VALUES ('18', '', '2016-11-22 16:20:32', '0', 'gejemic', '', '', '', '0', '1', '2016-11-22 16:20:32');

-- ----------------------------
-- Table structure for `auth_user_groups`
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
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

-- ----------------------------
-- Records of auth_user_groups
-- ----------------------------

-- ----------------------------
-- Table structure for `auth_user_user_permissions`
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
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

-- ----------------------------
-- Records of auth_user_user_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for `back_office_advertisementtool`
-- ----------------------------
DROP TABLE IF EXISTS `back_office_advertisementtool`;
CREATE TABLE `back_office_advertisementtool` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(200) NOT NULL,
  `description` longtext NOT NULL,
  `tool_file` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of back_office_advertisementtool
-- ----------------------------

-- ----------------------------
-- Table structure for `back_office_bancousuario`
-- ----------------------------
DROP TABLE IF EXISTS `back_office_bancousuario`;
CREATE TABLE `back_office_bancousuario` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `usuario_id` int(11) NOT NULL,
  `tipo_plan` int(11) NOT NULL,
  `monto_total` double NOT NULL,
  PRIMARY KEY (`id`),
  KEY `back_office_bancousuario_c69e2c81` (`usuario_id`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of back_office_bancousuario
-- ----------------------------
INSERT INTO `back_office_bancousuario` VALUES ('19', '1', '4', '48');
INSERT INTO `back_office_bancousuario` VALUES ('20', '13', '4', '15.4');
INSERT INTO `back_office_bancousuario` VALUES ('21', '7', '4', '24');
INSERT INTO `back_office_bancousuario` VALUES ('22', '1', '12', '115.832');
INSERT INTO `back_office_bancousuario` VALUES ('23', '8', '4', '17.2');
INSERT INTO `back_office_bancousuario` VALUES ('24', '9', '4', '8.6');
INSERT INTO `back_office_bancousuario` VALUES ('25', '10', '4', '8.6');
INSERT INTO `back_office_bancousuario` VALUES ('26', '11', '4', '8.6');
INSERT INTO `back_office_bancousuario` VALUES ('27', '12', '4', '8.6');
INSERT INTO `back_office_bancousuario` VALUES ('28', '8', '2', '9.03');
INSERT INTO `back_office_bancousuario` VALUES ('29', '1', '14', '6.622');

-- ----------------------------
-- Table structure for `back_office_beneficios`
-- ----------------------------
DROP TABLE IF EXISTS `back_office_beneficios`;
CREATE TABLE `back_office_beneficios` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `beneficio_total_empresa` int(11) NOT NULL,
  `beneficio_total_empresa_socios_VIP_PRO` int(11) NOT NULL,
  `facturacion_global` int(11) NOT NULL,
  `distribuido` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of back_office_beneficios
-- ----------------------------

-- ----------------------------
-- Table structure for `back_office_estadoretousuario`
-- ----------------------------
DROP TABLE IF EXISTS `back_office_estadoretousuario`;
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

-- ----------------------------
-- Records of back_office_estadoretousuario
-- ----------------------------

-- ----------------------------
-- Table structure for `back_office_historialtransacciones`
-- ----------------------------
DROP TABLE IF EXISTS `back_office_historialtransacciones`;
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

-- ----------------------------
-- Records of back_office_historialtransacciones
-- ----------------------------

-- ----------------------------
-- Table structure for `back_office_invitacion`
-- ----------------------------
DROP TABLE IF EXISTS `back_office_invitacion`;
CREATE TABLE `back_office_invitacion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `de_usuario_id` int(11) NOT NULL,
  `para` varchar(50) NOT NULL,
  `para_correo` varchar(75) NOT NULL,
  `url` varchar(200) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `back_office_invitacion_2db5027c` (`de_usuario_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of back_office_invitacion
-- ----------------------------

-- ----------------------------
-- Table structure for `back_office_membresia`
-- ----------------------------
DROP TABLE IF EXISTS `back_office_membresia`;
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

-- ----------------------------
-- Records of back_office_membresia
-- ----------------------------
INSERT INTO `back_office_membresia` VALUES ('1', '1', '0', '0', '1', '0');
INSERT INTO `back_office_membresia` VALUES ('2', '2', '10', '1', '1', '10');
INSERT INTO `back_office_membresia` VALUES ('3', '3', '25', '1', '1', '20');
INSERT INTO `back_office_membresia` VALUES ('4', '4', '50', '1', '1', '30');
INSERT INTO `back_office_membresia` VALUES ('5', '5', '100', '1', '1', '50');
INSERT INTO `back_office_membresia` VALUES ('6', '6', '250', '1', '1', '100');
INSERT INTO `back_office_membresia` VALUES ('7', '7', '500', '1', '1', '150');
INSERT INTO `back_office_membresia` VALUES ('8', '8', '1000', '1', '1', '300');
INSERT INTO `back_office_membresia` VALUES ('9', '9', '2000', '1', '1', '500');

-- ----------------------------
-- Table structure for `back_office_mensaje`
-- ----------------------------
DROP TABLE IF EXISTS `back_office_mensaje`;
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

-- ----------------------------
-- Records of back_office_mensaje
-- ----------------------------
INSERT INTO `back_office_mensaje` VALUES ('1', '1', '7', 'Mensaje de prueba', '1', '2016-09-27 20:58:01');

-- ----------------------------
-- Table structure for `back_office_perfilusuario`
-- ----------------------------
DROP TABLE IF EXISTS `back_office_perfilusuario`;
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
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of back_office_perfilusuario
-- ----------------------------
INSERT INTO `back_office_perfilusuario` VALUES ('1', '1', null, '8', '9', '2017-01-31 03:08:13', 'Test Dir', 'Gtmo', 'Gtmo', 'Cuba', '054232332', 'Admin', 'adminwhatsapp', 'adminskype', '41', '936');
INSERT INTO `back_office_perfilusuario` VALUES ('7', '7', '1', '1', '1', '2017-01-31 03:08:13', 'Calle5', 'Gtmo', 'Gtmo', 'Cuba', '054232332', 'lcol88', 'assdfdf', 'dsfsdf', '1', '3');
INSERT INTO `back_office_perfilusuario` VALUES ('8', '8', '1', '1', '3', '2017-01-31 03:08:13', '', '', '', '', '', 'rulico', '', '', '50', '0');
INSERT INTO `back_office_perfilusuario` VALUES ('9', '9', '1', '1', '2', '2017-01-31 03:08:13', '', '', '', '', '', 'kavitat', '', '', '20', '0');
INSERT INTO `back_office_perfilusuario` VALUES ('10', '10', '1', '1', '2', '2016-09-29 00:05:01', '', '', '', '', '', 'lememu', '', '', '0', '0');
INSERT INTO `back_office_perfilusuario` VALUES ('11', '11', '8', '1', '5', '2016-09-29 00:05:01', '', '', '', '', '', 'virure', '', '', '0', '0');
INSERT INTO `back_office_perfilusuario` VALUES ('12', '12', '9', '1', '3', '2016-09-29 00:05:01', '', '', '', '', '', 'jigaki', '', '', '0', '0');
INSERT INTO `back_office_perfilusuario` VALUES ('13', '13', '7', '1', '1', '2016-09-30 20:14:08', 'Calle5', 'Gtmo', 'Gtmo', 'Cuba', '054232332', 'brissi', 'asdsad', 'dasdasd', '0', '0');
INSERT INTO `back_office_perfilusuario` VALUES ('14', '14', '1', '8', '9', '2016-11-22 16:19:53', '', '', '', '', '', 'dadumih', '', '', '0', '0');
INSERT INTO `back_office_perfilusuario` VALUES ('15', '15', '12', '7', '8', '2016-11-22 16:20:02', '', '', '', '', '', 'hevuf', '', '', '0', '0');
INSERT INTO `back_office_perfilusuario` VALUES ('16', '16', '9', '5', '2', '2016-11-22 16:20:12', '', '', '', '', '', 'befatag', '', '', '0', '0');
INSERT INTO `back_office_perfilusuario` VALUES ('17', '17', '12', '5', '1', '2016-11-22 16:20:22', '', '', '', '', '', 'jikudo', '', '', '0', '0');
INSERT INTO `back_office_perfilusuario` VALUES ('18', '18', '12', '5', '3', '2016-11-22 16:20:32', '', '', '', '', '', 'gejemic', '', '', '0', '0');

-- ----------------------------
-- Table structure for `back_office_plancompensacion`
-- ----------------------------
DROP TABLE IF EXISTS `back_office_plancompensacion`;
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

-- ----------------------------
-- Records of back_office_plancompensacion
-- ----------------------------
INSERT INTO `back_office_plancompensacion` VALUES ('1', '1', 'MEMBRESIAS EN LA RED 2,4,6,10,15,20', '1', '1', '1', '0', '0', '0', 'MEMBRESIAS EN LA RED 2,4,6,10,15,20');
INSERT INTO `back_office_plancompensacion` VALUES ('2', '2', 'BINARIO HIBRIDO', '1', '1', '2', '2', '0', '50', 'BINARIO HIBRIDO');
INSERT INTO `back_office_plancompensacion` VALUES ('3', '3', 'PLAN UNILEVEL DE VENTA DIRECTA DE PUJAS', '1', '1', '1', '0', '0', '0', 'PLAN UNILEVEL DE VENTA DIRECTA DE PUJAS');
INSERT INTO `back_office_plancompensacion` VALUES ('4', '4', 'BINARIO POR DERRAME EMPRESA MENSUAL', '1', '1', '2', '0', '0', '0', 'BINARIO POR DERRAME EMPRESA MENSUAL');
INSERT INTO `back_office_plancompensacion` VALUES ('5', '5', 'BONOS DE LOGRO (RETOS)', '1', '1', '1', '0', '0', '0', 'BONOS DE LOGRO (RETOS)');
INSERT INTO `back_office_plancompensacion` VALUES ('6', '6', 'BENEFICIO A MEMBRESIAS DE PAGO', '1', '1', '2', '0', '0', '0', 'BENEFICIO A MEMBRESIAS DE PAGO');
INSERT INTO `back_office_plancompensacion` VALUES ('7', '7', 'BENEFICIO VIP Y VIP WINNER', '1', '1', '8', '0', '0', '0', 'BENEFICIO VIP Y VIP WINNER');
INSERT INTO `back_office_plancompensacion` VALUES ('8', '8', 'FONDO GLOBAL DE LIDERAZGO', '1', '1', '1', '0', '100000', '0', 'FONDO GLOBAL DE LIDERAZGO');
INSERT INTO `back_office_plancompensacion` VALUES ('9', '9', 'BONO 1000', '1', '1', '1', '0', '20000', '0', 'BONO 1000');
INSERT INTO `back_office_plancompensacion` VALUES ('10', '10', 'BONO 31', '1', '1', '1', '0', '15000', '0', 'BONO 31');
INSERT INTO `back_office_plancompensacion` VALUES ('11', '11', 'PLAN DE AUTOENRIQUECIMIENTO\r\n', '1', '1', '1', '0', '0', '0', 'PLAN DE AUTOENRIQUECIMIENTO\r\n');
INSERT INTO `back_office_plancompensacion` VALUES ('12', '12', 'BONO DE IGUALACIÓN EN LA RED 2,4,6,10,15', '1', '4', '1', '0', '0', '0', 'BONO DE IGUALACIÓN EN LA RED 2,4,6,10,15');
INSERT INTO `back_office_plancompensacion` VALUES ('13', '13', 'BONO DE IGUALACIÓN PLAN UNILEVEL', '1', '4', '1', '0', '0', '0', 'BONO DE IGUALACIÓN PLAN UNILEVEL');
INSERT INTO `back_office_plancompensacion` VALUES ('14', '14', 'BONO DE IGUALACIÓN DEL BINARIO HIBRIDO', '1', '4', '1', '0', '0', '0', 'BONO DE IGUALACIÓN DEL BINARIO HIBRIDO');

-- ----------------------------
-- Table structure for `back_office_reto`
-- ----------------------------
DROP TABLE IF EXISTS `back_office_reto`;
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

-- ----------------------------
-- Records of back_office_reto
-- ----------------------------
INSERT INTO `back_office_reto` VALUES ('1', '1', '30', '4', '2016-05-20 00:00:00', '0', '40', '1', '0');
INSERT INTO `back_office_reto` VALUES ('2', '2', null, '5', '2016-05-18 00:00:00', '0', '70', '1', '0');

-- ----------------------------
-- Table structure for `back_office_tipomembresia`
-- ----------------------------
DROP TABLE IF EXISTS `back_office_tipomembresia`;
CREATE TABLE `back_office_tipomembresia` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of back_office_tipomembresia
-- ----------------------------
INSERT INTO `back_office_tipomembresia` VALUES ('1', 'Free');
INSERT INTO `back_office_tipomembresia` VALUES ('2', 'Junior');
INSERT INTO `back_office_tipomembresia` VALUES ('3', 'Amateur');
INSERT INTO `back_office_tipomembresia` VALUES ('4', 'Semi-Profesional');
INSERT INTO `back_office_tipomembresia` VALUES ('5', 'Profesional');
INSERT INTO `back_office_tipomembresia` VALUES ('6', 'Player');
INSERT INTO `back_office_tipomembresia` VALUES ('7', 'Player-Pro');
INSERT INTO `back_office_tipomembresia` VALUES ('8', 'VIP');
INSERT INTO `back_office_tipomembresia` VALUES ('9', 'VIP Winner');

-- ----------------------------
-- Table structure for `back_office_tiporeto`
-- ----------------------------
DROP TABLE IF EXISTS `back_office_tiporeto`;
CREATE TABLE `back_office_tiporeto` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `descripcion` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of back_office_tiporeto
-- ----------------------------
INSERT INTO `back_office_tiporeto` VALUES ('1', 'Si consigues registrar a un total de X personas con membresias X antes de XFecha ganaras X $');
INSERT INTO `back_office_tiporeto` VALUES ('2', 'Si consigues hacer que los usuarios de tu primera generacion pasen a una membresia X antes de XFecha ganaras X $');
INSERT INTO `back_office_tiporeto` VALUES ('3', 'Si consigues vender X dinero en pujas, ganaras X $');

-- ----------------------------
-- Table structure for `back_office_tipousuario`
-- ----------------------------
DROP TABLE IF EXISTS `back_office_tipousuario`;
CREATE TABLE `back_office_tipousuario` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of back_office_tipousuario
-- ----------------------------
INSERT INTO `back_office_tipousuario` VALUES ('1', 'Team Trainer');
INSERT INTO `back_office_tipousuario` VALUES ('2', 'Team Leader');
INSERT INTO `back_office_tipousuario` VALUES ('3', 'Team Coordinator');
INSERT INTO `back_office_tipousuario` VALUES ('4', 'National Director');
INSERT INTO `back_office_tipousuario` VALUES ('5', 'International Director');
INSERT INTO `back_office_tipousuario` VALUES ('6', 'National Vicepresident');
INSERT INTO `back_office_tipousuario` VALUES ('7', 'International Vicepresident');
INSERT INTO `back_office_tipousuario` VALUES ('8', 'Team President');

-- ----------------------------
-- Table structure for `back_office_userxdeliveredprofit`
-- ----------------------------
DROP TABLE IF EXISTS `back_office_userxdeliveredprofit`;
CREATE TABLE `back_office_userxdeliveredprofit` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of back_office_userxdeliveredprofit
-- ----------------------------
INSERT INTO `back_office_userxdeliveredprofit` VALUES ('1', '2016-10-25 13:00:51');
INSERT INTO `back_office_userxdeliveredprofit` VALUES ('2', '2016-10-25 13:01:00');
INSERT INTO `back_office_userxdeliveredprofit` VALUES ('3', '2016-11-22 16:15:47');
INSERT INTO `back_office_userxdeliveredprofit` VALUES ('4', '2017-01-31 03:08:14');

-- ----------------------------
-- Table structure for `back_office_williampaypaltransaction`
-- ----------------------------
DROP TABLE IF EXISTS `back_office_williampaypaltransaction`;
CREATE TABLE `back_office_williampaypaltransaction` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `amount` double NOT NULL,
  PRIMARY KEY (`id`),
  KEY `back_office_williampaypaltransaction_6340c63c` (`user_id`),
  CONSTRAINT `user_id_refs_id_bb9aad5e` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of back_office_williampaypaltransaction
-- ----------------------------

-- ----------------------------
-- Table structure for `django_admin_log`
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
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
) ENGINE=InnoDB AUTO_INCREMENT=44 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------
INSERT INTO `django_admin_log` VALUES ('1', '2016-05-08 01:05:27', '1', 'Plan de compensacion: 1', '1', '', '27', '1');
INSERT INTO `django_admin_log` VALUES ('2', '2016-05-08 01:06:44', '2', 'Plan de compensacion: 2', '1', '', '27', '1');
INSERT INTO `django_admin_log` VALUES ('3', '2016-05-08 01:07:57', '3', 'Plan de compensacion: 3', '1', '', '27', '1');
INSERT INTO `django_admin_log` VALUES ('4', '2016-05-08 01:08:18', '4', 'Plan de compensacion: 4', '1', '', '27', '1');
INSERT INTO `django_admin_log` VALUES ('5', '2016-05-08 01:09:41', '5', 'Plan de compensacion: 5', '1', '', '27', '1');
INSERT INTO `django_admin_log` VALUES ('6', '2016-05-08 01:12:49', '6', 'Plan de compensacion: 6', '1', '', '27', '1');
INSERT INTO `django_admin_log` VALUES ('7', '2016-05-08 01:13:21', '7', 'Plan de compensacion: 7', '1', '', '27', '1');
INSERT INTO `django_admin_log` VALUES ('8', '2016-05-08 01:14:03', '8', 'Plan de compensacion: 8', '1', '', '27', '1');
INSERT INTO `django_admin_log` VALUES ('9', '2016-05-08 01:14:52', '9', 'Plan de compensacion: 9', '1', '', '27', '1');
INSERT INTO `django_admin_log` VALUES ('10', '2016-05-08 01:15:17', '10', 'Plan de compensacion: 10', '1', '', '27', '1');
INSERT INTO `django_admin_log` VALUES ('11', '2016-05-08 01:15:31', '11', 'Plan de compensacion: 11', '1', '', '27', '1');
INSERT INTO `django_admin_log` VALUES ('12', '2016-05-08 01:16:39', '12', 'Plan de compensacion: 12', '1', '', '27', '1');
INSERT INTO `django_admin_log` VALUES ('13', '2016-05-08 01:16:51', '13', 'Plan de compensacion: 13', '1', '', '27', '1');
INSERT INTO `django_admin_log` VALUES ('14', '2016-05-08 01:17:21', '14', 'Plan de compensacion: 14', '1', '', '27', '1');
INSERT INTO `django_admin_log` VALUES ('15', '2016-05-08 01:18:07', '13', 'Plan de compensacion: 13', '2', 'Modificado/a tipo_usuario.', '27', '1');
INSERT INTO `django_admin_log` VALUES ('16', '2016-05-08 01:18:15', '12', 'Plan de compensacion: 12', '2', 'Modificado/a tipo_usuario.', '27', '1');
INSERT INTO `django_admin_log` VALUES ('17', '2016-05-08 14:54:03', '9', 'Plan de compensacion: 9', '2', 'Modificado/a cantidad_de_dinero.', '27', '1');
INSERT INTO `django_admin_log` VALUES ('18', '2016-05-08 14:54:24', '10', 'Plan de compensacion: 10', '2', 'Modificado/a cantidad_de_dinero.', '27', '1');
INSERT INTO `django_admin_log` VALUES ('19', '2016-05-08 14:58:54', '10', 'Plan de compensacion: 10', '2', 'Modificado/a descripcion.', '27', '1');
INSERT INTO `django_admin_log` VALUES ('20', '2016-05-08 14:59:05', '9', 'Plan de compensacion: 9', '2', 'Modificado/a descripcion.', '27', '1');
INSERT INTO `django_admin_log` VALUES ('21', '2016-05-08 14:59:14', '8', 'Plan de compensacion: 8', '2', 'Modificado/a descripcion.', '27', '1');
INSERT INTO `django_admin_log` VALUES ('22', '2016-05-08 15:00:02', '7', 'Plan de compensacion: 7', '2', 'Modificado/a descripcion.', '27', '1');
INSERT INTO `django_admin_log` VALUES ('23', '2016-05-08 15:00:35', '6', 'Plan de compensacion: 6', '2', 'Modificado/a descripcion.', '27', '1');
INSERT INTO `django_admin_log` VALUES ('24', '2016-05-08 15:00:39', '5', 'Plan de compensacion: 5', '2', 'No ha cambiado ningún campo.', '27', '1');
INSERT INTO `django_admin_log` VALUES ('25', '2016-05-08 15:01:03', '1', 'Plan de compensacion: 1', '2', 'Modificado/a descripcion.', '27', '1');
INSERT INTO `django_admin_log` VALUES ('26', '2016-05-08 15:15:39', '7', 'Plan de compensacion: 7', '2', 'Modificado/a descripcion.', '27', '1');
INSERT INTO `django_admin_log` VALUES ('27', '2016-05-10 01:56:11', '1', 'AdvertisementTool object', '1', '', '29', '1');
INSERT INTO `django_admin_log` VALUES ('28', '2016-05-10 02:13:38', '1', 'Si consigues registrar a un total de X personas con membresias X antes de XFecha ganaras X $', '1', '', '25', '1');
INSERT INTO `django_admin_log` VALUES ('29', '2016-05-10 02:15:11', '2', 'Si consigues hacer que los usuarios de tu primera generacion pasen a una membresia X antes de XFecha ganaras X $', '1', '', '25', '1');
INSERT INTO `django_admin_log` VALUES ('30', '2016-08-24 21:32:41', '1', 'Pullas', '1', '', '9', '1');
INSERT INTO `django_admin_log` VALUES ('31', '2016-08-24 22:03:43', '1', 'Pullas', '1', '', '9', '1');
INSERT INTO `django_admin_log` VALUES ('32', '2016-08-25 12:01:02', '2', 'Tennis', '1', '', '9', '1');
INSERT INTO `django_admin_log` VALUES ('33', '2016-08-25 13:24:45', '3', '30, 5.0', '1', '', '10', '1');
INSERT INTO `django_admin_log` VALUES ('34', '2016-09-30 00:29:43', '4', 'Chair', '1', '', '9', '1');
INSERT INTO `django_admin_log` VALUES ('35', '2016-09-30 00:46:14', '50', 'Subasta de Chair', '1', '', '14', '1');
INSERT INTO `django_admin_log` VALUES ('36', '2016-09-30 00:51:12', '51', 'Subasta de Chair', '1', '', '14', '1');
INSERT INTO `django_admin_log` VALUES ('37', '2016-09-30 01:03:40', '52', 'Subasta de Chair', '1', '', '14', '1');
INSERT INTO `django_admin_log` VALUES ('38', '2016-09-30 01:12:00', '53', 'Subasta de Chair', '1', '', '14', '1');
INSERT INTO `django_admin_log` VALUES ('39', '2016-09-30 01:12:28', '54', 'Subasta de Chair', '1', '', '14', '1');
INSERT INTO `django_admin_log` VALUES ('40', '2016-09-30 01:21:23', '55', 'Subasta de Chair', '1', '', '14', '1');
INSERT INTO `django_admin_log` VALUES ('41', '2016-09-30 01:25:48', '56', 'Subasta de Chair', '1', '', '14', '1');
INSERT INTO `django_admin_log` VALUES ('42', '2016-09-30 01:28:41', '57', 'Subasta de Chair', '1', '', '14', '1');
INSERT INTO `django_admin_log` VALUES ('43', '2016-11-23 17:29:17', '1', '30, 1.0', '1', '', '10', '1');

-- ----------------------------
-- Table structure for `django_content_type`
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_3ec8c61c_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES ('1', 'log entry', 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES ('2', 'permission', 'auth', 'permission');
INSERT INTO `django_content_type` VALUES ('3', 'group', 'auth', 'group');
INSERT INTO `django_content_type` VALUES ('4', 'user', 'auth', 'user');
INSERT INTO `django_content_type` VALUES ('5', 'content type', 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES ('6', 'session', 'sessions', 'session');
INSERT INTO `django_content_type` VALUES ('7', 'tipo subasta', 'williambid', 'tiposubasta');
INSERT INTO `django_content_type` VALUES ('8', 'content', 'williambid', 'content');
INSERT INTO `django_content_type` VALUES ('9', 'articulo', 'williambid', 'articulo');
INSERT INTO `django_content_type` VALUES ('10', 'paquete bid', 'williambid', 'paquetebid');
INSERT INTO `django_content_type` VALUES ('11', 'venta', 'williambid', 'venta');
INSERT INTO `django_content_type` VALUES ('12', 'venta articulo', 'williambid', 'ventaarticulo');
INSERT INTO `django_content_type` VALUES ('13', 'venta paquete bid', 'williambid', 'ventapaquetebid');
INSERT INTO `django_content_type` VALUES ('14', 'subasta', 'williambid', 'subasta');
INSERT INTO `django_content_type` VALUES ('15', 'robot', 'williambid', 'robot');
INSERT INTO `django_content_type` VALUES ('16', 'tipo membresia', 'back_office', 'tipomembresia');
INSERT INTO `django_content_type` VALUES ('17', 'membresia', 'back_office', 'membresia');
INSERT INTO `django_content_type` VALUES ('18', 'tipo usuario', 'back_office', 'tipousuario');
INSERT INTO `django_content_type` VALUES ('19', 'perfil usuario', 'back_office', 'perfilusuario');
INSERT INTO `django_content_type` VALUES ('20', 'banco usuario', 'back_office', 'bancousuario');
INSERT INTO `django_content_type` VALUES ('21', 'historial transacciones', 'back_office', 'historialtransacciones');
INSERT INTO `django_content_type` VALUES ('22', 'mensaje', 'back_office', 'mensaje');
INSERT INTO `django_content_type` VALUES ('23', 'invitacion', 'back_office', 'invitacion');
INSERT INTO `django_content_type` VALUES ('24', 'tipo reto', 'back_office', 'tiporeto');
INSERT INTO `django_content_type` VALUES ('25', 'reto', 'back_office', 'reto');
INSERT INTO `django_content_type` VALUES ('26', 'estado reto usuario', 'back_office', 'estadoretousuario');
INSERT INTO `django_content_type` VALUES ('27', 'plan compensacion', 'back_office', 'plancompensacion');
INSERT INTO `django_content_type` VALUES ('28', 'beneficios', 'back_office', 'beneficios');
INSERT INTO `django_content_type` VALUES ('29', 'advertisement tool', 'back_office', 'advertisementtool');
INSERT INTO `django_content_type` VALUES ('30', 'auto puja', 'williambid', 'autopuja');
INSERT INTO `django_content_type` VALUES ('31', 'shoppingg cart', 'williambid', 'shoppinggcart');
INSERT INTO `django_content_type` VALUES ('32', 'subasta vendida', 'williambid', 'subastavendida');
INSERT INTO `django_content_type` VALUES ('33', 'PayPal IPN', 'ipn', 'paypalipn');
INSERT INTO `django_content_type` VALUES ('34', 'user x delivered profit', 'back_office', 'userxdeliveredprofit');
INSERT INTO `django_content_type` VALUES ('35', 'william paypal transaction', 'back_office', 'williampaypaltransaction');

-- ----------------------------
-- Table structure for `django_migrations`
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES ('1', 'contenttypes', '0001_initial', '2016-10-22 01:00:33');
INSERT INTO `django_migrations` VALUES ('2', 'auth', '0001_initial', '2016-10-22 01:00:33');
INSERT INTO `django_migrations` VALUES ('3', 'admin', '0001_initial', '2016-10-22 01:00:33');
INSERT INTO `django_migrations` VALUES ('4', 'ipn', '0001_initial', '2016-10-22 01:00:34');
INSERT INTO `django_migrations` VALUES ('5', 'ipn', '0002_paypalipn_mp_id', '2016-10-22 01:00:34');
INSERT INTO `django_migrations` VALUES ('6', 'ipn', '0003_auto_20141117_1647', '2016-10-22 01:00:35');
INSERT INTO `django_migrations` VALUES ('7', 'ipn', '0004_auto_20150612_1826', '2016-10-22 01:00:51');
INSERT INTO `django_migrations` VALUES ('8', 'ipn', '0005_auto_20151217_0948', '2016-10-22 01:00:52');
INSERT INTO `django_migrations` VALUES ('9', 'ipn', '0006_auto_20160108_1112', '2016-10-22 01:00:54');
INSERT INTO `django_migrations` VALUES ('10', 'ipn', '0007_auto_20160219_1135', '2016-10-22 01:00:54');
INSERT INTO `django_migrations` VALUES ('11', 'sessions', '0001_initial', '2016-10-22 01:00:54');

-- ----------------------------
-- Table structure for `django_session`
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO `django_session` VALUES ('06d5lf9tdlw652vhj4em29s496otk3gd', 'YTIzMmMxNjljZTk4ZmI1MDdhYzFhMjhiYjAyMmY0ODczYWFmNjEyNzp7fQ==', '2016-09-09 13:31:56');
INSERT INTO `django_session` VALUES ('26sbgcemcenal27segn5lmklvk6wdpw7', 'MGFjMTlmYTc4MDVlODRhMjgxODNhMzE2MGZiZTE1OTMzMWZiMjExYTp7InNoYXJlcl9wYXJlbnQiOiJob3dfd29ya3MiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6ImNmNjcwOWY2MTczZjBkYmIxZTEwZTBhM2E1OTY2MGZlMzQ4MDg2ODEiLCJfYXV0aF91c2VyX2lkIjoxLCJfc2Vzc2lvbl9leHBpcnkiOjB9', '2016-11-02 19:31:47');
INSERT INTO `django_session` VALUES ('2sp518kdrtpq1v8j9hwp2tbjq9t1wm5o', 'YTIzMmMxNjljZTk4ZmI1MDdhYzFhMjhiYjAyMmY0ODczYWFmNjEyNzp7fQ==', '2016-10-12 20:54:10');
INSERT INTO `django_session` VALUES ('3b8csoky1oav4ex4pnlxyh613rq1z781', 'YTIzMmMxNjljZTk4ZmI1MDdhYzFhMjhiYjAyMmY0ODczYWFmNjEyNzp7fQ==', '2017-03-04 15:30:07');
INSERT INTO `django_session` VALUES ('3n4k1dz1kau2v6eko73cc44xsrzr8zdi', 'YTIzMmMxNjljZTk4ZmI1MDdhYzFhMjhiYjAyMmY0ODczYWFmNjEyNzp7fQ==', '2016-09-09 13:31:56');
INSERT INTO `django_session` VALUES ('7wqop381xk21maqevpqjgrorzygtj89o', 'YTIzMmMxNjljZTk4ZmI1MDdhYzFhMjhiYjAyMmY0ODczYWFmNjEyNzp7fQ==', '2016-10-14 00:52:07');
INSERT INTO `django_session` VALUES ('909bne4rmiadekm0m3tgumm07lmg5vxc', 'YTIzMmMxNjljZTk4ZmI1MDdhYzFhMjhiYjAyMmY0ODczYWFmNjEyNzp7fQ==', '2016-10-20 18:49:27');
INSERT INTO `django_session` VALUES ('a6zvymsawfctj3skdkl7i13b3u1wzibr', 'YTIzMmMxNjljZTk4ZmI1MDdhYzFhMjhiYjAyMmY0ODczYWFmNjEyNzp7fQ==', '2016-10-20 18:49:27');
INSERT INTO `django_session` VALUES ('agxxl6ehlykcipl82i5ufb57dsf5uwbh', 'Mzg2ZjRkYTQ4YzNjNGQ2OGUyNDUwNTE2MjM4NjkxMGIzNGEzNmI2NDp7Il9hdXRoX3VzZXJfaGFzaCI6ImNmNjcwOWY2MTczZjBkYmIxZTEwZTBhM2E1OTY2MGZlMzQ4MDg2ODEiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9', '2016-07-19 18:12:27');
INSERT INTO `django_session` VALUES ('aki1su6xlmmzyj12gstm4chpnywqtnmx', 'YTIzMmMxNjljZTk4ZmI1MDdhYzFhMjhiYjAyMmY0ODczYWFmNjEyNzp7fQ==', '2016-10-14 20:14:32');
INSERT INTO `django_session` VALUES ('b8a8b0ajfurb8r2wrrx8o6mwfj8jmols', 'YTIzMmMxNjljZTk4ZmI1MDdhYzFhMjhiYjAyMmY0ODczYWFmNjEyNzp7fQ==', '2016-10-20 18:49:27');
INSERT INTO `django_session` VALUES ('k2aepc66kln2sqxl4xugp6n7lw80be4f', 'YTIzMmMxNjljZTk4ZmI1MDdhYzFhMjhiYjAyMmY0ODczYWFmNjEyNzp7fQ==', '2016-10-14 00:52:07');
INSERT INTO `django_session` VALUES ('kd1z0jm79uubesto1lehyaqbqdpqo0dt', 'YTIzMmMxNjljZTk4ZmI1MDdhYzFhMjhiYjAyMmY0ODczYWFmNjEyNzp7fQ==', '2016-10-12 20:54:10');
INSERT INTO `django_session` VALUES ('l4hyo2hxyjex62g2n2cmg8w4mybpnive', 'YTIzMmMxNjljZTk4ZmI1MDdhYzFhMjhiYjAyMmY0ODczYWFmNjEyNzp7fQ==', '2016-10-14 20:14:32');
INSERT INTO `django_session` VALUES ('lkllu7u3j3ejkwxslbi7cmf42lxupff8', 'Mzg2ZjRkYTQ4YzNjNGQ2OGUyNDUwNTE2MjM4NjkxMGIzNGEzNmI2NDp7Il9hdXRoX3VzZXJfaGFzaCI6ImNmNjcwOWY2MTczZjBkYmIxZTEwZTBhM2E1OTY2MGZlMzQ4MDg2ODEiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9', '2016-12-07 17:19:21');
INSERT INTO `django_session` VALUES ('mjcz4nffrfu8167fn1yxfco2ttdew98q', 'YTIzMmMxNjljZTk4ZmI1MDdhYzFhMjhiYjAyMmY0ODczYWFmNjEyNzp7fQ==', '2016-10-14 20:14:32');
INSERT INTO `django_session` VALUES ('mobasiu0bvynpe3c3usnu0hhxrr562n3', 'YTIzMmMxNjljZTk4ZmI1MDdhYzFhMjhiYjAyMmY0ODczYWFmNjEyNzp7fQ==', '2016-09-09 13:31:56');
INSERT INTO `django_session` VALUES ('nknrd2r5vp8543imq622ga5ugvk4dmj1', 'NGMxYjUyMzY0Y2ZiMjg2N2YyMDUwYjEwNTY0NjU3MGQ3MGE1MGU3ZDp7InNoYXJlcl9wYXJlbnQiOiJhZGRpYXoiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6ImNmNjcwOWY2MTczZjBkYmIxZTEwZTBhM2E1OTY2MGZlMzQ4MDg2ODEiLCJfYXV0aF91c2VyX2lkIjoxLCJfc2Vzc2lvbl9leHBpcnkiOjB9', '2016-11-05 17:05:07');
INSERT INTO `django_session` VALUES ('owhfnwa1ghzmax70jwjfwlg90txxsdm7', 'ZjE1NTM2YTc5YTdiZjQ0MWRjZmE5ODc4ODhjYmY5MmZlMTY5ZGI3NDp7Il9hdXRoX3VzZXJfaGFzaCI6ImNmNjcwOWY2MTczZjBkYmIxZTEwZTBhM2E1OTY2MGZlMzQ4MDg2ODEiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjd9', '2016-09-12 18:21:46');
INSERT INTO `django_session` VALUES ('qwouwlshl28e6mztfxcp5usm6hfou3ay', 'YjJjYjU3MjhlMTU1ZmJhNWE4ODgxZTcyOTAyZTBkMmUzNmIxZWQ2Zjp7InNoYXJlcl9wYXJlbnQiOiJhZGRpYXoiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6ImNmNjcwOWY2MTczZjBkYmIxZTEwZTBhM2E1OTY2MGZlMzQ4MDg2ODEiLCJfYXV0aF91c2VyX2lkIjo3LCJfc2Vzc2lvbl9leHBpcnkiOjB9', '2016-10-14 20:14:32');
INSERT INTO `django_session` VALUES ('ss27s1k2z6sc9k1q4dlocksbzmuct3ux', 'ZjE1NTM2YTc5YTdiZjQ0MWRjZmE5ODc4ODhjYmY5MmZlMTY5ZGI3NDp7Il9hdXRoX3VzZXJfaGFzaCI6ImNmNjcwOWY2MTczZjBkYmIxZTEwZTBhM2E1OTY2MGZlMzQ4MDg2ODEiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjd9', '2016-11-14 13:58:19');
INSERT INTO `django_session` VALUES ('u31iu6la981mmodpnbe01lkhplzncjtw', 'YTIzMmMxNjljZTk4ZmI1MDdhYzFhMjhiYjAyMmY0ODczYWFmNjEyNzp7fQ==', '2016-10-14 00:52:07');
INSERT INTO `django_session` VALUES ('v1trlumpbfh4vg9tut41812nodn1kcrc', 'YTIzMmMxNjljZTk4ZmI1MDdhYzFhMjhiYjAyMmY0ODczYWFmNjEyNzp7fQ==', '2016-05-21 23:49:54');
INSERT INTO `django_session` VALUES ('vv7zl8et25mdykfceryaxc108oem6p2j', 'Mzg2ZjRkYTQ4YzNjNGQ2OGUyNDUwNTE2MjM4NjkxMGIzNGEzNmI2NDp7Il9hdXRoX3VzZXJfaGFzaCI6ImNmNjcwOWY2MTczZjBkYmIxZTEwZTBhM2E1OTY2MGZlMzQ4MDg2ODEiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9', '2016-05-24 01:14:30');
INSERT INTO `django_session` VALUES ('wev45t86dsy8oy3jvwxjrs0v3h25kktl', 'Mzg2ZjRkYTQ4YzNjNGQ2OGUyNDUwNTE2MjM4NjkxMGIzNGEzNmI2NDp7Il9hdXRoX3VzZXJfaGFzaCI6ImNmNjcwOWY2MTczZjBkYmIxZTEwZTBhM2E1OTY2MGZlMzQ4MDg2ODEiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9', '2016-10-14 01:02:11');
INSERT INTO `django_session` VALUES ('wzv67rqitwxlgchi4zfg2amufhbj8xez', 'YTIzMmMxNjljZTk4ZmI1MDdhYzFhMjhiYjAyMmY0ODczYWFmNjEyNzp7fQ==', '2016-10-14 00:52:07');
INSERT INTO `django_session` VALUES ('z5vwatmvnm1azvgk5oitlmwd96pjzh43', 'YTIzMmMxNjljZTk4ZmI1MDdhYzFhMjhiYjAyMmY0ODczYWFmNjEyNzp7fQ==', '2016-10-12 20:54:10');

-- ----------------------------
-- Table structure for `paypal_ipn`
-- ----------------------------
DROP TABLE IF EXISTS `paypal_ipn`;
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

-- ----------------------------
-- Records of paypal_ipn
-- ----------------------------

-- ----------------------------
-- Table structure for `robots`
-- ----------------------------
DROP TABLE IF EXISTS `robots`;
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

-- ----------------------------
-- Records of robots
-- ----------------------------
INSERT INTO `robots` VALUES ('1', '14', null);
INSERT INTO `robots` VALUES ('2', '15', null);
INSERT INTO `robots` VALUES ('3', '16', null);
INSERT INTO `robots` VALUES ('4', '17', null);
INSERT INTO `robots` VALUES ('5', '18', null);

-- ----------------------------
-- Table structure for `williambid_articulo`
-- ----------------------------
DROP TABLE IF EXISTS `williambid_articulo`;
CREATE TABLE `williambid_articulo` (
  `content_ptr_id` int(11) NOT NULL,
  `imagen` varchar(100) NOT NULL,
  `cantidad_de_articulos` int(11) NOT NULL,
  `precio` double NOT NULL,
  `pujas_automaticas` tinyint(1) NOT NULL,
  PRIMARY KEY (`content_ptr_id`),
  CONSTRAINT `content_ptr_id_refs_id_15c42207` FOREIGN KEY (`content_ptr_id`) REFERENCES `williambid_content` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of williambid_articulo
-- ----------------------------

-- ----------------------------
-- Table structure for `williambid_autopuja`
-- ----------------------------
DROP TABLE IF EXISTS `williambid_autopuja`;
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of williambid_autopuja
-- ----------------------------

-- ----------------------------
-- Table structure for `williambid_content`
-- ----------------------------
DROP TABLE IF EXISTS `williambid_content`;
CREATE TABLE `williambid_content` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre_pt_pt` varchar(30) DEFAULT NULL,
  `nombre_en_us` varchar(30) DEFAULT NULL,
  `nombre_es_es` varchar(30) DEFAULT NULL,
  `descripcion_pt_pt` varchar(50) DEFAULT NULL,
  `descripcion_en_us` varchar(50) DEFAULT NULL,
  `descripcion_es_es` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of williambid_content
-- ----------------------------
INSERT INTO `williambid_content` VALUES ('1', '30x1', '30x1', '30x1', '30x1', '30x1', '30x1');

-- ----------------------------
-- Table structure for `williambid_paquetebid`
-- ----------------------------
DROP TABLE IF EXISTS `williambid_paquetebid`;
CREATE TABLE `williambid_paquetebid` (
  `content_ptr_id` int(11) NOT NULL,
  `cantidad_de_bids` int(11) NOT NULL,
  `precio` double NOT NULL,
  PRIMARY KEY (`content_ptr_id`),
  CONSTRAINT `content_ptr_id_refs_id_d2961be6` FOREIGN KEY (`content_ptr_id`) REFERENCES `williambid_content` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of williambid_paquetebid
-- ----------------------------
INSERT INTO `williambid_paquetebid` VALUES ('1', '30', '1');

-- ----------------------------
-- Table structure for `williambid_shoppinggcart`
-- ----------------------------
DROP TABLE IF EXISTS `williambid_shoppinggcart`;
CREATE TABLE `williambid_shoppinggcart` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `usuario_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `usuario_id` (`usuario_id`),
  CONSTRAINT `usuario_id_refs_id_d3b79a79` FOREIGN KEY (`usuario_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of williambid_shoppinggcart
-- ----------------------------
INSERT INTO `williambid_shoppinggcart` VALUES ('2', '1');
INSERT INTO `williambid_shoppinggcart` VALUES ('1', '7');
INSERT INTO `williambid_shoppinggcart` VALUES ('4', '10');

-- ----------------------------
-- Table structure for `williambid_subasta`
-- ----------------------------
DROP TABLE IF EXISTS `williambid_subasta`;
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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of williambid_subasta
-- ----------------------------
INSERT INTO `williambid_subasta` VALUES ('1', '1', '1', '2016-11-24 05:29:23', '00:01:00', '2016-11-24 05:30:23', '0.9', '1', null, '3', null);
INSERT INTO `williambid_subasta` VALUES ('2', '1', '1', '2017-01-31 15:08:42', '00:01:00', '2017-01-31 15:09:42', '0.9', '1', null, '3', null);

-- ----------------------------
-- Table structure for `williambid_subastavendida`
-- ----------------------------
DROP TABLE IF EXISTS `williambid_subastavendida`;
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

-- ----------------------------
-- Records of williambid_subastavendida
-- ----------------------------

-- ----------------------------
-- Table structure for `williambid_tiposubasta`
-- ----------------------------
DROP TABLE IF EXISTS `williambid_tiposubasta`;
CREATE TABLE `williambid_tiposubasta` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `descripcion` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of williambid_tiposubasta
-- ----------------------------
INSERT INTO `williambid_tiposubasta` VALUES ('1', 'Oportunity', 'Oportunity');
INSERT INTO `williambid_tiposubasta` VALUES ('2', 'Hot Bid', 'Hot Bid');
INSERT INTO `williambid_tiposubasta` VALUES ('3', 'Special', 'Special');
INSERT INTO `williambid_tiposubasta` VALUES ('4', 'Premium', 'Premium');

-- ----------------------------
-- Table structure for `williambid_venta`
-- ----------------------------
DROP TABLE IF EXISTS `williambid_venta`;
CREATE TABLE `williambid_venta` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `subasta_id` int(11) NOT NULL,
  `a_usuario` int(11) NOT NULL,
  `precio` double NOT NULL,
  `fecha_creacion` datetime NOT NULL,
  `en_red_de_usuario_id` int(11) NOT NULL,
  `confirmada` tinyint(1) NOT NULL,
  `fecha_confirmacion` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `subasta_id` (`subasta_id`),
  KEY `williambid_venta_8d35d038` (`en_red_de_usuario_id`),
  CONSTRAINT `en_red_de_usuario_id_refs_id_44c2c06f` FOREIGN KEY (`en_red_de_usuario_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `subasta_id_refs_id_e2316b99` FOREIGN KEY (`subasta_id`) REFERENCES `williambid_subastavendida` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of williambid_venta
-- ----------------------------

-- ----------------------------
-- Table structure for `williambid_ventaarticulo`
-- ----------------------------
DROP TABLE IF EXISTS `williambid_ventaarticulo`;
CREATE TABLE `williambid_ventaarticulo` (
  `venta_ptr_id` int(11) NOT NULL,
  `articulo_id` int(11) NOT NULL,
  PRIMARY KEY (`venta_ptr_id`),
  KEY `williambid_ventaarticulo_1818f191` (`articulo_id`),
  CONSTRAINT `articulo_id_refs_content_ptr_id_8c9c5971` FOREIGN KEY (`articulo_id`) REFERENCES `williambid_articulo` (`content_ptr_id`),
  CONSTRAINT `venta_ptr_id_refs_id_5dc41db1` FOREIGN KEY (`venta_ptr_id`) REFERENCES `williambid_venta` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of williambid_ventaarticulo
-- ----------------------------

-- ----------------------------
-- Table structure for `williambid_ventapaquetebid`
-- ----------------------------
DROP TABLE IF EXISTS `williambid_ventapaquetebid`;
CREATE TABLE `williambid_ventapaquetebid` (
  `venta_ptr_id` int(11) NOT NULL,
  `paquete_id` int(11) NOT NULL,
  PRIMARY KEY (`venta_ptr_id`),
  KEY `williambid_ventapaquetebid_54ff6362` (`paquete_id`),
  CONSTRAINT `paquete_id_refs_content_ptr_id_07d50d3c` FOREIGN KEY (`paquete_id`) REFERENCES `williambid_paquetebid` (`content_ptr_id`),
  CONSTRAINT `venta_ptr_id_refs_id_06f9448a` FOREIGN KEY (`venta_ptr_id`) REFERENCES `williambid_venta` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of williambid_ventapaquetebid
-- ----------------------------
