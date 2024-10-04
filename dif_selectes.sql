# BAD ONE


SELECT c.name, c.surname, o.order_id, p.product_name, p.product_category
FROM opt_clients c
JOIN opt_orders o ON c.id = o.client_id
JOIN opt_products p ON o.product_id = p.product_id
WHERE p.product_category = (
    SELECT product_category
    FROM opt_products
    GROUP BY product_category
    ORDER BY COUNT(*) DESC
    LIMIT 1
)
ORDER BY o.order_date DESC;



SELECT COUNT(*) FROM opt_clients;
SELECT COUNT(*) FROM opt_orders;
SELECT COUNT(*) FROM opt_products;

# INDEXES

CREATE INDEX idx_opt_orders_client_id ON opt_orders(client_id);
CREATE INDEX idx_opt_orders_product_id ON opt_orders(product_id);
CREATE INDEX idx_opt_products_product_id ON opt_products(product_id);



SELECT c.name, c.surname, COUNT(DISTINCT p.product_category) AS distinct_categories
FROM opt_clients c
JOIN opt_orders o ON c.id = o.client_id
JOIN opt_products p ON o.product_id = p.product_id
GROUP BY c.id
HAVING COUNT(o.order_id) > 1
ORDER BY distinct_categories DESC;



# EXAMPLE WITH CTE

WITH client_top_category AS (
    SELECT o.client_id, p.product_category, COUNT(*) AS category_order_count
    FROM opt_orders o
    JOIN opt_products p ON o.product_id = p.product_id
    GROUP BY o.client_id, p.product_category
)

SELECT c.name, c.surname, ctc.product_category, ctc.category_order_count
FROM opt_clients c
JOIN client_top_category ctc ON c.id = ctc.client_id
WHERE ctc.category_order_count > 1
ORDER BY ctc.category_order_count DESC;





