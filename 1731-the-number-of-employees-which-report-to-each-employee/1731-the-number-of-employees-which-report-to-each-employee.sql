# Write your MySQL query statement below
select e.employee_id,
e.name,
count(e1.reports_to)as reports_count,
round(avg(e1.age)) as average_age from employees e 
left join employees e1 on
e.employee_id=e1.reports_to
group by e.employee_id,e.name
having count(e1.reports_to) > 0
order by e.employee_id
;