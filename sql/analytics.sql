SELECT * FROM fact_sales LIMIT 5;

-- KPI 1: Total Revenue
SELECT ROUND(SUM(total_amount),2) AS total_revenue
FROM fact_sales;

-- KPI 2: Revenue by City
SELECT city, ROUND(SUM(total_amount),2) AS total_revenue
FROM fact_sales
GROUP BY city
ORDER BY total_revenue DESC;

-- KPI 3: Revenue by Product Category
SELECT category_name, ROUND(SUM(total_amount),2) AS total_revenue
FROM fact_sales
GROUP BY category_name
ORDER BY total_revenue DESC;

-- Monthly Revenue Trend
SELECT month, ROUND(SUM(total_amount),2) AS monthly_revenue
FROM fact_sales 
GROUP BY month
ORDER BY month;

-- Top 10 Products by 
SELECT product_name, ROUND(SUM(total_amount),2) AS revenue
FROM fact_sales
GROUP BY product_name
ORDER BY revenue DESC
LIMIT 10;

-- Top 10 Products by Quantity Sold
SELECT product_name, ROUND(SUM(total_amount),2) AS revenue
FROM fact_sales
GROUP BY product_name
ORDER BY revenue DESC
LIMIT 10;

-- Average Order Value
SELECT ROUND(AVG(total_amount),2) AS average_order_value
FROM fact_sales;