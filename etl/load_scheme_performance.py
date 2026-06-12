import pandas as pd
import sqlite3

perf_df = pd.read_csv(
    "data/raw/07_scheme_performance.csv"
)

conn = sqlite3.connect(
    "mutualfund.db"
)

perf_df.to_sql(
    "fact_scheme_performance",
    conn,
    if_exists="replace",
    index=False
)

print("40 Scheme Performance records loaded successfully!")

conn.close()