# Write your MySQL query statement below
with cte as(
    select o.sales_id from orders o
    join company c on o.com_id = c.com_id
    where c.name = 'RED'
)
select name from salesperson
where sales_id not in (select sales_id from cte);