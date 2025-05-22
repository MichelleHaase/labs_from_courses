SELECT SUM(performances.H) AS "total hits", teams.name FROM performances
    JOIN teams ON performances.team_id = teams.id
    WHERE performances.year = 2001 GROUP BY teams.name ORDER BY "total hits" DESC LIMIT 5;
