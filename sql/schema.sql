-- Schema for Retail ETL Project

CREATE TABLE customers (
    customer_id INT,
    customer_name STRING,
    city STRING
);

CREATE TABLE products (
    product_id INT,
    product_name STRING,
    category STRING
);

CREATE TABLE orders (
    order_id INT,
    customer_id INT,
    product_id INT,
    quantity INT,
    order_date DATE
);

CREATE TABLE fact_sales (
    order_id INT,
    customer_id INT,
    product_id INT,
    quantity INT,
    total_amount DOUBLE
);