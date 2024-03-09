Drop database computerParts;
create database computerParts;
USE computerParts;

CREATE TABLE processors(
	productID INT PRIMARY KEY AUTO_INCREMENT,
    productName VARCHAR(600),
    price DOUBLE,
    productImage VARCHAR(800),
    productDetailURL VARCHAR(800) DEFAULT '#' 
    -- page URL that is product detail page in 'newegg.com'
);


CREATE TABLE amdMotherboards(
	productID INT PRIMARY KEY AUTO_INCREMENT,
    productName VARCHAR(600),
    price DOUBLE,
    productImage VARCHAR(800),
    productDetailURL VARCHAR(800) DEFAULT '#'
);

CREATE TABLE intelMotherboards(
	productID INT PRIMARY KEY AUTO_INCREMENT,
    productName VARCHAR(600),
    price DOUBLE,
    productImage VARCHAR(800),
    productDetailURL VARCHAR(800) DEFAULT '#'
);


CREATE TABLE amdGraphicsCards(
	productID INT PRIMARY KEY AUTO_INCREMENT,
    productName VARCHAR(600),
    price DOUBLE,
    productImage VARCHAR(800),
    productDetailURL VARCHAR(800) DEFAULT '#'
);

CREATE TABLE nvidiaGraphicsCards(
	productID INT PRIMARY KEY AUTO_INCREMENT,
    productName VARCHAR(600),
    price DOUBLE,
    productImage VARCHAR(800),
    productDetailURL VARCHAR(800) DEFAULT '#'
);


CREATE TABLE cases(
	productID INT PRIMARY KEY AUTO_INCREMENT,
    productName VARCHAR(600),
    price DOUBLE,
    productImage VARCHAR(800),
    productDetailURL VARCHAR(800) DEFAULT '#'
);


CREATE TABLE memories(
	productID INT PRIMARY KEY AUTO_INCREMENT,
    productName VARCHAR(600),
    price DOUBLE,
    productImage VARCHAR(800),
    productDetailURL VARCHAR(800) DEFAULT '#'
);


CREATE TABLE hddStorages(
	productID INT PRIMARY KEY AUTO_INCREMENT,
    productName VARCHAR(600),
    price DOUBLE,
    productImage VARCHAR(800),
    productDetailURL VARCHAR(800) DEFAULT '#'
);

CREATE TABLE ssdStorages(
	productID INT PRIMARY KEY AUTO_INCREMENT,
    productName VARCHAR(600),
    price DOUBLE,
    productImage VARCHAR(800),
    productDetailURL VARCHAR(800) DEFAULT '#'
);


CREATE TABLE powerSupplies(
	productID INT PRIMARY KEY AUTO_INCREMENT,
    productName VARCHAR(600),
    price DOUBLE,
    productImage VARCHAR(800),
    productDetailURL VARCHAR(800) DEFAULT '#'
);


CREATE TABLE cpuAirCoolerCoolings(
	productID INT PRIMARY KEY AUTO_INCREMENT,
    productName VARCHAR(600),
    price DOUBLE,
    productImage VARCHAR(800),
    productDetailURL VARCHAR(800) DEFAULT '#'
);

CREATE TABLE liquidOrWaterCoolerCoolings(
	productID INT PRIMARY KEY AUTO_INCREMENT,
    productName VARCHAR(600),
    price DOUBLE,
    productImage VARCHAR(800),
    productDetailURL VARCHAR(800) DEFAULT '#'
);

CREATE TABLE pcCaseFanCoolings(
	productID INT PRIMARY KEY AUTO_INCREMENT,
    productName VARCHAR(600),
    price DOUBLE,
    productImage VARCHAR(800),
    productDetailURL VARCHAR(800) DEFAULT '#'
);


 -- drop table computerParts.powerSupplies;
 -- drop table computerParts.cpuAirCoolerCoolings;
 -- drop table computerParts.liquidOrWaterCoolerCoolings;
 -- drop table computerParts.pcCaseFanCoolings;