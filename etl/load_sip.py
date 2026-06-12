import pandas as pd
import sqlite3

sip_df = pd.read_csv(
    "data/raw/04_monthly_sip_inflows.csv"
)

sip_df['month'] = pd.to_datetime(
    sip_df['month']
)

conn = sqlite3.connect(
    "mutualfund.db"
)

sip_df.to_sql(
    "fact_sip",
    conn,
    if_exists="replace",
    index=False
)

print("48 SIP records loaded successfully!")

conn.close()