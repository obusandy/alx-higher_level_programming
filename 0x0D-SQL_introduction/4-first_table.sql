-- script that creates a table called first_table
-- which will be in the current database in your MySQL server.
-- it is passed as an arg
CREATE TABLE IF NOT EXISTS first_table(
    id INT,
    name VARCHAR(256)
);
