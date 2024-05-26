-- Displays the 3 cities with the highest average.
-- Temperatures between July and August
SELECT city, AVG(value) AS avg-temp
FROM temperature
WHERE month = 7 or month = 8
GROUP BY city
ORDER BY avg-temp DESC
limit 3;
