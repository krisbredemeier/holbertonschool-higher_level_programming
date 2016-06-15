\! echo "\nNumber of seasons by tvshow_id?"
select TVShow.id, count(Season.tvshow_id) from TVShow
  left join Season on (TVShow.id = Season.tvshow_id)
  group by Season.tvshow_id;

\! echo "\nNumber of occurrences of the same episode number ordered by episode number?"
select distinct number, count(number) from Episode
  group by number;

\! echo "\nTop 3 of the Genre's occurrences in all TVShows ordered by this number?"
select genre_id, count(genre_id) from TVShowGenre
  group by genre_id
  order by count(genre_id)
  DESC limit 3;

\! echo "\nSearch all TVShow with this letter sequence 'th' case insensitive and display with the name in lowercase?"
select lower(name) from TVShow where name like "%th%";
