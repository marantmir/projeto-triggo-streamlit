import streamlit as st
import pandas as pd
from utils.load_data import load_data_from_sql, download_and_cache_data

st.set_page_config(page_title="Dashboard E-commerce", layout="wide")

st.title("🛒 Dashboard de Análise de Vendas - Olist")
st.markdown("Projeto desenvolvido como parte do teste técnico da Triggo.ai.")

# Navegação
st.sidebar.title("📌 Navegação")
pages = {
    "1. Vendas por Mês e Categoria": "_1_📊_Vendas_por_Mês_e_Categoria",
    "2. Mapa de Vendas por Região": "_2_🗺️_Mapa_de_Vendas_por_Região",
    "3. Avaliação vs Tempo de Entrega": "_3_📈_Avaliação_vs_Entrega",
    "4. Análise de Vendedores": "_4_🧑‍💼_Análise_de_Vendedores"
}

selection = st.sidebar.radio("Ir para:", list(pages.keys()))

# Carregar dados do SQLite ou baixar se não existirem
if 'df' not in st.session_state:
    with st.spinner("🔄 Baixando dados do Kaggle pela primeira vez..."):
        df = download_and_cache_data()
        st.session_state.df = df
else:
    with st.spinner("🔁 Carregando dados do SQLite..."):
        df = st.session_state.df

page_file = pages[selection] + ".py"

try:
    with open(f"pages/{page_file}.py", encoding="utf-8") as f:
        code = compile(f.read(), page_file, 'exec')
        exec(code)
except FileNotFoundError:
    st.error(f"Arquivo {page_file} não encontrado na pasta 'pages/'.")
