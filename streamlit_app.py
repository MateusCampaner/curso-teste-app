import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import math
import seaborn as sns
import matplotlib.pyplot as plt
import base64

st.set_page_config(page_title='Streamlit', page_icon='🔴')

st.sidebar.header("🔴 Streamlit")

def download_csv(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # Codifica para base64
    href = f'<a href="data:file/csv;base64,{b64}" download="dados_filtrados.csv">Download do CSV</a>'
    return href

pagina = st.sidebar.selectbox(
    "Escolha",
    ('Visualizar CSV', 'Baixar')
)


if pagina == "Visualizar CSV":
    st.header("📊 Visualizar CSV")

    st.subheader('Upload de CSV')
    uploaded_file = st.file_uploader("Escolha um arquivo CSV", type=['csv'])

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)

        st.write("Dados do arquivo CSV:")

        selected_columns = st.multiselect(
            'Selecione as colunas para exibir',
            options=df.columns.tolist(),
            default=df.columns.tolist()
        )

        if selected_columns:
            df_filtered = df[selected_columns]
            st.write(df_filtered)

            st.session_state['df_filtered'] = df_filtered

        st.write("Selecione uma coluna para visualizar informações:")
        coluna_selecionada = st.selectbox(
            "Escolha uma coluna",
            options=df.columns.tolist()
        )

        if coluna_selecionada:
            # Exibe os valores únicos da coluna selecionada
            valores_unicos = df[coluna_selecionada].unique()
            st.write(f"Valores únicos de '{coluna_selecionada}':")
            st.write(valores_unicos)

            # Exibe a quantidade de valores únicos
            quantidade_valores_unicos = df[coluna_selecionada].nunique()
            st.write(f"Quantidade de valores únicos em '{coluna_selecionada}': {quantidade_valores_unicos}")

            # Exibe a quantidade total de linhas no DataFrame
            quantidade_linhas = df.shape[0]
            st.write(f"Quantidade total de linhas no DataFrame: {quantidade_linhas}")
        

        

# Página para baixar o CSV filtrado
if pagina == 'Baixar':
    st.header("📊 Baixar CSV")

    # Carregar o DataFrame filtrado da sessão
    df_filtered = st.session_state.get('df_filtered')

    if df_filtered is not None and not df_filtered.empty:
        st.write("Visualização dos dados filtrados:")
        st.write(df_filtered)

        # Botão para baixar o CSV filtrado
        st.markdown(download_csv(df_filtered), unsafe_allow_html=True)
    else:
        st.write("Nenhum dado filtrado disponível para download.")