# Write your MySQL query statement below
select eu.unique_id,ep.name from employees ep
left join employeeuni eu on
ep.id=eu.id;