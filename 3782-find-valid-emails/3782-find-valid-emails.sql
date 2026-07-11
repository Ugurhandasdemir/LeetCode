/* Write your PL/SQL query statement below */
select * from Users
where REGEXP_LIKE(email, '^[a-zA-Z0-9]+@[a-zA-Z]+\.com$') 
order by user_id ASC;