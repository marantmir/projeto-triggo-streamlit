import sqlite3

def init_db():
    conn = sqlite3.connect('olist.db')
    conn.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            order_id TEXT,
            customer_id TEXT,
            order_status TEXT,
            order_purchase_timestamp TEXT,
            order_approved_at TEXT,
            order_delivered_carrier_date TEXT,
            order_delivered_customer_date TEXT,
            order_estimated_delivery_date TEXT
        )
    ''')
    conn.close()
