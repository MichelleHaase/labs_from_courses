SELECT ROUND(AVG(salary),2) AS 'Average salary', year FROM salaries GROUP BY year ORDER BY year DESC;
