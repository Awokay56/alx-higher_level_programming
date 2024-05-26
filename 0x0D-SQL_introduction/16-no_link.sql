-- Lists all records of the table second_table name value.
-- Records are ordered by descending score.
SELECT score, name
FROM second_table
WHERE NAME != ""
ORDER BY score DESC;
