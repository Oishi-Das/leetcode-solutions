# Write your MySQL query statement below
WITH latest AS (
    SELECT
        user_id,
        plan_name AS current_plan,
        monthly_amount AS current_monthly_amount,
        event_date AS last_date,
        ROW_NUMBER() OVER (
            PARTITION BY user_id
            ORDER BY event_date DESC, event_id DESC
        ) AS rn
    FROM subscription_events
),
history AS (
    SELECT
        user_id,
        MIN(event_date) AS first_date,
        MAX(monthly_amount) AS max_historical_amount,
        SUM(event_type = 'downgrade') AS downgrade_count
    FROM subscription_events
    GROUP BY user_id
)
SELECT
    l.user_id,
    l.current_plan,
    l.current_monthly_amount,
    h.max_historical_amount,
    DATEDIFF(l.last_date, h.first_date) AS days_as_subscriber
FROM latest l
JOIN history h
    ON l.user_id = h.user_id
WHERE l.rn = 1
  AND l.current_plan IS NOT NULL
  AND h.downgrade_count > 0
  AND l.current_monthly_amount < h.max_historical_amount * 0.5
  AND DATEDIFF(l.last_date, h.first_date) >= 60
ORDER BY
    days_as_subscriber DESC,
    l.user_id ASC;