CREATE TABLE IF NOT EXISTS requests_log (
    id SERIAL PRIMARY KEY,
    city VARCHAR(255) NOT NULL,
    country VARCHAR(255) NOT NULL,
    year INT NOT NULL,
    trees_count INT
);

