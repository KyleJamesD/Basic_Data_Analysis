
import pandas as pd
from random import randint, choice
from datetime import datetime, timedelta

# Parameters for data generation
num_records = 1000  # Adjust this number to make the dataset larger or smaller
cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "San Diego", "Dallas", "San Francisco", "Miami", "Atlanta"]
products = [501, 502, 503, 504]
base_date = datetime.strptime("2023-05-01", "%Y-%m-%d")

# Create a list of dictionaries containing the data
data = []

for i in range(1, num_records + 1):
    order_id = i
    customer_id = randint(101, 110)
    product_id = choice(products)
    order_date = (base_date + timedelta(days=randint(0, 100))).strftime('%Y-%m-%d')
    quantity = randint(1, 10)
    price = round(randint(5, 25) + randint(0, 99) / 100, 2)
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
print(df)

# Optionally, export to a CSV if you need the data in a file
df.to_csv("data.csv", index=False)