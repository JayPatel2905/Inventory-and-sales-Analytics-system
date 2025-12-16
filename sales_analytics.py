import pandas as pd
from connection import connect

def top_selling_products():
    conn = connect()
    query = """
        SELECT p.name, SUM(s.quantity_sold) AS total_sold
        FROM sales s
        JOIN products p ON s.product_id = p.product_id
        GROUP BY p.name
        ORDER BY total_sold DESC
    """
    df = pd.read_sql(query, conn)
    conn.close()
    return df