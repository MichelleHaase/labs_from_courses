CREATE TABLE IF NOT EXISTS phrases(
    id INTEGER PRIMARY KEY,
    id_old INTEGER,
    substring TEXT,
    FOREIGN KEY(id_old) REFERENCES sentences(id)
);
INSERT INTO phrases (id_old, substring)
VALUES (14, (
    SELECT SUBSTR(sentence, 98, 4) FROM sentences WHERE id= 14)),
    (114, (
    SELECT SUBSTR(sentence, 3, 5) FROM sentences WHERE id= 114)),
    (618, (
    SELECT SUBSTR(sentence, 72, 9) FROM sentences WHERE id= 618)),
    (630, (
    SELECT SUBSTR(sentence, 7, 3) FROM sentences WHERE id= 630)),
    (932, (
    SELECT SUBSTR(sentence, 12, 5) FROM sentences WHERE id= 932)),
    (2230, (
    SELECT SUBSTR(sentence, 50, 7) FROM sentences WHERE id= 2230)),
    (2346, (
    SELECT SUBSTR(sentence, 44, 10) FROM sentences WHERE id= 2346)),
    (3041, (
    SELECT SUBSTR(sentence, 14, 5) FROM sentences WHERE id= 3041));



CREATE VIEW message AS
SELECT substring AS phrase FROM phrases ORDER BY id;
