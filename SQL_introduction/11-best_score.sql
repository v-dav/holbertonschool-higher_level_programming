-- a script that lists all records with a score >= 10 in the table second_table of the database hbtn_0c_0 in my MySQL server

SELECT second_table.score, second_table.name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
