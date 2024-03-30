import pandas as pd

# Load each dataset
spy_df = pd.read_csv('DataSets/spy.csv', parse_dates=['Date'])
crude_df = pd.read_csv('DataSets/crudeOil.csv', parse_dates=['Date'])
gold_df = pd.read_csv('DataSets/gold.csv', parse_dates=['Date'])

# Merge the datasets on the 'Date' column
merged_df = pd.merge(spy_df, crude_df, on='Date', how='outer')
merged_df = pd.merge(merged_df, gold_df, on='Date', how='outer')

# Save the merged dataset
merged_df.to_csv('combined_data.csv', index=False)
