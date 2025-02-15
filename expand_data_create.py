import pandas as pd
from random import randint, choice
from datetime import datetime, timedelta

# Parameters for data generation
num_records = 2000  # Adjust this number to make the dataset larger or smaller
cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "San Diego", "Dallas", "San Francisco", "Miami", "Atlanta"]

# Define fixed prices for each product ID
product_price_map = {501: 20.00, 502: 15.50, 503: 22.75, 504: 18.30}
products = list(product_price_map.keys())

base_date = datetime.strptime("2023-01-01", "%Y-%m-%d")  # Start from January for a full-year dataset

# Create a list of dictionaries containing the data
data = []

for i in range(1, num_records + 1):
    order_id = i
    customer_id = randint(101, 110)
    product_id = choice(products)
    order_date = (base_date + timedelta(days=randint(0, 364))).strftime('%Y-%m-%d')  # Up to a full year
    quantity = randint(1, 10)
    price = product_price_map[product_id]  # Use fixed price from map
    city = choice(cities)
    
    data.append({
        "OrderID": order_id,
        "CustomerID": customer_id,
        "ProductID": product_id,
        "OrderDate": order_date,
        "Quantity": quantity,
        "Price": price,
        "City": city
    })

# Convert to DataFrame
df = pd.DataFrame(data)

# Display some sample records to verify
print(df.head())

# Optionally, export to a CSV if you need the data in a file
df.to_csv("new_data.csv", index=False)