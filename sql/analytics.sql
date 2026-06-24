-- Total Revenue
-- Problem: How much revenue has the business generated?

SELECT ROUND(SUM(total_amount), 2) AS total_revenue
FROM fact_sales;

-- Revenue by City
-- Problem: Which cities generate the most revenue?

SELECT
    city,
    ROUND(SUM(total_amount),2) AS total_revenue
FROM fact_sales
GROUP BY city
ORDER BY total_revenue DESC;

-- Revenue Category Classification
-- Problem: Classify orders into High, Medium, and Low value transactions.

SELECT
    CASE
        WHEN total_amount >= 1000 THEN 'High Value'
        WHEN total_amount >= 500 THEN 'Medium Value'
        ELSE 'Low Value'
    END AS order_category,
    COUNT(*) AS total_orders
FROM fact_sales
GROUP BY order_category;

-- Revenue by Product Category
-- Problem: Which product categories contribute the most revenue?

SELECT category_name, 
            ROUND(SUM(total_amount),2) AS total_revenue 
FROM fact_sales 
GROUP BY category_name 
ORDER BY total_revenue DESC;

-- Monthly Revenue Trend
-- Problem: Analyze revenue trends across months.

WITH monthly_sales AS (
    SELECT
        month,
        SUM(total_amount) AS revenue
    FROM fact_sales
    GROUP BY month
)

SELECT *
FROM monthly_sales
ORDER BY month;

-- Month-over-Month Revenue Comparison
-- Problem: Compare each month's revenue against the previous month.

WITH monthly_sales AS (
    SELECT
        month,
        SUM(total_amount) AS revenue
    FROM fact_sales
    GROUP BY month
)

SELECT
    month,
    revenue,
    LAG(revenue) OVER (ORDER BY month) AS previous_month_revenue,
    revenue - LAG(revenue) OVER (ORDER BY month) AS revenue_change
FROM monthly_sales;

-- Top Products Ranking
-- Problem: Rank products based on revenue generated.

WITH product_revenue AS (
    SELECT
        product_name,
        SUM(total_amount) AS revenue
    FROM fact_sales
    GROUP BY product_name
)

SELECT
    product_name,
    revenue,
    RANK() OVER (ORDER BY revenue DESC) AS product_rank
FROM product_revenue;

