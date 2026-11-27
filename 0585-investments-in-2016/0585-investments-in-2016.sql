# Write your MySQL query statement below
with cte as (
    select tiv_2015
    from Insurance
    group by tiv_2015
    having count(tiv_2015) > 1
),
cte2 as(
    select lat,lon from Insurance
    group by lat,lon
    having count(*) = 1
)
select round(sum(i.tiv_2016),2)as tiv_2016 from Insurance i
join cte c on
i.tiv_2015 = c.tiv_2015
join cte2 c2 on
i.lat = c2.lat
and i.lon = c2.lon
;
