CREATE TABLE pet_images (
    id SERIAL PRIMARY KEY,
    pet_id INTEGER NOT NULL,
    image_path VARCHAR(255) NOT NULL,
    upload_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (pet_id) REFERENCES pet_info(id)
);