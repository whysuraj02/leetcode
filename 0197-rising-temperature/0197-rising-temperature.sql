# Write your MySQL query statement below
select id from
(select id,recordDate,temperature,
lag(temperature) over (order by recordDate) as prev_tem,
lag(recordDate) over (order by recordDate) as prev_date
 from Weather)t
where temperature > prev_tem 
and DATEDIFF(recordDate,prev_date) = 1;
