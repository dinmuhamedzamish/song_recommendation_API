import os
import sqlite3
import pandas as pd
from pathlib import Path

# Get the exact path to the data folder
DATA_DIR = Path(__file__).resolve().parent
CSV_PATH = DATA_DIR / "cleaned_dataset.csv"
DB_PATH = DATA_DIR / "song_db.db"

# 1. Read the cleaned dataset
df = pd.read_csv(CSV_PATH)

# Ensure only the needed columns are saved and create an 'id' column if missing
columns_needed = ["artists", "track_name", "tempo", "energy", "loudness"]
df = df[columns_needed].copy()

# Add an auto-incrementing ID column (1, 2, 3...)
df.reset_index(inplace=True)
df.rename(columns={"index": "id"}, inplace=True)
df["id"] = df["id"] + 1

# 2. Write to SQLite
conn = sqlite3.connect(DB_PATH)
df.to_sql("song", conn, index=False, if_exists="replace")
conn.close()

print(f"✅ Successfully seeded {len(df)} songs into {DB_PATH}!")
