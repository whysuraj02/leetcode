# Write your MySQL query statement below
select customer_number from orders 
group by customer_number
having count(order_number) = (
    select max(order_number) from (select count(order_number) as order_number from orders group by customer_number) as t
)