import pandas as pd
import matplotlib.pyplot as plt

# Load historical sales data
sales_data = pd.read_csv('Cleaned_Sales_Data.csv')

# Print columns to verify
print("Historical Sales Data Columns:", sales_data.columns)

# Rename column 'Sale Date' to 'Date' if needed
if 'Sale Date' in sales_data.columns:
    sales_data.rename(columns={'Sale Date': 'Date'}, inplace=True)

# Print updated columns to verify
print("Updated Historical Sales Data Columns:", sales_data.columns)

# Convert 'Date' column to datetime
if 'Date' in sales_data.columns:
    sales_data['Date'] = pd.to_datetime(sales_data['Date'], errors='coerce')
    
    # Drop rows with invalid dates if any
    sales_data.dropna(subset=['Date'], inplace=True)
    
    # Set 'Date' as index
    sales_data.set_index('Date', inplace=True)
    
    # Verify the data after setting index
    print("Data After Setting Index:", sales_data.head())
else:
    print("Column 'Date' not found in historical sales data")

# Sample predicted sales data for demonstration
predicted_sales_data = {
    'Date': ['2024-07-08', '2024-07-09', '2024-07-10', '2024-07-11', '2024-07-12'],
    'Predicted_Sales': [1900, 2000, 2100, 2200, 2300]
}
predicted_sales = pd.DataFrame(predicted_sales_data)
predicted_sales['Date'] = pd.to_datetime(predicted_sales['Date'], errors='coerce')
predicted_sales.set_index('Date', inplace=True)

# Print columns to verify
print("Predicted Sales Data Columns:", predicted_sales.columns)
print("Predicted Sales Data Preview:", predicted_sales.head())

# Plot historical and predicted sales
if 'Date' in sales_data.index.names and 'Date' in predicted_sales.index.names:
    plt.figure(figsize=(12, 6))
    plt.plot(sales_data.index, sales_data['Revenue'], label='Historical Sales', color='blue')
    plt.plot(predicted_sales.index, predicted_sales['Predicted_Sales'], label='Predicted Sales', color='red', linestyle='--')
    plt.xlabel('Date')
    plt.ylabel('Sales')
    plt.title('Sales Forecasting')
    plt.legend()
    plt.grid(True)
    plt.show()
else:
    print("Cannot plot data: Missing 'Date' column in one or both datasets")
