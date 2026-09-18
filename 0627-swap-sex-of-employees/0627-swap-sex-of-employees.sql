# Write your MySQL query statement below
update salary
set sex=
case
    WHEN sex='m' then 'f'
    else 'm'
    END;
