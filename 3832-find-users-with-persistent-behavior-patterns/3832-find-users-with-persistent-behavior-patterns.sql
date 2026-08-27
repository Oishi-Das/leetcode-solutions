# Write your MySQL query statement below
WITH one_action AS (
    SELECT
        user_id,
        action_date,
        MAX(action) AS action
    FROM activity
    GROUP BY user_id, action_date
    HAVING COUNT(*) = 1
),
numbered AS (
    SELECT
        user_id,
        action,
        action_date,
        ROW_NUMBER() OVER (
            PARTITION BY user_id, action
            ORDER BY action_date
        ) AS rn
    FROM one_action
),
grouped AS (
    SELECT
        user_id,
        action,
        action_date,
        DATE_SUB(action_date, INTERVAL rn DAY) AS grp
    FROM numbered
),
streaks AS (
    SELECT
        user_id,
        action,
        COUNT(*) AS streak_length,
        MIN(action_date) AS start_date,
        MAX(action_date) AS end_date
    FROM grouped
    GROUP BY user_id, action, grp
),
best AS (
    SELECT
        user_id,
        action,
        streak_length,
        start_date,
        end_date,
        ROW_NUMBER() OVER (
            PARTITION BY user_id
            ORDER BY streak_length DESC, start_date ASC
        ) AS rn
    FROM streaks
)
SELECT
    user_id,
    action,
    streak_length,
    start_date,
    end_date
FROM best
WHERE rn = 1
  AND streak_length >= 5
ORDER BY
    streak_length DESC,
    user_id ASC;