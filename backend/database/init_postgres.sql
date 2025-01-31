CREATE DATABASE tax_database;

CREATE TABLE tax_data (
    id SERIAL PRIMARY KEY,
    document_text TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
