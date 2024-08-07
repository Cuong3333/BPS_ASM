# import pandas as pd
# # Load CSV files into DataFrames
# customer_df = pd.read_csv('Customer.csv')
# market_trends_df = pd.read_csv('Market Trends and Insights.csv')
# product_pricing_df = pd.read_csv('Product and Pricing.csv')
# revenue_analysis_df = pd.read_csv('Revenue Analysis.csv')
# sales_data_df = pd.read_csv('Sales Data Table.csv')
# website_analytics_df = pd.read_csv('Website Analytics.csv')

# Display the first few rows of each DataFrame
# print(customer_df.head())
# print(market_trends_df.head())
# print(product_pricing_df.head())
# print(revenue_analysis_df.head())
# print(sales_data_df.head())
# print(website_analytics_df.head())

# # Check data types
# print(customer_df.info())
# print(market_trends_df.info())
# print(product_pricing_df.info())
# print(revenue_analysis_df.info())
# print(sales_data_df.info())
# print(website_analytics_df.info())


# # Ensure there are no duplicate records.
# customer_df = customer_df.drop_duplicates()

# #Handle Missing Values: Fill or drop missing values as needed.
# customer_df = customer_df.fillna('Unknown')  # or customer_df.dropna()

# #Correct Data Types: Convert columns to appropriate data types.
# customer_df['Purchase Frequency'] = customer_df['Purchase Frequency'].astype(int)

# #Convert date columns to datetime format.
# market_trends_df['Month/Year'] = pd.to_datetime(market_trends_df['Month/Year'], format='%Y-%m')

# #Ensure text columns are properly formatted.
# market_trends_df['Consumer Trends'] = market_trends_df['Consumer Trends'].str.strip()
# market_trends_df['Customer Feedback'] = market_trends_df['Customer Feedback'].str.strip()

# #Ensure no duplicate product entries.
# product_pricing_df = product_pricing_df.drop_duplicates()

# #Fill or drop missing values.
# product_pricing_df = product_pricing_df.fillna({'Inventory Level': 0})

# #Correct Data Types: Ensure columns have the correct data types.
# product_pricing_df['Price'] = product_pricing_df['Price'].replace('[\$,]', '', regex=True).astype(float)
# product_pricing_df['Inventory Level'] = product_pricing_df['Inventory Level'].astype(int)

# #Revenue Analysis.csv
# #Format Date Column: Convert date columns to datetime format
# revenue_analysis_df['Month/Year'] = pd.to_datetime(revenue_analysis_df['Month/Year'], format='%Y-%m')

# #Clean Text Data: Ensure text columns are properly formatted.
# revenue_analysis_df['Revenue by Product Type'] = revenue_analysis_df['Revenue by Product Type'].str.strip()

# #Sales Data Table.csv
# #Format Date Column: Convert sale dates to datetime format.
# sales_data_df['Sale Date'] = pd.to_datetime(sales_data_df['Sale Date'])

# #Handle Missing Values: Fill or drop missing values.
# sales_data_df = sales_data_df.fillna({'Quantity Sold': 0, 'Revenue': 0})

# #Website Analytics.csv
# #Format Date Column: Convert access dates to datetime format.
# website_analytics_df['Access Date'] = pd.to_datetime(website_analytics_df['Access Date'])

# #Clean Numerical Data: Ensure numerical data is properly formatted.
# website_analytics_df['Number of Visits'] = website_analytics_df['Number of Visits'].astype(int)
# website_analytics_df['Bounce Rate'] = website_analytics_df['Bounce Rate'].str.rstrip('%').astype(float) / 100

# # : Merge sales data with product pricing data
# merged_df = pd.merge(sales_data_df, product_pricing_df, on='Product Code')

# # : Calculate total revenue from sales data
# sales_data_df['Total Revenue'] = sales_data_df['Quantity Sold'] * sales_data_df['Revenue']


# #Save the cleaned DataFrames to new CSV files or databases as needed.
# customer_df.to_csv('Cleaned_Customer.csv', index=False)
# market_trends_df.to_csv('Cleaned_Market_Trends.csv', index=False)
# product_pricing_df.to_csv('Cleaned_Product_Pricing.csv', index=False)
# revenue_analysis_df.to_csv('Cleaned_Revenue_Analysis.csv', index=False)
# sales_data_df.to_csv('Cleaned_Sales_Data.csv', index=False)
# website_analytics_df.to_csv('Cleaned_Website_Analytics.csv', index=False)
