-- a script that lists all records of the table second_table of the database hbtn_0c_0 in my MySQL server without listing rows that don't have the "name " value

SELECT second_table.score, second_table.name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
