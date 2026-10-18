# Write your MySQL query statement below
with cte as (
    select query_name,count(query_name) as querycount from Queries
    group by query_name
)
select q.query_name,round((sum(q.rating/q.position)/c.querycount),2) as quality,
round(
    (count(case when rating < 3 then 1 end) / c.querycount * 100),2
) as poor_query_percentage
from queries q join
cte c on 
q.query_name = c.query_name
group by query_name;
