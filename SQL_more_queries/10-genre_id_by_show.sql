-- Left join
-- SELECT columns
-- FROM table1
-- TYPE JOIN table2 ON table1.column = table2.column

SELECT tv_shows.title, tv_shows_genres.genre_id
FROM tv_shows
JOIN tv_shows_genres ON tv_shows.id = tv_shows_genres.show_id;