import pandas as pd
from connection import connect

def monthly_revenue():
    conn = connect()
    query = """
        SELECT MONTH(sale_date) AS month, SUM(total_amount) AS revenue
        FROM sales
        GROUP BY month
    """
    df = pd.read_sql(query, conn)
    conn.close()
    return df