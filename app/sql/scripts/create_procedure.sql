CREATE OR REPLACE FUNCTION most_common_city()
RETURNS TABLE(city VARCHAR, count BIGINT) AS $$
BEGIN
    RETURN QUERY
    SELECT requests_log.city, COUNT(*) AS count_value
    FROM requests_log
    GROUP BY requests_log.city
    ORDER BY count_value DESC
    LIMIT 1;
END;
$$ LANGUAGE plpgsql;