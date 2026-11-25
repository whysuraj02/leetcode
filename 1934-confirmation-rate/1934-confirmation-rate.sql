# Write your MySQL query statement below
select s.user_id,
coalesce(
    round(
        count(case when action = 'confirmed' then 1 end) * 1.0
        /nullif(count(c.user_id),0),
        2),
        0) as confirmation_rate
from Signups s
left join Confirmations c
on s.user_id = c.user_id
group by s.user_id;