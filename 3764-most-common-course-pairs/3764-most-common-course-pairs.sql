# Write your MySQL query statement below
WITH top_students AS (
    SELECT user_id
    FROM course_completions
    GROUP BY user_id
    HAVING COUNT(course_id) >= 5
       AND AVG(course_rating) >= 4
),
ranked_courses AS (
    SELECT
        c.user_id,
        c.course_name,
        ROW_NUMBER() OVER (
            PARTITION BY c.user_id
            ORDER BY c.completion_date, c.course_id
        ) AS rn
    FROM course_completions c
    JOIN top_students t
        ON c.user_id = t.user_id
)
SELECT
    c1.course_name AS first_course,
    c2.course_name AS second_course,
    COUNT(*) AS transition_count
FROM ranked_courses c1
JOIN ranked_courses c2
    ON c1.user_id = c2.user_id
   AND c2.rn = c1.rn + 1
GROUP BY
    c1.course_name,
    c2.course_name
ORDER BY
    transition_count DESC,
    first_course ASC,
    second_course ASC;