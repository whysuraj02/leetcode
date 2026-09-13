# Write your MySQL query statement below
-- select max(num) as num from (
--     select num from MyNumbers group by num having count(num) = 1
-- ) as t;
with cte as (
    select num from mynumbers group by num having count(num) = 1
)
select max(num) as num from cte;