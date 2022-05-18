--DDL BASICS COMMAND

CREATE DATABASE Staff;
USE Staff1;
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

SELECT * FROM StaffInfo

INSERT INTO StaffInfo

VALUES(1,'MUKESH YADAV','FATHER NAME',7457890098,'CG','INDIA','A+VE')

UPDATE StaffInfo
SET StaffID = 2, StaffName= 'Divpenshu','Digpal Pandey',PhoneNumber=67897,Addressofstaff='CG',Country='INDIA'
WHERE StaffID = 2

--Delete the if from deleete command
DELETE FROM StaffInfo WHERE StaffID = 2

--Drop command
DROP TABLE StaffInfo;

--Drop Database
--DROP DATABASE Students;

-- Alter command
ALTER TABLE StudentsInfo ADD




--Drop command
DROP TABLE StaffInfo;

--Drop Database
--DROP DATABSE

--Alter command


ALTER TABLE StudentsInfo ADD Rollnumber varchar(8000);

ALTER TABLE StudentsInfo DROP COLUMN Rollnumber;

ALTER TABLE StudentsInfo ADD DOB DATE;
--  Update type of DOB object
ALTER TABLE StudentsInfo ALTER COLUMN DOB datetime;

-- rename the table file name from StudentsInfo to InfoStudent 
