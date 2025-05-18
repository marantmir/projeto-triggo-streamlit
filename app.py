import streamlit as st
import os

# Configuração inicial
st.set_page_config(page_title="Dashboard E-commerce", layout="wide")

# Título e descrição
st.title("🛒 Dashboard de Análise de Vendas - Olist")
st.markdown("Este dashboard foi desenvolvido como parte do teste técnico da Triggo.ai.")

# Navegação
st.sidebar.title("📌 Navegação")
pages = {
    "1. Vendas por Mês e Categoria": "_1_📊_Vendas_por_Mês_e_Categoria",
    "2. Mapa de Vendas por Região": "_2_🗺️_Mapa_de_Vendas_por_Região",
    "3. Avaliação vs Tempo de Entrega": "_3_📈_Avaliação_vs_Entrega",
    "4. Análise de Vendedores": "_4_🧑‍💼_Análise_de_Vendedores"
}

selection = st.sidebar.radio("Ir para:", list(pages.keys()))

# Carregar página selecionada
page = pages[selection] + ".py"

page_path = f"pages/{page}"

if os.path.exists(page_path):
    with open(page_path, encoding="utf-8") as f:
        code = compile(f.read(), page_path, 'exec')
        exec(code)
else:
    st.error(f"Arquivo não encontrado: {page_path}")
    st.stop()
