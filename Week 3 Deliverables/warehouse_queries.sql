# Count competitors by vertical
SELECT vertical, COUNT(*) AS competitor_count
FROM competitors
GROUP BY vertical
ORDER BY competitor_count DESC;

# A list of countries and the number of products with indirect distribution channel ranked by maximum to minimum 
SELECT c.countryName, COUNT(*) AS indirect_distributors
FROM competitors cp
JOIN countries c ON cp.countryId = c.countryId
WHERE cp.distributionChannel = 'Indirect Distribution'
GROUP BY c.countryName
ORDER BY indirect_distributors DESC;

# A list of demographic indicators that are related to eldercare and from the year 2025
SELECT variable, value, unit, source
FROM demographic_indicators
WHERE vertical = 'Eldercare' AND year = 2025
ORDER BY variable;

# Compare direct vs indirect distribution by vertical
SELECT vertical, distributionChannel, COUNT(*) AS competitor_count
FROM competitors
GROUP BY vertical, distributionChannel
ORDER BY vertical;

# Find competitors operating in verticals with TAM data
SELECT cp.competitorName, cp.vertical
FROM competitors cp
WHERE cp.vertical IN (
    SELECT DISTINCT vertical
    FROM market_estimates
);

# Which country has the most diverse competitor portfolio?
SELECT c.countryName, COUNT(DISTINCT cp.vertical) AS verticals_represented
FROM competitors cp
JOIN countries c ON cp.countryId = c.countryId
GROUP BY c.countryName
ORDER BY verticals_represented DESC;

# Which vertical relies most on indirect distribution?
SELECT vertical, COUNT(*) AS indirect_count
FROM competitors
WHERE distributionChannel = 'Indirect Distribution'
GROUP BY vertical
ORDER BY indirect_count DESC;

# Which Eldercare demographic indicator has the highest percentage value?"
SELECT variable, value, unit, source
FROM demographic_indicators
WHERE vertical = 'Eldercare' AND unit = 'Percent'
ORDER BY value DESC
LIMIT 1;






