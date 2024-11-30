import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# Set page config
st.set_page_config(page_title="IBAMA Hazardous Waste Dashboard", page_icon="♻️", layout="wide")

# Add custom CSS
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

# Title
st.title("🌍 SafeWaste")

# Load data
@st.cache_data
def load_data():
    df = pd.read_json("residuos_solidos.json")
    
    # Define the columns you want to select
    columns = [
        'cnpjGerador', 
        'detalhe',
        'estado', 
        'municipio',  
        'anoGeracao', 
        'tipoResiduo', 
        'quantidadeGerada', 
        'unidade',
        'classificacaoResiduo'
    ]
    
    # Check if columns exist in the dataframe
    existing_columns = [col for col in columns if col in df.columns]
    
    # Subset the dataframe with only existing columns
    df = df[existing_columns]
    
    # Filter only hazardous waste
    df = df[df['classificacaoResiduo'] == 'Perigoso']
    
    # Convert 'anoGeracao' to datetime
    df['anoGeracao'] = pd.to_datetime(df['anoGeracao'], format='%Y')
    
    return df

df = load_data()

# Sidebar filters
st.sidebar.header("Filtros")

# Year range slider
year_min = max(2012, df['anoGeracao'].dt.year.min())  # Garantir que o ano mínimo seja 2012
year_max = df['anoGeracao'].dt.year.max()
selected_years = st.sidebar.slider("Selecionar Faixa de Anos", year_min, year_max, (year_min, year_max))

# State multiselect
states = sorted(df['estado'].unique())

# Botão para selecionar todos os estados
if st.sidebar.button("Selecionar Todos os Estados"):
    selected_states = states
else:
    selected_states = st.sidebar.multiselect("Selecionar Estados", states, default=states)

# Waste type multiselect
waste_types = sorted(df['tipoResiduo'].unique())

# Botão para selecionar todos os tipos de resíduos
if st.sidebar.button("Selecionar Todos os Tipos de Resíduos"):
    selected_waste_types = waste_types
else:
    selected_waste_types = st.sidebar.multiselect("Selecionar Tipos de Resíduos", waste_types, default=waste_types[:5])

# Apply filters
filtered_df = df[
    (df['anoGeracao'].dt.year.between(selected_years[0], selected_years[1])) &
    (df['estado'].isin(selected_states)) &
    (df['tipoResiduo'].isin(selected_waste_types))
]

# Main content
st.header("Visão Geral do Dashboard")

# KPI metrics
col1, col2, col3, col4 = st.columns(4)

# Garantir que 'quantidadeGerada' seja numérica, ignorando valores não numéricos ou nulos
filtered_df['quantidadeGerada'] = filtered_df['quantidadeGerada'].str.replace('.', '', regex=False)  # Remove os pontos
filtered_df['quantidadeGerada'] = filtered_df['quantidadeGerada'].str.replace(',', '.', regex=False)  # Substitui a vírgula por ponto
filtered_df['quantidadeGerada'] = pd.to_numeric(filtered_df['quantidadeGerada'], errors='coerce')  # Converte para float

# Verificar se existem valores NaN e substituí-los por 0 ou outro valor padrão
filtered_df['quantidadeGerada'].fillna(0, inplace=True)

# Exibindo as métricas de forma segura
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

# Waste generation over time
st.subheader("Geração de Resíduos Perigosos ao Longo do Tempo")
yearly_waste = filtered_df.groupby(filtered_df['anoGeracao'].dt.year)['quantidadeGerada'].sum().reset_index()
fig_time = px.line(yearly_waste, x='anoGeracao', y='quantidadeGerada', 
                   labels={'anoGeracao': 'Ano', 'quantidadeGerada': 'Resíduos Gerados (toneladas)'},
                   color_discrete_sequence=['#985698'])
st.plotly_chart(fig_time, use_container_width=True)

# Waste distribution by state
st.subheader("Distribuição de Resíduos Perigosos por Estado")
state_waste = filtered_df.groupby('estado')['quantidadeGerada'].sum().sort_values(ascending=False).reset_index()
fig_state = px.bar(state_waste, x='estado', y='quantidadeGerada', 
                   labels={'estado': 'Estado', 'quantidadeGerada': 'Resíduos Gerados (toneladas)'},
                   color_discrete_sequence=['#985698'])
st.plotly_chart(fig_state, use_container_width=True)

# Top waste types
st.subheader("Principais Tipos de Resíduos Perigosos")
waste_types = filtered_df.groupby('tipoResiduo')['quantidadeGerada'].sum().sort_values(ascending=False).head(10).reset_index()
fig_types = px.pie(waste_types, values='quantidadeGerada', names='tipoResiduo', hole=0.3,
                   color_discrete_sequence=['#985698'])
st.plotly_chart(fig_types, use_container_width=True)

# Data table
st.subheader("Dados Detalhados")
st.dataframe(filtered_df)

# Footer
st.markdown("---")
st.markdown("Fonte dos dados: Arquivo JSON local (residuos_solidos.json)")
st.markdown(f"Última atualização: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
