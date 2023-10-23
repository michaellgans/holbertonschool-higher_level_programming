-- Left join
-- SELECT columns
-- FROM table1
-- TYPE JOIN table2 ON table1.column = table2.column

SELECT cities.id, cities.name, states.name
FROM cities
LEFT JOIN states ON cities.state_id = states.id;