-- a script that creates the table force_name where the field 'name' cannot be null
CREATE TABLE IF NOT EXISTS force_name(
	id INT,
	name VARCHAR(256) NOT NULL
);
