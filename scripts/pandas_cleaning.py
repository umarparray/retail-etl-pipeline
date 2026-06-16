#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd


df = pd.read_csv("../data/raw/online-retail.csv")

#fill missing values in column gender by UNKNOWN
df["gender"] = df["gender"].fillna("Unknown")

#fill missing values in column gender by 'NO Review'
df["review_score"] = df["review_score"].fillna("No Review")

#Convert order date type
df["order_date"] = pd.to_datetime(df["order_date"])



/Users/imran/Downloads/step2_pandas_load.py


# In[5]:


# Create Revenue Column
df["total_amount"] = df["quantity"] * df["price"]

# Extract Date Features
df["year"] = df["order_date"].dt.year
df["month"] = df["order_date"].dt.month
df["day"] = df["order_date"].dt.day


# In[13]:


#Create Customers Table
customers = df[["customer_id", "gender", "age", "city"]].drop_duplicates()

#Create PRODUCTS TABLE
products = df[[
    "product_id",
    "product_name",
    "category_id",
    "category_name",
    "price"
]].drop_duplicates()

#Create ORDERS TABLE

orders = df[[
    "customer_id", "product_id", "order_date",
    "quantity", "total_amount", "payment_method",
    "year", "month", "day"
]].drop_duplicates()


# In[17]:


#Save tables as customers.csv, products.csv, orders.csv
customers.to_csv("../data/cleaned/customers.csv", index=False)
products.to_csv("../data/cleaned/products.csv", index=False)
orders.to_csv("../data/cleaned/orders.csv", index=False)


# In[ ]:




