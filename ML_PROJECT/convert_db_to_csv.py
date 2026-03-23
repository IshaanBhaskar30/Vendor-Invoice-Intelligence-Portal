import sqlite3
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

db_path = BASE_DIR / "data" / "inventory.db"
conn = sqlite3.connect(db_path)

print("Connected to DB...")

# 🔥 CORRECT QUERY (WITH JOIN)
query = """
WITH purchase_agg AS (
    SELECT 
        PONumber,
        SUM(Quantity) AS total_item_quantity,
        SUM(Dollars) AS total_item_dollars,
        AVG(julianday(ReceivingDate) - julianday(PODate)) AS avg_receiving_delay
    FROM purchases
    GROUP BY PONumber
)

SELECT 
    vi.PONumber,
    vi.Quantity,
    vi.Dollars,
    vi.Freight,
    pa.total_item_quantity,
    pa.total_item_dollars,
    pa.avg_receiving_delay

FROM vendor_invoice vi
LEFT JOIN purchase_agg pa
ON vi.PONumber = pa.PONumber
"""

df = pd.read_sql(query, conn)

print("Original shape:", df.shape)

# Safe sampling
df_sample = df.sample(n=min(20000, len(df)), random_state=42)

print("Sample shape:", df_sample.shape)

# Save CSV
output_path = BASE_DIR / "data" / "vendor_invoice_sample.csv"
df_sample.to_csv(output_path, index=False)

print("CSV saved at:", output_path)

conn.close()