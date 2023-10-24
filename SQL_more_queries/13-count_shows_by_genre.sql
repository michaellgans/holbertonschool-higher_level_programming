-- Lists all genres and displays the count of shows per genre
SELECT DISTINCT tv_genres.name AS genre COUNT (tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
INNER JOIN tv_show_genres ON tv_genres.show_id = tv_show_genres.genre_id
GROUP BY genre
ORDER BY number_of_shows DESC