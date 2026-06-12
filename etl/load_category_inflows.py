import pandas as pd
import sqlite3

category_df = pd.read_csv(
    "data/raw/05_category_inflows.csv"
)

category_df['month'] = pd.to_datetime(
    category_df['month']
)

conn = sqlite3.connect(
    "mutualfund.db"
)

category_df.to_sql(
    "fact_category_inflows",
    conn,
    if_exists="replace",
    index=False
)

print("144 Category Inflow records loaded successfully!")

conn.close()