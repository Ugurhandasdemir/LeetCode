select p.project_id as project_id  , ROUND(AVG(e.experience_years),2) as average_years
from Employee e
left join Project p on p.employee_id = e.employee_id 
where p.project_id IN (p.project_id )
group by p.project_id
order by p.project_id ASC