# Write your MySQL query statement below
with cte as(
    select product_id,max(change_date) as datebelow17 from products 
    where change_date <= '2019-08-16'
    group by product_id
),
uniquepro as (
    select distinct product_id from products
)
select  u.product_id,
    coalesce(p.new_price,10) as price
from uniquepro u
left join cte c on
u.product_id = c.product_id
left join products p on
c.product_id = p.product_id
and p.change_date = c.datebelow17
;
     