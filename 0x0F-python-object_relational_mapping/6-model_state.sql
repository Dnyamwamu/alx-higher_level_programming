-- Create database hbtn_0e_6_usa
CREATE DATABASE IF NOT EXISTS hbtn_0e_6_usa;
USE hbtn_0e_6_usa;
CREATE TABLE IF NOT EXISTS states (
    id INT(11) NOT NULL AUTO_INCREMENT,
    name VARCHAR(128) NOT NULL,
    PRIMARY KEY (id)
) ENGINE=InnoDB;

SHOW CREATE TABLE states;
