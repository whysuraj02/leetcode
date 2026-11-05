# Write your MySQL query statement below
with cte as(
    select date_format(trans_date,'%Y-%m') as month,country,count(state) as trans_count,
    sum(amount) as trans_total_amount from Transactions 
    group by month,country
),
cte2 as(
select date_format(trans_date,'%Y-%m') as month,country,count(state) as approved_count,sum(amount) as approved_total_amount from Transactions 
where state = 'approved'
group by month,country)

select c.month,c.country,c.trans_count,coalesce(c2.approved_count,0)as approved_count,c.trans_total_amount,
coalesce(c2.approved_total_amount,0) as approved_total_amount from cte c
left join cte2 c2 on
c.month = c2.month and c.country <=> c2.country;