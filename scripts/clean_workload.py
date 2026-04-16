import pandas as pd

# Load data
df = pd.read_csv("agent_workload.csv")

# Convert datetime
df["created_at"] = pd.to_datetime(df["created_at"])
df["resolved_at"] = pd.to_datetime(df["resolved_at"])

# Create resolution_time (in hours)
df["resolution_time"] = (
    (df["resolved_at"] - df["created_at"]).dt.total_seconds() / 3600
)

# Remove nulls
df = df.dropna()

# Save cleaned data
df.to_csv("cleaned_workload.csv", index=False)

print("Data cleaned successfully")