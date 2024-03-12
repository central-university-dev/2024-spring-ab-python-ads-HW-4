CREATE EXTENSION IF NOT EXISTS plpython3u;

CREATE TABLE post_information (
    id SERIAL PRIMARY KEY,
    city VARCHAR(255),
    country VARCHAR(255),
    year INT,
    trees_count INT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE OR REPLACE FUNCTION most_frequent_city() RETURNS TABLE(city VARCHAR, queries_count bigint) AS $$ BEGIN RETURN QUERY
SELECT t.city,
    COUNT(*) as queries_count
FROM "Trees" t
GROUP BY t.city
ORDER BY queries_count DESC
LIMIT 1;
END;
$$ LANGUAGE plpgsql;
