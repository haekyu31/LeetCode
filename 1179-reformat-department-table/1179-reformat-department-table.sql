# Write your MySQL query statement below
SELECT
  Ids.id,
  January.revenue AS Jan_Revenue,
  Feburary.revenue AS Feb_Revenue,
  March.revenue AS Mar_Revenue,
  April.revenue AS Apr_Revenue,
  May.revenue AS May_Revenue,
  June.revenue AS Jun_Revenue,
  July.revenue AS Jul_Revenue,
  August.revenue AS Aug_Revenue,
  September.revenue AS Sep_Revenue,
  October.revenue AS Oct_Revenue,
  November.revenue AS Nov_Revenue,
  December.revenue AS Dec_Revenue
FROM
  (
    SELECT DISTINCT
      id
    FROM
      Department
  ) AS Ids
  LEFT JOIN Department AS January ON (
    Ids.id = January.id
    AND January.month = "Jan"
  )
  LEFT JOIN Department AS Feburary ON (
    Ids.id = Feburary.id
    AND Feburary.month = "Feb"
  )
  LEFT JOIN Department AS March ON (
    Ids.id = March.id
    AND March.month = "Mar"
  )
  LEFT JOIN Department AS April ON (
    Ids.id = April.id
    AND April.month = "Apr"
  )
  LEFT JOIN Department AS May ON (
    Ids.id = May.id
    AND May.month = "May"
  )
  LEFT JOIN Department AS June ON (
    Ids.id = June.id
    AND June.month = "Jun"
  )
  LEFT JOIN Department AS July ON (
    Ids.id = July.id
    AND July.month = "Jul"
  )
  LEFT JOIN Department AS August ON (
    Ids.id = August.id
    AND August.month = "Aug"
  )
  LEFT JOIN Department AS September ON (
    Ids.id = September.id
    AND September.month = "Sep"
  )
  LEFT JOIN Department AS October ON (
    Ids.id = October.id
    AND October.month = "Oct"
  )
  LEFT JOIN Department AS November ON (
    Ids.id = November.id
    AND November.month = "Nov"
  )
  LEFT JOIN Department AS December ON (
    Ids.id = December.id
    AND December.month = "Dec"
  );