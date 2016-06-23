''' task three '''
\! echo "\nNumber of season by TVShow ordered by name (A-Z)?"
select TVShow.name, count(Season.tvshow_id) as nb_seasons from TVShow
  left join Season on (TVShow.id = Season.tvshow_id)
  group by Season.tvshow_id
  order by name;

\! echo "\nList of Network by TVShow ordered by name (A-Z)?"
select TVShow.name as "TVShow name", Network.name as Network from TVShow
  left join Network on (TVShow.network_id = Network.id)
  order by TVShow.name;

\! echo "\nList of TVShows ordered by name (A-Z) in the Network 'Fox (US)'?"
select TVShow.name from TVShow
  left join Network on (TVShow.network_id = Network.id)
  where Network.name = "Fox (US)"
  order by TVShow.name;

\! echo "\nNumber of episodes by TVShows ordered by name (A-Z)?"
select TVShow.name, count(Episode.id) as nb_episodes from TVShow
  left join Season on (TVShow.id = Season.tvshow_id)
  left join Episode on (Season.id = Episode.season_id)
  group by TVShow.id
  order by TVShow.name;
