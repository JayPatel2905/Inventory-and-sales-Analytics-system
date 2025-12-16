# Inventory & Sales Analytics System

## Overview
The **Inventory & Sales Analytics System** is a Python-based application designed to help small and medium-sized businesses manage inventory, suppliers, and sales while deriving **actionable business insights** from transactional data.

Unlike basic CRUD applications, this project emphasizes **analytics, reporting, and visualization**, demonstrating practical use of Python, SQL, and data analysis tools in a real-world business context.

---

## Key Features

### Inventory Management
- Add and view products with category and pricing details  
- Track stock levels and define reorder thresholds  
- Maintain supplier information with relational integrity  

### Sales Management
- Record sales transactions  
- Automatically update inventory after each sale  
- Calculate total sales value per transaction  

### Analytics & Insights
- Identify top-selling products  
- Generate monthly revenue summaries  
- Detect low-stock items to prevent stock-outs  

### Data Visualization
- Revenue trends using line charts  
- Product demand using bar charts  
- Inventory risk visualization for low-stock products  

---

## Tech Stack

| Component | Technology |
|---------|------------|
| Language | Python |
| Database | MySQL |
| Data Analysis | Pandas |
| Visualization | Matplotlib |
| DB Connectivity | mysql-connector-python |
| Environment Management | python-dotenv |
| Version Control | Git |

---

## Project Structure

```text
inventory_sales/
│
├── database/
│   ├── connection.py        # Database connection logic
│   └── schema.sql           # SQL schema
│
├── inventory/
│   ├── product_crud.py      # Product-related operations
│   └── supplier_crud.py     # Supplier-related operations
│
├── sales/
│   └── sales.py             # Sales handling and stock updates
│
├── analytics/
│   ├── sales_analysis.py    # Revenue and demand analytics
│   ├── stock_analysis.py    # Inventory risk analysis
│   └── visualization.py    # Matplotlib charts
│
├── reports/
│   └── monthly_report.py    # Revenue reports
│
├── main.py                  # Application entry point
├── .env                     # Environment variables (ignored)
├── requirements.txt         # Project dependencies
└── README.md
