''' task one  '''
\! echo "\nList of all tables?"
show tables;

\! echo "\nDisplay the table structure of TVShow, Genre and TVShowGenre?"
describe TVShow;
describe Genre;
describe TVShowGenre;

\! echo "\nList of TVShows, only id and name ordered by name (A-Z)?"
select id, name from TVShow
  order by name;

\! echo "\nList of Genres, only id and name ordered by name (Z-A)?"
select id, name from Genre
  order by name DESC;

\! echo "\nList of Network, only id and name?"
select id, name from Network;

\! echo "\nNumber of episodes in the database?"
select count(id) From Episode;
