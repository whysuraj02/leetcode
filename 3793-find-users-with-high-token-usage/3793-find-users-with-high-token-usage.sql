# Write your MySQL query statement below
with cte as(
    select distinct p1.user_id from prompts p1
    where p1.tokens >(
        select avg(p2.tokens)
        from prompts p2
        where p1.user_id = p2.user_id
    )
)
select p.user_id,count(p.prompt) as prompt_count,round(avg(p.tokens),2) as avg_tokens from prompts p 
right join cte c on
p.user_id = c.user_id
group by p.user_id
having count(*) >=3
order by avg_tokens desc,p.user_id asc;


