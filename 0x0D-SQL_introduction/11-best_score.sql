-- List all records with score >= 10 from the table second_table of the database hbtn_0c_0
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
