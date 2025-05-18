import streamlit as st
import pandas as pd
from utils.load_data import download_and_cache_data, load_data_from_sql
from utils.db_utils import init_db

init_db()
st.set_page_config(page_title="Dashboard E-commerce", layout="wide")

st.title("🛒 Dashboard de Análise de Vendas - Olist")
st.markdown("Este dashboard foi desenvolvido como parte do teste técnico da Triggo.ai.")

# Navegação lateral
st.sidebar.title("📌 Navegação")
pages = {
    "1. Vendas por Mês e Categoria": "_1_📊_Vendas_por_Mês_e_Categoria",
    "2. Mapa de Vendas por Região": "_2_🗺️_Mapa_de_Vendas_por_Região",
    "3. Avaliação vs Tempo de Entrega": "_3_📈_Avaliação_vs_Entrega",
    "4. Análise de Vendedores": "_4_🧑‍💼_Análise_de_Vendedores"
}

selection = st.sidebar.radio("Ir para:", list(pages.keys()))

# Se não houver dados no SQLite, baixa e salva
if 'df' not in st.session_state:
    with st.spinner("🔄 Baixando e preparando dados pela primeira vez..."):
        st.session_state.df = download_and_cache_data()
else:
    with st.spinner("🔁 Carregando dados do SQLite..."):
        st.session_state.df = load_data_from_sql()

page_file = pages[selection] + ".py"

with open(f"pages/{page_file}", encoding="utf-8") as f:
    code = compile(f.read(), page_file, 'exec')
    exec(code)
