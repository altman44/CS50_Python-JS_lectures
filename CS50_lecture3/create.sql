-- SQL Shell (psql):
-- database: postgres
-- \d    -- to see the List of relations
-- \c name_database  -- in order to entry in that database

-- Created two databases (default: postgres (user: postgres); new one: cs50(user: me))
-- Both have the same tables with different values in their fields

CREATE TABLE flights (
    id SERIAL PRIMARY KEY,
    origin VARCHAR NOT NULL,
    destination VARCHAR NOT NULL,
    duration INTEGER NOT NULL
);

-- Foreign Keys
-- REFERENCES: generally speaking, references the primary key
CREATE TABLE passengers (
    id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL,
    flight_id INTEGER NOT NULL REFERENCES flights
);

-- INSERTS
INSERT INTO flights (origin, destination, duration) VALUES ('Paris', 'Shanghai', 620);
INSERT INTO flights (origin, destination, duration) VALUES ('Moscow', 'New York', 1300);
INSERT INTO flights (origin, destination, duration) VALUES ('London', 'Lima', 1400);
INSERT INTO flights (origin, destination, duration) VALUES ('Buenos Aires', 'Istanbul', 1500);
INSERT INTO flights (origin, destination, duration) VALUES ('Dubai', 'Washington', 700);
INSERT INTO flights (origin, destination, duration) VALUES ('Tokyo', 'London', 650);
INSERT INTO flights (origin, destination, duration) VALUES ('London', 'Washington', 500);
INSERT INTO flights (origin, destination, duration) VALUES ('London', 'Paris', 340);
INSERT INTO flights (origin, destination, duration) VALUES ('Moscow', 'Washington', 1000);
INSERT INTO flights (origin, destination, duration) VALUES ('Washington', 'Shanghai', 200);
INSERT INTO flights (origin, destination, duration) VALUES ('Dubai', 'Buenos Aires', 600);
INSERT INTO flights (origin, destination, duration) VALUES ('Tokyo', 'Paris', 1200);


INSERT INTO passengers (name, flight_id) VALUES ('Alice', 1);
INSERT INTO passengers (name, flight_id) VALUES ('Mia', 7);
INSERT INTO passengers (name, flight_id) VALUES ('Fred', 7);
INSERT INTO passengers (name, flight_id) VALUES ('Thomas', 8);
INSERT INTO passengers (name, flight_id) VALUES ('Jennifer', 4);
INSERT INTO passengers (name, flight_id) VALUES ('Chris', 6);
INSERT INTO passengers (name, flight_id) VALUES ('Mary', 1);
INSERT INTO passengers (name, flight_id) VALUES ('Joe', 1);
INSERT INTO passengers (name, flight_id) VALUES ('Milton', 4);
INSERT INTO passengers (name, flight_id) VALUES ('Pete', 10);
INSERT INTO passengers (name, flight_id) VALUES ('Oswald', 9);
INSERT INTO passengers (name, flight_id) VALUES ('Bruce', 9);
INSERT INTO passengers (name, flight_id) VALUES ('Moe', 10);
INSERT INTO passengers (name, flight_id) VALUES ('Lisa', 3);
INSERT INTO passengers (name, flight_id) VALUES ('Joe', 3);
INSERT INTO passengers (name, flight_id) VALUES ('Joe', 3);
INSERT INTO passengers (name, flight_id) VALUES ('Mary', 5);
INSERT INTO passengers (name, flight_id) VALUES ('Thomas', 6);
INSERT INTO passengers (name, flight_id) VALUES ('Chris', 6);
INSERT INTO passengers (name, flight_id) VALUES ('Chris', 5);




-- SELECT 
SELECT * FROM flights; 
SELECT * FROM flights WHERE origin = 'New York';  -- single quote!
SELECT origin FROM flights WHERE duration > 1000;
SELECT origin, destination FROM flights;
SELECT * FROM flights WHERE id > 3 OR destination = 'New York';
-- SELECT with functions
SELECT AVG(duration) FROM flights;  -- get the average
SELECT COUNT(*) FROM flights;  -- get how many rows are
SELECT MIN(duration) FROM flights WHERE duration > 700;
SELECT * FROM flights WHERE origin LIKE '%a%'; -- get the rows in which the origin field matches with 'a' (even if it is just a substring)
SELECT SUM(duration) FROM flights;
SELECT * FROM flights LIMIT 2; -- get just the first 2 rows
SELECT * FROM flights ORDER BY duration ASC LIMIT 3; --get the first 3 rows it catches in an ascending order
SELECT origin, COUNT(*) FROM flights GROUP BY origin; --GROUP BY origin  takes all of the rows and puts them in groups based on their origin
SELECT origin, COUNT(*) FROM flights GROUP BY origin HAVING COUNT(*) > 1;
--SELECT with JOIN
SELECT origin, destination, name FROM flights JOIN passengers ON passengers.flight_id = flights.id;
SELECT origin, destination, name FROM flights JOIN passengers ON passengers.flight_id = flights.id WHERE destination = 'London';
SELECT origin, destination, name FROM flights LEFT JOIN passengers ON passengers.flight_id = flights.id;
SELECT flight_id FROM passengers GROUP BY flight_id HAVING COUNT(*) > 1;
SELECT * FROM flights WHERE id IN (SELECT flight_id FROM passengers GROUP BY flight_id HAVING COUNT(*) > 1);

-- UPDATE
UPDATE flights 
    SET duration = 430
    WHERE origin = 'Paris'
    AND destination = 'Shanghai';

-- DELETE
DELETE FROM flights
    WHERE origin = 'Tokyo';

-- Race Conditions
-- Injection
-- SQL Transactions
--  .BEGIN
--  .Commit