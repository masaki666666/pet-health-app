CREATE TABLE health_log (
    id SERIAL PRIMARY KEY,
    pet_id INTEGER NOT NULL,
    record_date DATE NOT NULL,
    weight FLOAT NOT NULL,
    activity_level INTEGER NOT NULL,
    appetite_level INTEGER NOT NULL,
    coat_condition INTEGER NOT NULL,
    urine_condition INTEGER NOT NULL,
    feces_condition INTEGER NOT NULL,
    FOREIGN KEY (pet_id) REFERENCES pet_info(id)
);