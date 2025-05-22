SELECT teams.name FROM performances
    JOIN teams on performances.team_id = teams.id
        JOIN players ON performances.player_id = players.id
        WHERE performances.player_id = (SELECT id FROM players WHERE first_name LIKE 'Satchel' AND last_name LIKE 'Paige');
