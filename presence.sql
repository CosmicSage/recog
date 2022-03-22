CREATE TABLE presence (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    time_spent TEXT
);

INSERT INTO presence (id, name, time_spent) VALUES(abs(random()), 'Obama', '0s');
