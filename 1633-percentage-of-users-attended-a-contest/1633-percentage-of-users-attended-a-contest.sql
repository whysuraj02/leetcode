# Write your MySQL query statement below
with cte as (
    select count(user_id) as noofusers from users
)
select r.contest_id,round((count(r.user_id)/c.noofusers * 100),2) as percentage
from register r 
cross join cte c
group by r.contest_id
order by percentage desc,r.contest_id asc;


