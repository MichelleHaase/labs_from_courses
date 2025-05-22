
-- *** The Lost Letter ***
-- name: Anneke address: 900 Somerville Avenue letter for: Varsha at 2 Finnegan Street, upotown( might be wrong)
SELECT contents from packages where contents Like '%letter%'; -- check if contents letter exists

SELECT id FROM packages
where contents Like '%letter%' AND
from_address_id = (SELECT id FROM addresses WHERE "address" like '900 Somerville Avenue'); -- two entries

SELECT id FROM packages
where contents Like '%Congratulatory letter%' AND
from_address_id = (SELECT id FROM addresses WHERE "address" like '900 Somerville Avenue');-- 384

SELECT * from scans WHERE package_id = (SELECT id FROM packages
where contents Like '%Congratulatory letter%' AND
from_address_id = (SELECT id FROM addresses WHERE "address" like '900 Somerville Avenue')); -- checking if the letter got droped off

SELECT * FROM addresses where id = (SELECT address_id from scans WHERE package_id = (SELECT id FROM packages
where contents Like '%Congratulatory letter%' AND
from_address_id = (SELECT id FROM addresses WHERE "address" like '900 Somerville Avenue')) AND "action" LIKE 'Drop'); --  finding the drop off address

-- *** The Devious Delivery ***
-- fiftyville box NO FROM
SELECT * FROM packages
WHERE from_address_id IS NULL; -- Duck debugger

SELECT * FROM addresses
WHERE id =
(SELECT to_address_id FROM packages
    WHERE from_address_id IS NULL); -- address where it landed not right according to check 50

SELECT address_id FROM scans
WHERE action LIKE 'Drop'
AND package_id =
    (SELECT id FROM packages
    WHERE from_address_id IS NULL); -- drop off id where it was dropped of not send

SELECT * FROM addresses
WHERE id =
    (SELECT address_id FROM scans
    WHERE action LIKE 'Drop'
    AND package_id =
        (SELECT id FROM packages
        WHERE from_address_id IS NULL));

-- *** The Forgotten Gift ***
-- mystery gift to: 728 Maple Place, 2 weeks ago, from: 109 Tileston Street
SELECT * FROM packages WHERE from_address_id = (
    SELECT id FROM addresses WHERE address LIKE '109 Tileston Street')
    AND to_address_id = (
        SELECT id FROM addresses WHERE address LIKE '728 Maple Place'
    ); -- finding the package

SELECT * FROM addresses WHERE id = (
    SELECT to_address_id FROM packages WHERE from_address_id = (
    SELECT id FROM addresses WHERE address LIKE '109 Tileston Street')
    AND to_address_id = (
        SELECT id FROM addresses WHERE address LIKE '728 Maple Place'
    )
); -- the drop off address

-- was picked up again
SELECT driver_id FROM scans WHERE action LIKE 'Pick' AND timestamp > '2023-08-16%' AND package_id = (SELECT id FROM packages WHERE from_address_id = (
    SELECT id FROM addresses WHERE address LIKE '109 Tileston Street')
    AND to_address_id = (
        SELECT id FROM addresses WHERE address LIKE '728 Maple Place'
    )); -- driver id who picked it up again

SELECT name FROM drivers WHERE id = (SELECT driver_id FROM scans WHERE action LIKE 'Pick' AND timestamp > '2023-08-16%' AND package_id = (SELECT id FROM packages WHERE from_address_id = (
    SELECT id FROM addresses WHERE address LIKE '109 Tileston Street')
    AND to_address_id = (
        SELECT id FROM addresses WHERE address LIKE '728 Maple Place'
    ))); -- driver who currently has package
