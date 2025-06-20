# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
# Let's assume we have a CSV file named 'sales_data.csv'
data = pd.read_csv('sales_data.csv')

# Display the first few rows of the dataset
print("First few rows of the dataset:")
print(data.head())

# Check for missing values
print("\nMissing values in each column:")
print(data.isnull().sum())

# Fill missing values, here we fill with the mean for numerical columns
data.fillna(data.mean(), inplace=True)

# Convert date column to datetime type if necessary
# Assuming there's a 'date' column in the dataset
data['date'] = pd.to_datetime(data['date'])

# Group data by month and calculate total sales
monthly_sales = data.resample('M', on='date').sum()

# Display the monthly sales data
print("\nMonthly sales data:")
print(monthly_sales)

# Plotting the total sales over time
plt.figure(figsize=(12, 6))
plt.plot(monthly_sales.index, monthly_sales['sales'], marker='o')
plt.title('Total Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.grid()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Additional analysis: Top-selling products
top_products = data.groupby('product_name')['sales'].sum().nlargest(10)

# Display the top-selling products
print("\nTop-selling products:")
print(top_products)

# Bar plot of top-selling products
top_products.plot(kind='bar', figsize=(10, 5))
plt.title('Top Selling Products')
plt.xlabel('Product Name')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
