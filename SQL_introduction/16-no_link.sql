-- Lists all records of a table
-- Don't show values without a name
-- Display score then name

SELECT score, name
FROM second_table
WHERE name != NULL;