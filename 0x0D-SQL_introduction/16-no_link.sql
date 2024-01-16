-- lists all records of the table second_table of the database
-- listed in descending order
-- rows are not listed without name value
-- database name will be passed as an arg to the mysql command
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
