import pandas as pd
import sqlite3

# Load cleaned data
df = pd.read_csv("cleaned_workload.csv")

# Connect DB
conn = sqlite3.connect("workload.db")

# Load into table
df.to_sql("tickets", conn, if_exists="replace", index=False)

print("Data loaded into database")