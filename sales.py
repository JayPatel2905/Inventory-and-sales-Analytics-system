from connection import connect
from datetime import date

def record_sale(product_id, quantity):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT price, stock_quantity FROM products WHERE product_id=%s", (product_id,))
    price, stock = cursor.fetchone()

    if stock < quantity:
        print("Insufficient stock")
        return

    total = price * quantity

    cursor.execute(
        "INSERT INTO sales (product_id, quantity_sold, sale_date, total_amount) VALUES (%s,%s,%s,%s)",
        (product_id, quantity, date.today(), total)
    )

    cursor.execute(
        "UPDATE products SET stock_quantity = stock_quantity - %s WHERE product_id=%s",
        (quantity, product_id)
    )

    conn.commit()
    conn.close()