CREATE TABLE tree_requests_log (
    id SERIAL PRIMARY KEY,
    city VARCHAR(255),
    country VARCHAR(255),
    year INT,
    tree_count INT,
    query_date TIMESTAMP
);