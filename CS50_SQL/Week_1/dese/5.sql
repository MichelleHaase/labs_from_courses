SELECT COUNT(type LIKE '%public%'), city FROM schools WHERE type LIKE '%public%' GROUp BY city HAVING COUNT(type LIKE '%public%') <4 ORDER BY COUNT(type LIKE '%public%') DESC, city;
