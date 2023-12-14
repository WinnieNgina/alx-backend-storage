--  SQL script that ranks country origins of bands
-- Ordered by the number of (non-unique) fans
SELECT
    origin,
    SUM(fans) AS nb_fans
FROM
    metal_bands
GROUP by
    origin
ORDER by
    nb_fans DESC;