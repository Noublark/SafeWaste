import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
from src.models.data import Data

st.set_page_config(page_title="SafeWaste", page_icon="♻️", layout="wide")

st.markdown("""
<style>
    .reportview-container {
        background: #f0f2f6
    }
    .sidebar .sidebar-content {
        background: #ffffff
    }
</style>
""", unsafe_allow_html=True)

st.title("🌍 SafeWaste")

data = Data()
df = data.load_data()

st.sidebar.header("Filtros")

# slider de anos
ano_min = max(2012, df['anoGeracao'].dt.year.min())  
ano_max = df['anoGeracao'].dt.year.max()
anos_selecionados = st.sidebar.slider("Selecionar Faixa de Anos", ano_min, ano_max, (ano_min, ano_max))

# seleção de estados
estados = sorted(df['estado'].unique())
if st.sidebar.button("Selecionar Todos os Estados"):
    estados_selecionados = estados
else:
    estados_selecionados = st.sidebar.multiselect("Selecionar Estados", estados, default=estados)

# seleção de tipos de resíduos
tipos_residuos = sorted(df['tipoResiduo'].unique())
if st.sidebar.button("Selecionar Todos os Tipos de Resíduos"):
    tipos_residuos_selecionados = tipos_residuos
else:
    tipos_residuos_selecionados = st.sidebar.multiselect("Selecionar Tipos de Resíduos", tipos_residuos, default=tipos_residuos)

df_filtrado = df[
    (df['anoGeracao'].dt.year.between(anos_selecionados[0], anos_selecionados[1])) &
    (df['estado'].isin(estados_selecionados)) &
    (df['tipoResiduo'].isin(tipos_residuos_selecionados))
]

st.header("Visão Geral do Dashboard")

# metricas
col1, col2, col3, col4 = st.columns(4)

# quantidadeGerada == num
df_filtrado['quantidadeGerada'] = df_filtrado['quantidadeGerada'].str.replace('.', '', regex=False)  # remove os pontos
df_filtrado['quantidadeGerada'] = df_filtrado['quantidadeGerada'].str.replace(',', '.', regex=False)  # substitui a vírgula por ponto
df_filtrado['quantidadeGerada'] = pd.to_numeric(df_filtrado['quantidadeGerada'], errors='coerce')  # converte para float

# verificar se existem valores NaN e substituí-los por 0 
df_filtrado['quantidadeGerada'].fillna(0, inplace=True)

total_residuos_gerados = df_filtrado['quantidadeGerada'].sum()
num_geradores = df_filtrado['cnpjGerador'].nunique()
num_municipios = df_filtrado['municipio'].nunique()
num_tipos_residuos = df_filtrado['tipoResiduo'].nunique()

with col1:
    st.metric("Total de Resíduos Gerados", f"{total_residuos_gerados:,.2f} toneladas")

with col2:
    st.metric("Número de Geradores", num_geradores)

with col3:
    st.metric("Número de Municípios", num_municipios)

with col4:
    st.metric("Tipos de Resíduos Perigosos", num_tipos_residuos)

st.subheader("Geração de Resíduos Perigosos ao Longo do Tempo")
df_residuos_anual = df_filtrado.groupby(df_filtrado['anoGeracao'].dt.year)['quantidadeGerada'].sum().reset_index()
fig_tempo = px.line(df_residuos_anual, x='anoGeracao', y='quantidadeGerada', 
                   labels={'anoGeracao': 'Ano', 'quantidadeGerada': 'Resíduos Gerados (toneladas)'},
                   color_discrete_sequence=['#985698'])
st.plotly_chart(fig_tempo, use_container_width=True)

st.subheader("Distribuição de Resíduos Perigosos por Estado")
df_residuos_estado = df_filtrado.groupby('estado')['quantidadeGerada'].sum().sort_values(ascending=False).reset_index()
fig_estado = px.bar(df_residuos_estado, x='estado', y='quantidadeGerada', 
                   labels={'estado': 'Estado', 'quantidadeGerada': 'Resíduos Gerados (toneladas)'},
                   color_discrete_sequence=['#985698'])
st.plotly_chart(fig_estado, use_container_width=True)

st.subheader("Principais Tipos de Resíduos Perigosos")
df_tipos_residuos = df_filtrado.groupby('tipoResiduo')['quantidadeGerada'].sum().sort_values(ascending=False).head(10).reset_index()
fig_tipos = px.pie(df_tipos_residuos, values='quantidadeGerada', names='tipoResiduo', hole=0.3,
                   color_discrete_sequence=['#985698'])
st.plotly_chart(fig_tipos, use_container_width=True)

st.subheader("Dados Detalhados")
st.dataframe(df_filtrado)

st.markdown("---")
st.markdown("Fonte dos dados: Arquivo JSON local (residuos_solidos.json)")
st.markdown(f"Última atualização: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
