-- delete a database
BEGIN;
DELETE FROM INFORMATION_SCHEMA.DATABASES
WHERE DATABASE = 'hbtn_0c_0';
COMMIT;
