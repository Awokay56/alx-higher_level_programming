-- Displays the max temperature of each state, order by state name.
SELECT state, MAX(value) AS max_temperature
FROM temperature
GROUP BY state;
