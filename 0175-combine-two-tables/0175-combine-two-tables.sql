select firstName,lastName ,city, state from
(select * from Person p
left join Address a on p.personId=a.personId)