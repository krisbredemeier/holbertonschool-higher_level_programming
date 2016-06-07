insert into eyescolor (person_id, color) values ( (select id from Person where first_name="Jon" AND last_name="Snow"), "Brown");
insert into eyescolor (person_id, color) values ( (select id from Person where first_name="Arya" AND last_name="Stark"), "Green");

CREATE TABLE TVShow (
  id INTEGER PRIMARY KEY NOT NULL,
  name CHAR(128) NOT NULL
);

CREATE TABLE TVShowPerson (
  tvshow_id INT NOT NULL,
  person_id INT NOT NULL,
  FOREIGN KEY (TVShow_id) REFERENCES tvshow(id),
  FOREIGN KEY (Person_id) REFERENCES person(id)
);

insert into TVshow (name) values ("Homeland");
insert into TVshow (name) values ("The big bang theory");
insert into TVshow (name) values ("Game of Thrones");
insert into TVshow (name) values ("Breaking bad");

insert into tvshowperson (person_id, tvshow_id) values (
  (select id from TVShow where name="Breaking bad"),
	(select id from Person where first_name="Walter Junior" and last_name="White")
);
insert into tvshowperson (person_id, tvshow_id) values (
  (select id from TVShow where name="Game of Thrones"),
	(select id from Person where first_name="Jaime" and last_name="Lannister")
);
insert into tvshowperson (person_id, tvshow_id) values (
  (select id from TVShow where name="The big bang theory"),
	(select id from Person where first_name="Sheldon" and last_name="Cooper")
);
insert into tvshowperson (person_id, tvshow_id) values (
  (select id from TVShow where name="Game of Thrones"),
	(select id from Person where first_name="Tyrion" and last_name="Lannister")
);
insert into tvshowperson (person_id, tvshow_id) values (
  (select id from TVShow where name="Game of Thrones"),
	(select id from Person where first_name="Jon" and last_name="Snow")
);
insert into tvshowperson (person_id, tvshow_id) values (
  (select id from TVShow where name="Game of Thrones"),
	(select id from Person where first_name="Arya" and last_name="Stark")
);

select * from person;
select * from eyescolor;
select * from tvshow;
select * from tvshowperson;
