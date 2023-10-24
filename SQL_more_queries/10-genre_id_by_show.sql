-- Left join
-- SELECT columns
-- FROM table1
-- TYPE JOIN table2 ON table1.column = table2.column

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;