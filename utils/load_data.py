import pandas as pd
import os
import kagglehub

def load_data():
    # Baixar dataset automaticamente
    path = kagglehub.dataset_download("olistbr/brazilian-ecommerce")
    print(f"Dataset baixado em: {path}")

    # Carregar todos os CSVs na pasta
    all_files = [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.csv')]

    dfs = {}
    for file in all_files:
        filename = os.path.basename(file).replace(".csv", "")
        try:
            dfs[filename] = pd.read_csv(file)
            print(f"✅ Carregado: {filename}")
        except Exception as e:
            print(f"❌ Erro ao carregar {filename}: {e}")

    return dfs

    # Junção das tabelas principais
    orders = dfs['olist_orders_dataset']
    customers = dfs['olist_customers_dataset']
    order_items = dfs['olist_order_items_dataset']
    products = dfs['olist_products_dataset']
    sellers = dfs['olist_sellers_dataset']
    reviews = dfs['olist_order_reviews_dataset']

    # Converter datas
    orders['order_purchase_timestamp'] = pd.to_datetime(orders['order_purchase_timestamp'])
    orders['order_delivered_customer_date'] = pd.to_datetime(orders['order_delivered_customer_date'], errors='coerce')
    orders['order_estimated_delivery_date'] = pd.to_datetime(orders['order_estimated_delivery_date'])

    # Tratar valores nulos
    orders = orders.dropna(subset=['order_delivered_customer_date'])

    # Junções
    df = pd.merge(orders, customers, on='customer_id', how='inner')
    df = pd.merge(df, order_items, on='order_id', how='inner')
    df = pd.merge(df, products, on='product_id', how='left')
    df = pd.merge(df, sellers, on='seller_id', how='left')
    df = pd.merge(df, reviews[['order_id', 'review_score']], on='order_id', how='left')

    # Tempo de entrega
    df['delivery_days'] = (df['order_delivered_customer_date'] - df['order_purchase_timestamp']).dt.days

    # Definir se foi entregue com atraso
    df['delayed'] = (df['order_delivered_customer_date'] > df['order_estimated_delivery_date']).astype(int)

    return df
