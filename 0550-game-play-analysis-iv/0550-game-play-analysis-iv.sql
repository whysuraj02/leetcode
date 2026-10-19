# Write your MySQL query statement below
with cte as (
    select player_id,min(event_date) as first_login  from Activity
    group by player_id
),
cte2 as (
    select count(Distinct player_id) as noofplayers from Activity
)
select coalesce(
    round((count(distinct a.player_id)/ c2.noofplayers),2)
    ,0)
     as fraction from Activity a
join cte c on
    a.player_id = c.player_id
    and a.event_date = date_add(c.first_login,interval 1 day)
cross join cte2 c2;
