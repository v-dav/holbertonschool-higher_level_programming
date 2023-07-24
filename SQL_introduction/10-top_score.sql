/* a script that lists all records of the table second_table of the database hbtn_0c_0
in my MySQL server in descending order */

SELECT second_table.score, second_table.name
FROM second_table
ORDER BY score DESC;
