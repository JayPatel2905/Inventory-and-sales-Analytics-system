from product import add_product, view_product
from suppliers_info import add_supplier
from analytics import low_stock_products
from sales_analytics import top_selling_products
from sales import record_sale
from graphs import (plot_top_selling_products , plot_monthly_revenue , plot_low_stock)

print("1. Add Supplier")
print("2. Add Product")
print("3. View Products")
print("4. Record Sale")
print("5. Low Stock Report")
print("6. Top Selling Products")
print("7. Show Top Selling Products Chart")
print("8. Show Monthly Revenue Chart")
print("9. Show Low Stock Chart")


choice = input("Enter choice: ")

if choice == "1":
    add_supplier("ABC Traders", "9999999999", "abc@mail.com")

elif choice == "2":
    add_product("Laptop", "Electronics", 50000, 45000, 10, 3, 1)

elif choice == "3":
    view_product()

elif choice == "4":
    p_id=int(input("enter product id: "))
    quantity=int(input("enter quantity : "))
    record_sale(p_id, quantity)

elif choice == "5":
    print(low_stock_products())

elif choice == "6":
    print(top_selling_products())

elif choice == "7":
    plot_top_selling_products()

elif choice == "8":
    plot_monthly_revenue()

elif choice == "9":
    plot_low_stock()