# Write your MySQL query statement below
WITH FirstPositive AS (
    SELECT
        patient_id,
        MIN(test_date) AS positive_date
    FROM covid_tests
    WHERE result = 'Positive'
    GROUP BY patient_id
),
FirstNegative AS (
    SELECT
        c.patient_id,
        MIN(c.test_date) AS negative_date
    FROM covid_tests c
    JOIN FirstPositive p
        ON c.patient_id = p.patient_id
        AND c.test_date > p.positive_date
    WHERE c.result = 'Negative'
    GROUP BY c.patient_id
)
SELECT
    p.patient_id,
    p.patient_name,
    p.age,
    DATEDIFF(n.negative_date, fp.positive_date) AS recovery_time
FROM FirstPositive fp
JOIN FirstNegative n
    ON fp.patient_id = n.patient_id
JOIN patients p
    ON fp.patient_id = p.patient_id
ORDER BY recovery_time ASC, p.patient_name ASC;