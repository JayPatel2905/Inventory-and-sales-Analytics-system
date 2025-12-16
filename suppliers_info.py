from connection import connect

def add_supplier(name,contact,email):
    conn=connect()
    cursor=conn.cursor()
    cursor.execute("insert into suppliers(suppliers_name,contact,email) values (%s,%s,%s)",(name,contact,email))
    cursor.commit()
    conn.close()

