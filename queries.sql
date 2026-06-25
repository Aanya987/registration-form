-- SRM Registration Form Database Queries
CREATE TABLE srm_responses (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(15),
    created_at TIMESTAMP
);
