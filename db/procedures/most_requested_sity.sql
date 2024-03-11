CREATE OR REPLACE FUNCTION most_requested_city()
RETURNS TABLE(city VARCHAR, requests_count BIGINT) AS $$
BEGIN
    RETURN QUERY
    SELECT city, COUNT(*) AS requests_count FROM requests GROUP BY city ORDER BY requests_count DESC LIMIT 1;
END;
$$ LANGUAGE plpgsql;