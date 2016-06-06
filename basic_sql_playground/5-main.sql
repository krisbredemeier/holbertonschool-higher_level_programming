select distinct last_name
from person
join (select tvshow_id, person_id as id from tvshowperson) using (id)
where tvshow_id = 3;

select count(*) From Person where age > 30;

select P.id, first_name, last_name, age, color, name from Person P
	inner join EyesColor E on P.id=E.person_id
	inner join TVShowPerson TVSP on P.id=TVSP.person_id
	inner join TVShow TVS on TVS.id=TVSP.tvshow_id
;

select SUM(age) from Person;
