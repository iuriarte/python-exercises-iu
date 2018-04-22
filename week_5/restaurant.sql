CREATE TABLE restaurant (
id SERIAL NOT NULL PRIMARY KEY,
name VARCHAR,
distance FLOAT,
stars FLOAT,
category VARCHAR,
favoritedish VARCHAR,
takeout BOOLEAN,
lasttimeyouatethere DATE

);