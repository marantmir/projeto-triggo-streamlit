import streamlit as st
import pandas as pd

@st.cache_data
def get_monthly_data():
    df = st.session_state.df.copy()
    df['purchase_month'] = df['order_purchase_timestamp'].dt.to_period('M').astype(str)
    monthly_orders = df.groupby('purchase_month').size().reset_index(name='order_count')
    return monthly_orders

def main():
    st.header("📅 Vendas por Mês")
    monthly_orders = get_monthly_data()
    st.line_chart(monthly_orders.set_index('purchase_month'))

main()
