CREATE DATABASE IF NOT EXISTS plate_test;

\c plate_test;

CREATE TABLE IF NOT EXISTS cameras (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    ip_address VARCHAR(45),
    latitude DECIMAL(10, 8),
    longitude DECIMAL(11, 8)
);


CREATE TABLE IF NOT EXISTS plate_events (
    id SERIAL PRIMARY KEY,
    plate_number VARCHAR(15),
    brand VARCHAR(50),
    color VARCHAR(30),
    camera_id INTEGER REFERENCES cameras(id),
    recognition_time TIMESTAMP
);
