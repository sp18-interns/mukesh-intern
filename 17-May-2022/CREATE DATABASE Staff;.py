CREATE DATABASE Staff;
USE Staff;
CREATE TABLE StaffInfo
(
StaffID int,
StaffName varchar(6000),
FatherName varchar(6000),
PhoneNumber bigint,
Addressofstaff varchar(6000),
City varchar(6000),
Country varchar(6000),
);

ALTER TABLE StaffInfo ADD BloodGroup varchar(6000)
----------------------------------------------------------------------
CREATE TABLE StaffInfo
(
StaffID int,
StaffName varchar(6000)NOT NULL,
FatherName varchar(6000),
PhoneNumber bigint,
Addressofstaff varchar(6000)NOT NULL,
City varchar(6000),
Country varchar(6000),
);
INSERT INTO  StaffInfo VALUES('07','Tanmay','Yadav','961788990',NOT NULL,'PUNE','INDIA')
----------------------------------------------------------------------------------------
CREATE TABLE StaffInfo
(
StaffID int NOT NULL,
StaffName varchar(6000)NOT NULL,
FatherName varchar(6000),
PhoneNumber bigint,
Addressofstaff varchar(6000)NOT NULL,
City varchar(6000),
Country varchar(6000),
CONSTRAINT UC_StaffInfo UNIQUE(StaffInfo, PhoneNumber)
);