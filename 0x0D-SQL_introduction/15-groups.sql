-- lists the number of records with the same score
-- from the table second_table of the database
-- in a descending order
-- database name will be passed as an arg to the mysql command
SELECT score, COUNT(score) AS number
FROM second_table
GROUP BY score
ORDER BY score DESC;
