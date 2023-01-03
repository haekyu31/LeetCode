# Write your MySQL query statement below
SELECT actor_id, director_id FROM(
SELECT actor_id, director_id, COUNT(timestamp) AS cooperated FROM ActorDirector 
GROUP BY actor_id, director_id)
table1
WHERE cooperated >= 3;