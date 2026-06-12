import pandas as pd
import sqlite3

# Read CSV
fund_df = pd.read_csv("data/raw/01_fund_master.csv")

# Connect Database
conn = sqlite3.connect("mutualfund.db")

# Load into SQLite
fund_df.to_sql(
    "dim_fund",
    conn,
    if_exists="replace",
    index=False
)

print("40 Mutual Fund schemes loaded successfully!")

conn.close()