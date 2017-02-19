
CREATE DATABASE `webxscan`  ;
CREATE TABLE `webxscan`.`cms` (
 `url` varchar(100) NOT NULL DEFAULT '',
 `cms` varchar(100) DEFAULT NULL,
 `postIP` varchar(100) DEFAULT NULL,
 `time` varchar(50) DEFAULT NULL,
 PRIMARY KEY (`url`)
) DEFAULT CHARSET=utf8;
