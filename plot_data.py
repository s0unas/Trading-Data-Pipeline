import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Create the directory if it's missing (important for the runner!)
import os
if not os.path.exists('charts'):
    os.makedirs('charts')

# ... your plotting code ...

plt.savefig('charts/price_trend.png')

# 1. Connect to the database
conn = sqlite3.connect('trading_data.db')

# 2. Read the data into a Pandas DataFrame
df = pd.read_sql_query("SELECT * FROM prices WHERE Ticker='AAPL'", conn)
conn.close()

# 3. Convert Date to datetime objects and sort
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values('Date')

# 4. Create the plot
plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['Close'], marker='o', linestyle='-', color='#007bff')

# Styling
plt.title('Apple (AAPL) Price Trend - Automated Pipeline', fontsize=14)
plt.xlabel('Date')
plt.ylabel('Close Price ($)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(rotation=45)
plt.tight_layout()

# 5. Save the chart as an image
plt.savefig('charts/price_trend.png')
print("Chart generated successfully in /charts folder!")

