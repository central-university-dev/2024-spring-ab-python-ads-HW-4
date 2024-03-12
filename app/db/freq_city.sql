CREATE OR REPLACE FUNCTION most_frequent_city()
RETURNS TEXT AS $$
    from collections import Counter
    
    plan = plpy.prepare("SELECT city FROM requests", [])
    result = plpy.execute(plan)
    cities = [row['city'] for row in result]
    if len(cities) == 0:
        return ""
    city_counts = Counter(cities)
    most_common_city = city_counts.most_common(1)[0][0]

    return most_common_city
$$ LANGUAGE plpython3u;
