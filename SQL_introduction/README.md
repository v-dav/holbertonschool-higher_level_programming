# SQL - Introduction

![image](https://github.com/v-dav/holbertonschool-higher_level_programming/assets/115344057/ae1ee515-e110-4682-9d29-19449fccf68a)


## 📖  Learning objectives
At the end of this project, I'am expected to be able to explain to anyone:

- What’s a database
- What’s a relational database
- What does SQL stand for
- What’s MySQL
- How to create a database in MySQL
- What does DDL and DML stand for
- How to CREATE or ALTER a table
- How to SELECT data from a table
- How to INSERT, UPDATE or DELETE data
- What are subqueries
- How to use MySQL functions

## How to Launch

`service mysql start`

`mysql -u root -p`

## Database
Collection of related information. 2 main types:
- Relational Database: tables with columns and rows and keys
- Non-Relational Database: KV pairs, JSON, XML…

RDBMS: Related Database Management System
- Allows to create and maintain a database
- Create - Read - Update - Delete —> CRUD = 4 main operations on information

SQL is a Structured Query Language used to interact with RDBMS

## Basics
### Keys
- Primary Key: unique for each row in the table. Can be of 2 types:  
- Surrogate Key: no mapped to anything in a real world (ex: a random number)
- Natural Key: mapped to a real utility in the real world (ex security number)
- Foreign Key: stores a primary key of another table to link to a different table
- Composite Key: a key composed of 2 attributes (2 columns)

### Data Types used in SQL
- INT — whole numbers
- DECIMAL (M, N) —decimal numbers - Exact value
- VARCHAR (1) — string of text of lenght 1
- BLOB — binary large objects, stores large data
- DATE — ‘YYYY-MM-DD”
- TIMESTAMP — ‘YYY-MM-DD HH:MM:SS”

## Commands
### Database
```sql
SHOW DATABASES;

CREATE DATABASE IF NOT EXISTS name;

DROP DATABASE IF EXISTS name;

USE databse_name;
```
### Tables
```sql
SHOW TABLES -- show all the tables of the datadase

SHOW CREATE TABLE table_name; -- shows the full structure of the table used to create this table

CREATE TABLE tablename (
	student_id INT PRIMARY KEY, #creates the first column with a primary key. Another way PRIMARY KEY (student_id)
	name VARCHAR (20) NOT NULL, #allocates space for 20 chars max for this field. NOT NULL means that we cannot insert a NULL name into the this field
  major VARCHAR (20) UNIQUE #UNIQUE keyword makes sure that that only unique values can be entered as attribute value
); #always ends with ;

DESCRIBE student; # shows the data

DROP TABLE student #deletes the table

ALTER TABLE student ADD gpa DECIMAL(3, 2); #adds a column to a table

ALTER TABLE student DROP COLUMN gpa; #deletes a columns

#By default the primary key is NOT NULL and UNIQUE. These are called constraints.

```

### Data Insertion
```sql
INSERT INTO student VALUES(1, "Jack", "Biology");
INSERT INTO student(student_id, name) VALUES(3, "Claire"); # specifieng pieces of info we want to enter
```

### Data Update
```sql
UPDATE student
SET major = "Bio"
WHERE major = "Biology"

UPDATE student
SET major = "Comp Sci"
WHERE major = "CS";

UPDATE student
SET major = "Socio"
WHERE name = "Kate";

UPDATE student
SET major = "Bio-Socio"
WHERE major = "Bio" OR major = "Socio";

UPDATE student
SET name = "Tom", major = "undecided"
WHERE student_id = 1;

UPDATE student
SET major = "biology";
```

### Data Deletion
```sql
DELETE FROM student
WHERE major = "biology";
```

### Basic Queries
```sql
SELECT *
FROM student;

SELECT name, major #selects the column name and major
FROM student;

SELECT student.name, student.major #same thing
FROM student

SELECT student.name, student.major
FROM student
ORDER BY name # returns in alphabetical order.

SELECT student.name, student.major
FROM student
ORDER BY name DESC #returns in reverse (descendant) alphabetical order. ASC it's ascending order

SELECT student.name, student.major
FROM student
ORDER BY name
LIMIT 2; # will only display the first 2

-- thats a comment

<> -- this in not equal to sign

SELECT *
FROM student
WHERE name IN ("Jack", "Vlad");
```

### Functions
```sql
SELECT COUNT(emp_id)
FROM employee
WHERE SEX = 'F' AND birth_day > "1970-01-01"

SELECT AVG(salary)
FROM employee;

SELECT SUM(salary)
FROM employee;

SELECT COUNT(sex), sex --AGREGATION of DATA
FROM employee
GROUP BY sex;
```

### Wildcards
```sql
SELECT *
FROM client
WHERE client_name LIKE "%LLC";

```

### Unions
```sql
SELECT first_name
FROM employee
UNION
SELECT branch_name
FROM branch;
--Gives a commun column. !RULE: must have the same number of columns and similar data types
```

### Joins
```sql
SELECT employee.emp_id, employee.first_name, branch.branch_name
FROM employee
JOIN branch
ON employee.emp_id = branch.mgr_id;
--General JOIN or inner JOIN

--Left JOIN: include all rows from the FROM table
--Right JOIN: include all rows from the right table
```
![sq_joins](https://github.com/v-dav/holbertonschool-higher_level_programming/assets/115344057/4e0dd8d3-ec8a-4d41-ac3d-c36ab61a4526)

![joins](https://github.com/v-dav/holbertonschool-higher_level_programming/assets/115344057/b2d1e311-0e11-493a-9992-23b2eecd83d3)

### Nested Queries
```sql
SELECT employee.first_name, employee.last_name
FROM employee
WHERE emp_id IN (
	SELECT works_with.emp_id
	FROM works_with
	WHERE works_with.total_sales > 30000
);

SELECT client.client_name
FROM client
WHERE client.branch_id = (
	SELECT branch.branch_id
	FROM branch
	WHERE branch.mgr_id = 102
);
```

### ON Delete Cascade
```sql
ON DELETE SET NULL --if we delete an entry from a table, the value associated with this entry in the another table will be set to NULL
ON DELETE CASCADE -- the entire row will be deleted
```

## How To Create a SQL Dump
```jsx
$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
Enter password: 
$ curl "https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
$ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
id  name
1   Drama
2   Mystery
3   Adventure
4   Fantasy
5   Comedy
6   Crime
7   Suspense
8   Thriller
$
```
