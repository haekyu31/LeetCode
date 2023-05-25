# Write your MySQL query statement below
SELECT query_name 
,  ROUND(AVG(rating*100 / position), 0)/100 AS quality
,  ROUND(SUM(case 
             when rating < 3 then 1 
             else 0 end
            )*100 / count(*), 2) as poor_query_percentage
FROM Queries
GROUP BY query_name