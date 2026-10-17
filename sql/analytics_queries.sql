-- Query 1
-- Business Question:
-- Which vendor generated the highest total revenue?

SELECT 
    "VendorID",
    SUM(total_amount) AS total_revenue,
    COUNT(*) AS total_trips
FROM trips
GROUP BY "VendorID"
ORDER BY total_revenue DESC;


-- Query 2
-- Business Question:
-- What is the average fare and average distance for each passenger count?

SELECT
    passenger_count,
    COUNT(*) AS total_trips,
    AVG(fare_amount) AS average_fare,
    AVG(trip_distance) AS average_distance
FROM trips
GROUP BY passenger_count
ORDER BY passenger_count;


-- Query 3
-- Business Question:
-- What are the top 10 longest trips based on trip duration?

SELECT
    "VendorID",
    passenger_count,
    trip_distance,
    fare_amount,
    total_amount,
    trip_duration_minutes,
    RANK() OVER (
        ORDER BY trip_duration_minutes DESC
    ) AS duration_rank
FROM trips
ORDER BY duration_rank
LIMIT 10;
