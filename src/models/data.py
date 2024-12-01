from turtle import st
import pandas as pd

class Data:

    def __init__(self):
        self.data = None

    #@st.cache_data
    def load_data(self):
        
        df = pd.read_json("src/resources/json/residuos_solidos.json")
        self.data = df
    
        # converter 'anoGeracao' para datetime
        self.data['anoGeracao'] = pd.to_datetime(self.data['anoGeracao'], format='%Y')
    
        return self.data



