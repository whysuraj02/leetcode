# Write your MySQL query statement below
with cte as (
    select customer_id,min(order_date) as order_day from Delivery
    group by customer_id
),
noofcust as (
    select count(distinct customer_id) as noofcustomer from Delivery
)
select round(count(d.customer_pref_delivery_date)/n.noofcustomer * 100,2) as immediate_percentage from Delivery d
join cte c on
d.customer_id = c.customer_id
and d.customer_pref_delivery_date = c.order_day
cross join noofcust n ;
