''' task three '''
\! echo "\nList of TVShows ordered by name (A-Z) with more than or equal 4 seasons?"
select name from (select TVShow.name, count(Season.tvshow_id) as nb_seasons from TVShow
  left join Season on (TVShow.id = Season.tvshow_id)
  group by Season.tvshow_id
  order by name)
  As s Where nb_seasons >3;

\! echo "\nList of TVShows ordered by name (A-Z) with the Genre 'Comedy'?"
select TVShow.name from TVShow
  left join TVShowGenre on (TVShow.id = TVShowGenre.tvshow_id)
  left join Genre on (TVShowGenre.genre_id = Genre.id)
  where Genre.name = "Comedy"
  order by TVShow.name;

\! echo "\nList of Actors ordered by name (A-Z) for the TVShow 'The Big Bang Theory'?"
select Actor.name from TVShow
  left join TVShowActor on (TVShow.id = TVShowActor.tvshow_id)
  left join Actor on (TVShowActor.actor_id = Actor.id)
  where TVShow.name = "The Big Bang Theory"
  order by Actor.name;

\! echo "\nTop 10 of actors by number of TVShows where they are? (without Actor name order => can be random)"
select Actor.name, count(TVShow.id) as nb_tvshows from TVShow
  left join TVShowActor on (TVShow.id = TVShowActor.tvshow_id)
  left join Actor on (TVShowActor.actor_id = Actor.id)
  group by Actor.name
  order by count(TVShow.id) desc limit 10;
