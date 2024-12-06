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
year_min = max(2012, df['anoGeracao'].dt.year.min())  
year_max = df['anoGeracao'].dt.year.max()
selected_years = st.sidebar.slider("Selecionar Faixa de Anos", year_min, year_max, (year_min, year_max))

# seleção de estados
states = sorted(df['estado'].unique())
if st.sidebar.button("Selecionar Todos os Estados"):
    selected_states = states
else:
    selected_states = st.sidebar.multiselect("Selecionar Estados", states, default=states)

# seleção de tipos de resíduos
waste_types = sorted(df['tipoResiduo'].unique())
if st.sidebar.button("Selecionar Todos os Tipos de Resíduos"):
    selected_waste_types = waste_types
else:
    selected_waste_types = st.sidebar.multiselect("Selecionar Tipos de Resíduos", waste_types, default=waste_types)

filtered_df = df[
    (df['anoGeracao'].dt.year.between(selected_years[0], selected_years[1])) &
    (df['estado'].isin(selected_states)) &
    (df['tipoResiduo'].isin(selected_waste_types))
]

st.header("Visão Geral do Dashboard")

# metricas
col1, col2, col3, col4 = st.columns(4)

# quantidadeGerada == num
filtered_df['quantidadeGerada'] = filtered_df['quantidadeGerada'].str.replace('.', '', regex=False)  # Remove os pontos
filtered_df['quantidadeGerada'] = filtered_df['quantidadeGerada'].str.replace(',', '.', regex=False)  # Substitui a vírgula por ponto
filtered_df['quantidadeGerada'] = pd.to_numeric(filtered_df['quantidadeGerada'], errors='coerce')  # Converte para float

# verificar se existem valores NaN e substituí-los por 0 
filtered_df['quantidadeGerada'].fillna(0, inplace=True)

total_waste_generated = filtered_df['quantidadeGerada'].sum()
num_generators = filtered_df['cnpjGerador'].nunique()
num_municipalities = filtered_df['municipio'].nunique()
num_waste_types = filtered_df['tipoResiduo'].nunique()

with col1:
    st.metric("Total de Resíduos Gerados", f"{total_waste_generated:,.2f} toneladas")

with col2:
    st.metric("Número de Geradores", num_generators)

with col3:
    st.metric("Número de Municípios", num_municipalities)

with col4:
    st.metric("Tipos de Resíduos Perigosos", num_waste_types)

st.subheader("Geração de Resíduos Perigosos ao Longo do Tempo")
yearly_waste = filtered_df.groupby(filtered_df['anoGeracao'].dt.year)['quantidadeGerada'].sum().reset_index()
fig_time = px.line(yearly_waste, x='anoGeracao', y='quantidadeGerada', 
                   labels={'anoGeracao': 'Ano', 'quantidadeGerada': 'Resíduos Gerados (toneladas)'},
                   color_discrete_sequence=['#985698'])
st.plotly_chart(fig_time, use_container_width=True)

st.subheader("Distribuição de Resíduos Perigosos por Estado")
state_waste = filtered_df.groupby('estado')['quantidadeGerada'].sum().sort_values(ascending=False).reset_index()
fig_state = px.bar(state_waste, x='estado', y='quantidadeGerada', 
                   labels={'estado': 'Estado', 'quantidadeGerada': 'Resíduos Gerados (toneladas)'},
                   color_discrete_sequence=['#985698'])
st.plotly_chart(fig_state, use_container_width=True)

st.subheader("Principais Tipos de Resíduos Perigosos")
waste_types = filtered_df.groupby('tipoResiduo')['quantidadeGerada'].sum().sort_values(ascending=False).head(10).reset_index()
fig_types = px.pie(waste_types, values='quantidadeGerada', names='tipoResiduo', hole=0.3,
                   color_discrete_sequence=['#985698'])
st.plotly_chart(fig_types, use_container_width=True)

st.subheader("Dados Detalhados")
st.dataframe(filtered_df)

st.markdown("---")
st.markdown("Fonte dos dados: Arquivo JSON local (residuos_solidos.json)")
st.markdown(f"Última atualização: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
