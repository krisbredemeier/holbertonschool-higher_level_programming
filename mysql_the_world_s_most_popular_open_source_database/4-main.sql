\! echo "\nList of all TVShows by all Genres ordered by genre name (A-Z)? (if a genre has 0 TVShow, please display NULL)"
select Genre.name, TVShow.name from TVShow
  right join TVShowGenre on (TVShow.id = TVShowGenre.tvshow_id)
  right join Genre on (TVShowGenre.genre_id = Genre.id)
  order by Genre.name;

\! echo "\nName of the pilot (first episode of the first season) of each TVShow ordered by TVShow name (A-Z)?"
select TVShow.name, Episode.name from TVShow
  join Season on (TVShow.id = Season.tvshow_id)
  join Episode on (Season.id = Episode.season_id)
  where Episode.number =1 and Season.number = 1;

\! echo "\nList of all Genres by all TVShows ordered by TVShow name (A-Z)? (if a genre has 0 TVShow, please display NULL as TVShow name)"
select TVShow.name, Genre.name from TVShow
  right join TVShowGenre on (TVShow.id = TVShowGenre.tvshow_id)
  right join Genre on (TVShowGenre.genre_id = Genre.id)
  order by TVShow.name;
