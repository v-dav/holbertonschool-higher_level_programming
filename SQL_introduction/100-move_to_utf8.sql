-- a script that converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci) in my MySQL server.
ALTER DATABASE hbtn_0c_0
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

-- a part of the script that converts table first_table to UTF8
ALTER TABLE first_table
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

-- converts the field name of first table to UTF8
ALTER TABLE first_table
MODIFY COLUMN name VARCHAR(256) 
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
