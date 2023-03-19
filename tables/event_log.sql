CREATE TABLE event_log (
    id SERIAL PRIMARY KEY,
    pet_id INTEGER NOT NULL,
    event_type VARCHAR(255) NOT NULL,
    event_date DATE NOT NULL,
    notes TEXT,
    FOREIGN KEY (pet_id) REFERENCES pet_info(id)
);