import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("sales_data.csv")

# Display data
print(df.head())

# Summary
print(df.describe())

# Total sales by category
category_sales = df.groupby("Category")["Sales"].sum()

plt.figure(figsize=(6,4))
category_sales.plot(kind="bar")
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.savefig("category_chart.png")
plt.show()

# Monthly sales
monthly_sales = df.groupby("Month")["Sales"].sum()

plt.figure(figsize=(6,4))
monthly_sales.plot(kind="line", marker="o")
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.savefig("monthly_sales.png")
plt.show()

print("Analysis Completed Successfully!")