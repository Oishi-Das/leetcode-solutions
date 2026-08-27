# Write your MySQL query statement below
SELECT
    ip,
    COUNT(*) AS invalid_count
FROM logs
WHERE
    LENGTH(ip) - LENGTH(REPLACE(ip, '.', '')) <> 3
    OR ip REGEXP '(^|\\.)0[0-9]'
    OR EXISTS (
        SELECT 1
        FROM (
            SELECT CAST(SUBSTRING_INDEX(ip, '.', 1) AS UNSIGNED) AS octet
            UNION ALL
            SELECT CAST(SUBSTRING_INDEX(SUBSTRING_INDEX(ip, '.', 2), '.', -1) AS UNSIGNED)
            UNION ALL
            SELECT CAST(SUBSTRING_INDEX(SUBSTRING_INDEX(ip, '.', 3), '.', -1) AS UNSIGNED)
            UNION ALL
            SELECT CAST(SUBSTRING_INDEX(ip, '.', -1) AS UNSIGNED)
        ) x
        WHERE octet > 255
    )
GROUP BY ip
ORDER BY invalid_count DESC, ip DESC;