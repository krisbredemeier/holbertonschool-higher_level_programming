update Person set age=27 where first_name="Jon" AND last_name="Snow";
update Person set age=18 where first_name="Walter Junior" AND last_name="White";
delete from eyescolor where person_id=(select id from Person where first_name = "Waler" AND last_name = "White");
delete from person where first_name = "Walter" AND last_name = "White";
select * from person
  order by first_name;
