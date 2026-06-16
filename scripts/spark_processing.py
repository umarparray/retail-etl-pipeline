# Databricks notebook source
# STEP 1: Load Customers Dataset
# Purpose: Read customer master data from Unity Catalog Volume

customers = spark.read.csv(
    "/Volumes/workspace/default/firstlecture/cleaned/customers.csv",
    header=True,        # first row contains column names
    inferSchema=True    # automatically detect data types
)

# Display sample records to verify data load
customers.show(5)

# Print schema to confirm column types
customers.printSchema()


customers.columns



# COMMAND ----------

# STEP 2: Load Products Dataset
# Purpose: Contains product master information like category, price
products = spark.read.csv(
    "/Volumes/workspace/default/firstlecture/cleaned/products.csv",
    header=True,
    inferSchema=True
)

# Preview data
products.show(5)

# Schema validation
products.printSchema()


# COMMAND ----------


# STEP 3: Load Orders Dataset
# Purpose: Transactional data (core dataset for analytics)


orders = spark.read.csv(
    "/Volumes/workspace/default/firstlecture/cleaned/orders.csv",
    header=True,
    inferSchema=True
)

# Preview orders
orders.show(5)

# Check schema
orders.printSchema()

orders.columns

# COMMAND ----------

# STEP 4: Data Validation Check
# Purpose: Ensure data loaded correctly before transformations

print("Customers count:", customers.count())
print("Products count:", products.count())
print("Orders count:", orders.count())

# COMMAND ----------

# STEP 5.1: JOIN
# Purpose: Combine orders and customers

orders_customers = orders.join(
    customers,
    on="customer_id",
    how="left"
)

# STEP 5.2: Join with products
fact_table = orders_customers.join(
    products,
    on="product_id",
    how="left"
)

# STEP 4.3: Create Final Fact Table
# Purpose: Keep only business-relevant columns
fact_sales = fact_table.select(

    "product_id", "customer_id", "order_date",
    "quantity", "total_amount", "payment_method",
    "year", "month", "day","gender", "age", "city",
    "product_name", "category_id", "category_name","price"

)
fact_sales.show(5)



# COMMAND ----------

from pyspark.sql.functions import sum

# STEP 6.1: Total Revenue
fact_sales.agg(
    sum("total_amount").alias("total_revenue")
).show()



#STEP 6.2: Revenue by City
fact_sales.groupBy("city").agg(
    sum("total_amount").alias("city_revenue")
).orderBy("city_revenue", ascending=False).show(10)


# STEP 6.3: Top Selling Products
fact_sales.groupBy("product_name").agg(
    sum("total_amount").alias("revenue")
).orderBy("revenue", ascending=False).show(10)

# STEP 6.4: BONUS KPI: Top Products by Units Sold
# Purpose: Find most purchased products
fact_sales.groupBy("product_name") \
    .agg(sum("quantity").alias("units_sold")) \
    .orderBy("units_sold", ascending=False) \
    .show(10)

# COMMAND ----------

#STEP 7: Save as csv

fact_sales.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("workspace.default.fact_sales")

# COMMAND ----------

fact_sales.head(5)

# COMMAND ----------

fact_sales.columns

# COMMAND ----------

