import pandas as pd
import sqlite3

# Read CSV
nav_df = pd.read_csv("data/raw/02_nav_history.csv")

# Convert date
nav_df['date'] = pd.to_datetime(nav_df['date'])

# Connect DB
conn = sqlite3.connect("mutualfund.db")

# Load table
nav_df.to_sql(
    "fact_nav",
    conn,
    if_exists="replace",
    index=False
)

print("46000 NAV records loaded successfully!")

conn.close()