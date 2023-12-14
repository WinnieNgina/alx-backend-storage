-- Calculate life time of bands that have Glam rock as their main style 
SELECT 
    band_name, 
    IFNULL(split - formed, 2022 - formed) AS lifespan
FROM 
    metal_bands
WHERE 
    style LIKE '%Glam rock%'
ORDER BY 
    lifespan DESC;
