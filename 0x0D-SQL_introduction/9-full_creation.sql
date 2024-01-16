-- creates a table second_table in the database
-- adds multiples rows. 
-- database name will be passed as an arg
-- if the second_table already exist it will not fail
-- does not use the SELECT and SHOW.
CREATE TABLE
    IF NOT EXISTS second_table (id INT, name VARCHAR(256), score INT);

INSERT INTO
    second_table (id, name, score)
VALUES
    (1, "John", 10);

INSERT INTO
    second_table (id, name, score)
VALUES
    (2, "Alex", 3);

INSERT INTO
    second_table (id, name, score)
VALUES
    (3, "Bob", 14);

INSERT INTO
    second_table (id, name, score)
VALUES
    (4, "George", 8);
