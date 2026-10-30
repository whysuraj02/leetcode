# Write your MySQL query statement below

with cte as(
    select machine_id,sum(timestamp)as end_act,count(distinct process_id) as noofprocessid from Activity
    where activity_type = 'end'
    group by machine_id
),
cte2 as(
    select machine_id,sum(timestamp) as start_act from Activity
    where activity_type = 'start'
    group by machine_id
)
select c.machine_id,round((c.end_act - c2.start_act)/c.noofprocessid,3) as processing_time from cte c
join cte2 c2 on
c.machine_id = c2.machine_id;
