# Write your MySQL query statement below
SELECT a.Name AS 'Employee' FROM Employee AS a, Employee AS b WHERE a.ManagerID = b.Id AND a.Salary > b.Salary;