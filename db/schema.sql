DROP SCHEMA IF EXISTS `Rituals`;    
CREATE SCHEMA `Rituals`;
USE `Rituals`;

-- https://www.w3schools.com/sql/sql_comments.asp
-- Create a User table, we probably need a login system

CREATE TABLE `Location`(
    -- Minimal user table, adjust up to your needs
	`locationId` INT NOT NULL AUTO_INCREMENT,	
    `userLocation` VARCHAR(50) NOT NULL,
    PRIMARY KEY(`locationId`)
);

CREATE TABLE `User`(
    -- Minimal user table, adjust up to your needs
	`userId` INT NOT NULL AUTO_INCREMENT,	
    `name` VARCHAR(50) NOT NULL,
    `locationId` INT,
    `branchnumber` VARCHAR(50),
	`emailaddress` VARCHAR(250) NOT NULL,
    `telephonenumber` VARCHAR(15),
    `password` VARCHAR(15) NOT NULL,
    `isHandler` BOOLEAN,
    PRIMARY KEY(`userId`),
    FOREIGN KEY (`locationId`) REFERENCES `Location`(`locationId`)
);

CREATE TABLE `Deliverydate`(
    -- Minimal user table, adjust up to your needs
    `dateId` INT NOT NULL AUTO_INCREMENT,  
    `arrivalDate` DATE NOT NULL,
    PRIMARY KEY(`dateId`)
);
 
CREATE TABLE `Deliveries`(
    -- Minimal user table, adjust up to your needs
    `deliveryId` INT NOT NULL AUTO_INCREMENT,  
    `departureTime` TIME NOT NULL,
    `arrivalTime` TIME,
    `arrivalEstimate` TIME NOT NULL,
    `dateId` INT,
    `userId` INT,
    PRIMARY KEY(`deliveryId`),
    FOREIGN KEY (`dateId`) REFERENCES `Deliverydate`(`dateId`),
    FOREIGN KEY (`userId`) REFERENCES `User`(`userId`)
);
-- Add your create tables SQL here. Make sure to include the indexes!
-- Alternative: use an ORM like SQLAlchemy. Then you will not need this file.