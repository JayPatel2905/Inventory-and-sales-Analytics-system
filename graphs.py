import matplotlib.pyplot as plt
from sales_analytics import top_selling_products
from monthly_report import monthly_revenue
from analytics import low_stock_products

def plot_top_selling_products():
    df = top_selling_products()

    if df.empty:
        print("No sales data available")
        return

    plt.figure()
    plt.bar(df["name"], df["total_sold"])
    plt.xlabel("Product")
    plt.ylabel("Units Sold")
    plt.title("Top Selling Products")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_monthly_revenue():
    df = monthly_revenue()

    if df.empty:
        print("No revenue data available")
        return

    plt.figure()
    plt.plot(df["month"], df["revenue"], marker="o")
    plt.xlabel("Month")
    plt.ylabel("Revenue")
    plt.title("Monthly Revenue Trend")
    plt.grid(True)
    plt.show()

def plot_low_stock():
    data = low_stock_products()

    if not data:
        print("No low-stock items")
        return

    names = [row[0] for row in data]
    stock = [row[1] for row in data]

    plt.figure()
    plt.bar(names, stock)
    plt.xlabel("Product")
    plt.ylabel("Current Stock")
    plt.title("Low Stock Alert")
    plt.xticks(rotation=45)
    plt.show()
