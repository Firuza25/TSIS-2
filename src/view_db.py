import sqlite3
import pandas as pd
from pathlib import Path

DB_PATH = Path(__file__).resolve().parents[1] / "data" / "output.db"

conn = sqlite3.connect(DB_PATH)
df = pd.read_sql("SELECT * FROM news", conn)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 200)
print(df.head(20))
conn.close()
