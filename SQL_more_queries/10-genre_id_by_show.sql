-- Left join
-- SELECT columns
-- FROM table1
-- TYPE JOIN table2 ON table1.column = table2.column

SELECT tv_shows.title, tv_shows_genres.genre_id
FROM tv_shows
LEFT JOIN tv_shows_genres ON tv_shows.genre_id = tv_shows_genres.id
ORDER BY tv_shows.title ASC, tv_shows_genres.genre_id ASC;