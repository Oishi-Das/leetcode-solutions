# Write your MySQL query statement below
WITH user_avg AS (
    SELECT
        user_id,
        COUNT(*) AS prompt_count,
        AVG(tokens) AS avg_tokens
    FROM prompts
    GROUP BY user_id
)
SELECT
    p.user_id,
    a.prompt_count,
    ROUND(a.avg_tokens, 2) AS avg_tokens
FROM prompts p
JOIN user_avg a
    ON p.user_id = a.user_id
WHERE a.prompt_count >= 3
GROUP BY
    p.user_id,
    a.prompt_count,
    a.avg_tokens
HAVING MAX(p.tokens) > a.avg_tokens
ORDER BY
    a.avg_tokens DESC,
    p.user_id ASC;