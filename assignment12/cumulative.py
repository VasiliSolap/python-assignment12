import sqlite3
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

DB_PATH = "db/lesson.db"

SQL = """
SELECT o.order_id, SUM(p.price * l.quantity) AS total_price
FROM orders o
JOIN line_items l ON o.order_id = l.order_id
JOIN products p ON l.product_id = p.product_id
GROUP BY o.order_id;
"""

with sqlite3.connect(str(DB_PATH)) as con:
    df = pd.read_sql_query(SQL, con)

def cumulative(row):
   totals_above = df['total_price'][0:row.name+1]
   return totals_above.sum()

df['cumulative'] = df.apply(cumulative, axis=1)

df.plot(
    x="order_id", 
    y="cumulative", 
    kind="line", 
    title="Cumulative Revenue")
plt.show()