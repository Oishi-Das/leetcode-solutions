# Write your MySQL query statement below
WITH RECURSIVE EmployeeHierarchy AS (
    SELECT
        employee_id,
        employee_name,
        manager_id,
        salary,
        1 AS level
    FROM Employees
    WHERE manager_id IS NULL

    UNION ALL

    SELECT
        e.employee_id,
        e.employee_name,
        e.manager_id,
        e.salary,
        h.level + 1
    FROM Employees e
    JOIN EmployeeHierarchy h
        ON e.manager_id = h.employee_id
),

Subordinates AS (
    SELECT
        manager_id,
        employee_id,
        salary
    FROM Employees
    WHERE manager_id IS NOT NULL

    UNION ALL

    SELECT
        s.manager_id,
        e.employee_id,
        e.salary
    FROM Subordinates s
    JOIN Employees e
        ON e.manager_id = s.employee_id
),

TeamBudget AS (
    SELECT
        e.employee_id,
        COUNT(s.employee_id) AS team_size,
        COALESCE(SUM(s.salary), 0) + e.salary AS budget
    FROM Employees e
    LEFT JOIN Subordinates s
        ON e.employee_id = s.manager_id
    GROUP BY e.employee_id, e.salary
)

SELECT
    h.employee_id,
    h.employee_name,
    h.level,
    t.team_size,
    t.budget
FROM EmployeeHierarchy h
JOIN TeamBudget t
    ON h.employee_id = t.employee_id
ORDER BY h.level, t.budget DESC, h.employee_name;