CREATE TABLE SampleSourceTable (StudentID int, StudentName varchar(8000),Marks int);
CREATE TABLE SampleTargetTable(StudentID int, StudentName varchar(8000),Marks int)


INSERT INTO SampleSourceTable VALUES('1','Vidhate','78');
INSERT INTO SampleSourceTable VALUES('2','Vidhaty','87');
INSERT INTO SampleSourceTable VALUES('3','Vidhatp','98');

INSERT INTO SampleTargetTable VALUES('1','Vidhate','78');
INSERT INTO SampleTargetTable VALUES('2','Vidhaty','67');
INSERT INTO SampleTargetTable VALUES('3','Vidhatp','89');

MERGE SampleTargetTable TARGET USING SampleSourceTable SOURCE ON (TARGET.StudentID = SOURCE.StudentID)
WHEN MATCHED AND TARGET.StudentName <> Source.StudentName OR TARGET.Marks <> Source.Marks
THEN
UPDATE SET TARGET.StudentName = SOURCE.StudentName,TARGET.Marks = SOURCE.Marks
WHEN NOT MATCHED BY TARGET THEN
INSERT (StudentID, StudentName, Marks) VALUES (SOURCE.StudentID, SOURCE.StudentName, SOURCE.Marks)
WHEN NOT MATCHED BY SOURCE THEN
DELETE;

SELECT * FROM SampleSourceTable;

SELECT * FROM SampleTargetTable;
