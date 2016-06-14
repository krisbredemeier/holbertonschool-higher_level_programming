show tables;

describe TVShow;
describe Genre;
describe TVShowGenre;

select id, name from TVShow
  order by name;

select id, name from Genre
  order by name DESC;

select id, name from Network;

select count(id) From TVShow;
