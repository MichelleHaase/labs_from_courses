SELECT COUNT(type LIKE '%public%'), city FROM schools WHERE type LIKE '%public%' GROUp BY city ORDER BY COUNT(type LIKE '%public%') DESC, city LIMIT 10;
