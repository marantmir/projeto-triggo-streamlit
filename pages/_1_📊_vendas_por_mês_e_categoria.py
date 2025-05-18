import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from utils.load_data import load_data

@st.cache_data
def get_monthly_data():
    df = load_data()
    df['purchase_month'] = df['order_purchase_timestamp'].dt.to_period('M').astype(str)
    monthly_orders = df.groupby('purchase_month').size().reset_index(name='order_count')
    return monthly_orders

def main():
    st.header("📊 Vendas por Mês")
    st.markdown("Visualização do volume de vendas ao longo do tempo.")

    monthly_orders = get_monthly_data()

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(data=monthly_orders, x='purchase_month', y='order_count', marker='o', ax=ax)
    ax.set_title("Volume de Pedidos por Mês")
    ax.set_xlabel("Mês")
    ax.set_ylabel("Quantidade de Pedidos")
    plt.xticks(rotation=45)
    st.pyplot(fig)

main()
