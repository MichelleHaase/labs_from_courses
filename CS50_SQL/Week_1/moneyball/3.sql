SELECT HR, year FROM performances WHERE player_id = (SELECT id FROM players WHERE first_name LIKE 'KEN' AND last_name LIKE 'Griffey' AND birth_year = 1969) ORDER BY year DESC;
