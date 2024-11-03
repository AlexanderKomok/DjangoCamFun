CREATE TABLE cameras (
    id SERIAL PRIMARY KEY,
    name VARCHAR(20),
    ip_address VARCHAR(16),
    latitude DECIMAL(10, 8),
    longitude DECIMAL(11, 8)
);

CREATE TABLE plate_events (
    id SERIAL PRIMARY KEY,
    plate_number VARCHAR(8),
    brand VARCHAR(30),
    color VARCHAR(30),
    camera_id INTEGER REFERENCES cameras(id),
    recognition_time TIMESTAMP
);