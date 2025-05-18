import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from utils.load_data import load_data

@st.cache_data
def get_review_data():
    df = load_data()
    df = df[['review_score', 'delivery_days']].dropna()
    return df

def main():
    st.header("📈 Avaliação vs Tempo de Entrega")
    st.markdown("Relação entre a nota do cliente e o tempo de entrega.")

    review_data = get_review_data()

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(data=review_data, x='delivery_days', y='review_score', alpha=0.5, ax=ax)
    ax.set_title("Nota de Avaliação vs Tempo de Entrega")
    ax.set_xlabel("Tempo de Entrega (dias)")
    ax.set_ylabel("Nota de Avaliação")
    st.pyplot(fig)

main()
