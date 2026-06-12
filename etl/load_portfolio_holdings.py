import pandas as pd
import sqlite3

holding_df = pd.read_csv(
    "data/raw/09_portfolio_holdings.csv"
)

holding_df['portfolio_date'] = pd.to_datetime(
    holding_df['portfolio_date']
)

conn = sqlite3.connect(
    "mutualfund.db"
)

holding_df.to_sql(
    "fact_portfolio_holdings",
    conn,
    if_exists="replace",
    index=False
)

print("322 Portfolio Holding records loaded successfully!")

conn.close()