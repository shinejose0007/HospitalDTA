
CREATE TABLE IF NOT EXISTS cohort (
    id SERIAL PRIMARY KEY,
    patient_id TEXT,
    visit_date DATE,
    age INT,
    gender TEXT,
    systolic INT,
    diastolic INT
);
