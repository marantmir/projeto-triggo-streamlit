import streamlit as st
import pandas as pd
import plotly.express as px
from utils.load_data import load_data

@st.cache_data
def get_seller_data():
    df = load_data()
    seller_perf = df.groupby('seller_id').agg({
        'order_id': 'count',
        'review_score': 'mean',
        'delivery_days': 'mean'
    }).rename(columns={'order_id': 'total_sales'}).reset_index()
    return seller_perf

def main():
    st.header("🧑‍💼 Desempenho dos Vendedores")
    st.markdown("Comparação entre vendedores com base em vendas, satisfação e tempo de entrega.")

    seller_perf = get_seller_data()

    fig = px.scatter(
        seller_perf,
        x='delivery_days',
        y='review_score',
        size='total_sales',
        color='seller_id',
        title='Desempenho dos Vendedores',
        labels={
            'delivery_days': 'Tempo Médio de Entrega (dias)',
            'review_score': 'Nota Média dos Clientes'
        }
    )
    st.plotly_chart(fig)

main()
