select distinct last_name
from person
join (select tvshow_id, person_id as id from tvshowperson) using (id)
where tvshow_id = 3;

select count(*) From Person where age > 30;

select * from person, eyescolor, tvshow;

select SUM(age) from Person;
