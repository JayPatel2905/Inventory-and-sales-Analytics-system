from connection import connect

def low_stock_products():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT name, stock_quantity, reorder_level 
        FROM products 
        WHERE stock_quantity < reorder_level
    """)
    result = cursor.fetchall()
    conn.close()
    return result