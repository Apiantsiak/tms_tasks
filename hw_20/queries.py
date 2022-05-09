
from typing import Dict

QUERIES: Dict[str, str] = dict()

QUERIES['company_employees_london_speedy_exp'] = """
SELECT c.company_name AS "Company name",
    CONCAT(e.first_name, ' ', e.last_name) AS "Full name"
FROM customers AS c
    INNER JOIN orders AS o ON c.customer_id = o.customer_id
    INNER JOIN employees AS e ON o.employee_id = e.employee_id
    INNER JOIN shippers AS s ON o.ship_via = s.shipper_id
WHERE c.city = 'London'
    AND e.city = 'London'
    AND s.company_name = 'Speedy Express';
"""

QUERIES['customers_without_orders'] = """
SELECT c.company_name, c.customer_id
FROM customers AS c
WHERE c.customer_id NOT IN(
    SELECT orders.customer_id FROM orders
    );
"""

QUERIES['active_products_condiments_meat_poultry_less_100'] = """
SELECT p.product_name, p.units_in_stock, s.contact_name, s.phone
FROM products AS p
    INNER JOIN suppliers AS s ON p.supplier_id = s.supplier_id
    INNER JOIN categories AS c ON p.category_id = c.category_id
WHERE p.discontinued = 0
    AND p.units_in_stock < 100
    AND c.category_name IN ('Condiments', 'Meat/Poultry');
"""

QUERIES['number_of_goods_in_categories'] = """
SELECT c.category_name, COUNT(p.product_name) AS "Number of goods"
FROM products AS p
    INNER JOIN categories AS c ON p.category_id = c.category_id
GROUP BY c.category_name
ORDER BY "Number of goods" DESC;
"""
