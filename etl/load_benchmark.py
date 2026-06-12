import pandas as pd
import sqlite3

benchmark_df = pd.read_csv(
    "data/raw/10_benchmark_indices.csv"
)

benchmark_df['date'] = pd.to_datetime(
    benchmark_df['date']
)

conn = sqlite3.connect(
    "mutualfund.db"
)

benchmark_df.to_sql(
    "fact_benchmark",
    conn,
    if_exists="replace",
    index=False
)

print("8050 Benchmark records loaded successfully!")

conn.close()