import pandas as pd
import matplotlib.pyplot as plt

# Load the combined dataset
combined_df = pd.read_csv('combine.csv', parse_dates=['Date'])

# Plot the data
plt.figure(figsize=(10, 6))

# Plot SpyClose
plt.plot(combined_df['Date'], combined_df['SpyClose'], label='SPY Close')

# Plot CrudePrice
plt.plot(combined_df['Date'], combined_df['CrudePrice'], label='Crude Price')

# Plot GoldPrice
plt.plot(combined_df['Date'], combined_df['GoldPrice'], label='Gold Price')

# Set title and labels
plt.title('Combined Data Line Chart')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()

# Rotate date labels for better readability
plt.xticks(rotation=45)

# Show plot
plt.tight_layout()
plt.show()
