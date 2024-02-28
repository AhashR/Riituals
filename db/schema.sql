DROP SCHEMA IF EXISTS `Rituals`;    
CREATE SCHEMA `Rituals`;
USE `Rituals`;

-- https://www.w3schools.com/sql/sql_comments.asp
-- Create a User table, we probably need a login system

-- Handlers table

CREATE TABLE `User`(
    -- Minimal user table, adjust up to your needs
	`userId` INT NOT NULL AUTO_INCREMENT,	
    `firstname` VARCHAR(50),
    `lastname` VARCHAR(100),
	`emailaddress` VARCHAR(250),
    `telephonenumber` VARCHAR(15),
    `password` VARCHAR(15),
    PRIMARY KEY(`userId`)
);

CREATE TABLE `handlers` (
    `handlerId` INT NOT NULL AUTO_INCREMENT,
    `username` VARCHAR(255) NOT NULL,
    `password` VARCHAR(255) NOT NULL,
    `email` VARCHAR(255),
    `phoneNumber` VARCHAR(20),
    PRIMARY KEY(`handlerId`)
);

-- Employees table
CREATE TABLE `employees` (
    `employeeId` INT NOT NULL AUTO_INCREMENT,
    `username` VARCHAR(255) NOT NULL,
    `password` VARCHAR(255) NOT NULL,
    `email` VARCHAR(255),
    `phoneNumber` VARCHAR(20),
    PRIMARY KEY(`employeeId`)
);

-- Add your create tables SQL here. Make sure to include the indexes!
-- Alternative: use an ORM like SQLAlchemy. Then you will not need this file.