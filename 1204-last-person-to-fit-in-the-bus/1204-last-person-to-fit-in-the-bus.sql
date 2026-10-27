# Write your MySQL query statement below
with cte as(select person_name,turn,lessequal from(
    select person_name,weight,turn,sum(weight) over(order by turn asc) as lessequal
    from Queue)t
    where lessequal <=1000
    
)
select person_name from cte 
order by turn desc limit 1;