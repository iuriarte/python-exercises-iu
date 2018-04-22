Query 1:
SELECT * FROM restaurant WHERE stars > 4.5;

Query 2:
SELECT * FROM restaurant favoritedish;

Query 3:
SELECT * FROM restaurant WHERE name = 'moontower';

Query 4:
SELECT * FROM restaurant WHERE category = 'bbq';

Query 5:
SELECT * FROM restaurant WHERE takeout = TRUE;

Query 6:
SELECT * FROM restaurant WHERE takeout = TRUE AND category = 'bbq';

Query 7:
SELECT * FROM restaurant WHERE distance <= 2;

Query 8:
SELECT * FROM restaurant WHERE '2017-03-21T00:00:00Z'> lasttimeyouatethere AND lasttimeyouatethere <'2017-03-31T00:00:00Z' ;

Query 9:
SELECT * FROM restaurant WHERE '2017-03-21T00:00:00Z'> lasttimeyouatethere AND lasttimeyouatethere <'2017-03-31T00:00:00Z'AND stars = 5 ;
