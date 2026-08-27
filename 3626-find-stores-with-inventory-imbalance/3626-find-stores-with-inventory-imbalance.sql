# Write your MySQL query statement below
WITH store_products AS (
    SELECT
        i.*,
        COUNT(*) OVER (PARTITION BY store_id) AS product_count,
        MAX(price) OVER (PARTITION BY store_id) AS max_price,
        MIN(price) OVER (PARTITION BY store_id) AS min_price
    FROM inventory i
),
store_data AS (
    SELECT
        store_id,
        MAX(CASE WHEN price = max_price THEN product_name END) AS most_exp_product,
        MAX(CASE WHEN price = max_price THEN quantity END) AS expensive_quantity,
        MAX(CASE WHEN price = min_price THEN product_name END) AS cheapest_product,
        MAX(CASE WHEN price = min_price THEN quantity END) AS cheapest_quantity,
        MAX(product_count) AS product_count
    FROM store_products
    GROUP BY store_id
)
SELECT
    s.store_id,
    s.store_name,
    s.location,
    d.most_exp_product,
    d.cheapest_product,
    ROUND(d.cheapest_quantity / d.expensive_quantity, 2) AS imbalance_ratio
FROM store_data d
JOIN stores s
    ON d.store_id = s.store_id
WHERE d.product_count >= 3
  AND d.expensive_quantity < d.cheapest_quantity
ORDER BY
    imbalance_ratio DESC,
    s.store_name ASC;