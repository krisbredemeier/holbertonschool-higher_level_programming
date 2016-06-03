insert into eyescolor (person_id, color) values (6, "Brown");
insert into eyescolor (person_id, color) values (7, "Green");

CREATE TABLE TVShow (
  id INT PRIMARY KEY NOT NULL,
  name CHAR(128) NOT NULL
);

CREATE TABLE TVShowPerson (
  tvshow_id INT NOT NULL,
  person_id INT NOT NULL,
  FOREIGN KEY (TVShow_id) REFERENCES tvshow(id),
  FOREIGN KEY (Person_id) REFERENCES person(id)
);

insert into tvshow (name) values ("Homeland");
insert into tvshow (name) values ("The big bang theory");
insert into tvshow (name) values ("Game of Thrones");
insert into tvshow (name) values ("Breaking bad");

insert into tvshowperson (person_id, tvshow_id) values (4, 2);
insert into tvshowperson (person_id, tvshow_id) values (3, 3);
insert into tvshowperson (person_id, tvshow_id) values (2, 4);
insert into tvshowperson (person_id, tvshow_id) values (3, 5);
insert into tvshowperson (person_id, tvshow_id) values (3, 6);
insert into tvshowperson (person_id, tvshow_id) values (3, 7);

select * from person;
select * from eyescolor;
select * from tvshow;
select * from tvshowperson;
