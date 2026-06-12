import pandas as pd
import sqlite3

folio_df = pd.read_csv(
    "data/raw/06_industry_folio_count.csv"
)

folio_df['month'] = pd.to_datetime(
    folio_df['month']
)

conn = sqlite3.connect(
    "mutualfund.db"
)

folio_df.to_sql(
    "fact_folio_count",
    conn,
    if_exists="replace",
    index=False
)

print("21 Folio records loaded successfully!")

conn.close()