-- Lists the number of records with the same score in the table second_table.
-- Record are ordered by DESC count.
SELECT score, count(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
