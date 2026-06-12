import sqlite3

conn = sqlite3.connect("mutualfund.db")

print("Database created successfully!")

conn.close()