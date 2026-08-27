# Write your MySQL query statement below
WITH reaction_counts AS (
    SELECT
        user_id,
        reaction,
        COUNT(*) AS reaction_count
    FROM reactions
    GROUP BY user_id, reaction
),
user_totals AS (
    SELECT
        user_id,
        COUNT(*) AS total_reactions,
        COUNT(DISTINCT content_id) AS content_count
    FROM reactions
    GROUP BY user_id
),
ranked AS (
    SELECT
        user_id,
        reaction,
        reaction_count,
        ROW_NUMBER() OVER (
            PARTITION BY user_id
            ORDER BY reaction_count DESC, reaction ASC
        ) AS rn
    FROM reaction_counts
)
SELECT
    r.user_id,
    r.reaction AS dominant_reaction,
    ROUND(r.reaction_count / u.total_reactions, 2) AS reaction_ratio
FROM ranked r
JOIN user_totals u
    ON r.user_id = u.user_id
WHERE r.rn = 1
  AND u.content_count >= 5
  AND r.reaction_count / u.total_reactions >= 0.60
ORDER BY
    reaction_ratio DESC,
    r.user_id ASC;