-- creates database hbtn_0d_usa and table states inside it
CREATE database IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE table IF NOT EXISTS states(id INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,name VARCHAR(256) NOT NULL);
