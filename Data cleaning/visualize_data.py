import matplotlib.pyplot as plt
import pandas as pd
# Load cleaned data
customer_df = pd.read_csv('Cleaned_Customer.csv')
market_trends_df = pd.read_csv('Cleaned_Market_Trends.csv')
product_pricing_df = pd.read_csv('Cleaned_Product_Pricing.csv')
revenue_analysis_df = pd.read_csv('Cleaned_Revenue_Analysis.csv')
sales_data_df = pd.read_csv('Cleaned_Sales_Data.csv')
website_analytics_df = pd.read_csv('Cleaned_Website_Analytics.csv')

# Line chart to compare popular paths
paths = website_analytics_df['Popular Paths'].unique()
plt.figure(figsize=(12, 8))
for path in paths:
    path_data = website_analytics_df[website_analytics_df['Popular Paths'] == path]
    plt.plot(path_data['Access Date'], path_data['Number of Visits'], marker='o', label=path)
plt.title('Comparison of Popular Paths')
plt.xlabel('Date')
plt.ylabel('Number of Visits')
plt.legend(title='Paths')
plt.grid(True)
plt.xticks(rotation=45)
plt.show()

##############################################################################################################
# Bar chart of bounce rate by day
plt.figure(figsize=(12, 6))
plt.bar(website_analytics_df['Access Date'], website_analytics_df['Bounce Rate'], color='orange')
plt.title('Bounce Rate by Day')
plt.xlabel('Date')
plt.ylabel('Bounce Rate')
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(rotation=45)
plt.show()

##############################################################################################################
# Line chart of website visits
plt.figure(figsize=(12, 6))
plt.plot(website_analytics_df['Access Date'], website_analytics_df['Number of Visits'], marker='o', color='blue')
plt.title('Website Visits by Day')
plt.xlabel('Date')
plt.ylabel('Number of Visits')
plt.grid(True)
plt.xticks(rotation=45)
plt.show()

################################################################################################################
# Scatter plot of sales revenue by day
plt.figure(figsize=(12, 8))
plt.scatter(sales_data_df['Sale Date'], sales_data_df['Revenue'], color='purple')
plt.title('Sales Revenue by Day')
plt.xlabel('Date')
plt.ylabel('Revenue (USD)')
plt.grid(True)
plt.xticks(rotation=45)
plt.show()

################################################################################################################
# #Monthly Revenue (Line Chart)
# Convert 'Revenue by Product Type' to numeric, coerce errors to NaN and then fill NaN with 0
revenue_analysis_df['Revenue by Product Type'] = pd.to_numeric(revenue_analysis_df['Revenue by Product Type'], errors='coerce').fillna(0)
# Group by 'Month/Year' and sum the 'Revenue by Product Type'
monthly_revenue = revenue_analysis_df.groupby('Month/Year')['Revenue by Product Type'].sum()
# Plot the data
plt.figure(figsize=(12, 6))
monthly_revenue.plot(kind='line', marker='o', color='green')
plt.title('Monthly Revenue')
plt.xlabel('Month/Year')
plt.ylabel('Revenue (USD)')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#############################################################################################################
#Revenue by Product Type (Bar Chart)
# Inspect the DataFrame to understand its structure
print(revenue_analysis_df.head())

# Clean the 'Revenue by Product Type' column by removing any non-numeric characters
if 'Revenue by Product Type' in revenue_analysis_df.columns:
    revenue_analysis_df['Revenue by Product Type'] = revenue_analysis_df['Revenue by Product Type'].replace('[\$,]', '', regex=True).astype(float)
    revenue_by_product_type = revenue_analysis_df.groupby('Revenue by Product Type')['Revenue by Product Type'].sum()
    print(revenue_by_product_type)

    # Check if the series is empty or contains only NaN values
    if revenue_by_product_type.empty or revenue_by_product_type.isna().all():
        print("No valid numeric data to plot.")
    else:
        plt.figure(figsize=(10, 6))
        revenue_by_product_type.plot(kind='bar', color='skyblue')
        plt.title('Revenue by Product Type')
        plt.xlabel('Product Type')
        plt.ylabel('Revenue (USD)')
        plt.xticks(rotation=45)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.show()
else:
    print("'Revenue by Product Type' column not found in the DataFrame.")
