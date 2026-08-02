# Write your MySQL query statement below
SELECT tweet_id FROM tweets
WHERE char_length(content)>15;