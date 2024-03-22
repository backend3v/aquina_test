USE db;

CREATE TABLE `events` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `api_id` varchar(45) DEFAULT NULL,
  `title` varchar(100) DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL,
  `categories` varchar(100) DEFAULT NULL,
  `sources` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
);
-- UPDATE mysql.user SET host='%' WHERE user='ed' AND host='localhost';
FLUSH PRIVILEGES;
ALTER USER 'ed'@'localhost' IDENTIFIED BY '12345Ab*';
GRANT ALL ON db.* TO 'ed'@'localhost';