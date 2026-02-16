import sqlite3
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

DB_PATH = "db/lesson.db"
con = sqlite3.connect(DB_PATH)


SQL = """
SELECT last_name, SUM(price * quantity) AS revenue
FROM employees e
JOIN orders o ON e.employee_id = o.employee_id
JOIN line_items l ON o.order_id = l.order_id
JOIN products p ON l.product_id = p.product_id
GROUP BY e.employee_id;
"""

with sqlite3.connect(str(DB_PATH)) as con:
    df = pd.read_sql_query(SQL, con)

    ax = df.plot(
        x="last_name",
        y="revenue",
        kind="bar",
        title="Revenue by Employee",
        xlabel="Employee (Last Name)",
        ylabel="Revenue",
        legend=False,
        color="skyblue",
    )

    # optional labels on bars
    ax.bar_label(ax.containers[0], fmt="%.0f")
    plt.tight_layout()
    plt.show()


