# Write your MySQL query statement below
SELECT Customers.name AS Customers FROM Customers WHERE Customers.id not in (SELECT customerid FROM Orders);