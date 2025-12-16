from connection import connect

def add_product(name, category, price, cost, stock, reorder, supplier_id):
    conn=connect()
    cursor=conn.cursor()
    cursor.execute("""insert into products
                   (name, category, price, cost_price, stock_quantity, reorder_level, supplier_id)
                    values (%s,%s,%s,%s,%s,%s,%s)"""
                   ,(name, category, price, cost, stock, reorder, supplier_id))
    cursor.commit()
    conn.close()

def view_product():
    conn=connect()
    cursor=conn.cursor()
    cursor.execute("select * from products")
    for row in cursor.fetchall():
        print(row)
    conn.close()

