import yfinance as yf
import pandas as pd
import sqlite3

# 1. Configuration
symbol = "AAPL"
db_name = "trading_data.db"

# 2. Extract
data = yf.download(symbol, period="5d")

# 3. Transform
# Move the Date from the index to a regular column
data = data.reset_index()
# Add a column so we know which stock this is
data['Ticker'] = symbol

# 4. Load
conn = sqlite3.connect(db_name)
# 'append' ensures we keep history; 'index=False' because we made Date a column
data.to_sql('prices', conn, if_exists="append", index=False)
conn.close()

print(f"Success! {symbol} data added to {db_name}")