import pandas as pd
import sqlite3

aum_df = pd.read_csv(
    "data/raw/03_aum_by_fund_house.csv"
)

aum_df['date'] = pd.to_datetime(
    aum_df['date']
)

conn = sqlite3.connect(
    "mutualfund.db"
)

aum_df.to_sql(
    "fact_aum",
    conn,
    if_exists="replace",
    index=False
)

print("90 AUM records loaded successfully!")

conn.close()