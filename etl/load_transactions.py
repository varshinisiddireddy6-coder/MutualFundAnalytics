import pandas as pd
import sqlite3

txn_df = pd.read_csv(
    "data/raw/08_investor_transactions.csv"
)

txn_df['transaction_date'] = pd.to_datetime(
    txn_df['transaction_date']
)

conn = sqlite3.connect(
    "mutualfund.db"
)

txn_df.to_sql(
    "fact_transactions",
    conn,
    if_exists="replace",
    index=False
)

print("32778 Transaction records loaded successfully!")

conn.close()