-- SRM Registration Form Database Queries
CREATE TABLE srm_responses (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(15),
    branch VARCHAR(50),
    year INTEGER,
    created_at TIMESTAMP
);

SELECT * FROM srm_responses;
SELECT * FROM srm_responses WHERE branch = 'CSE';
SELECT COUNT(*) FROM srm_responses;
