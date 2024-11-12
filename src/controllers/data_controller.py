from src.models.data import Data
import matplotlib.pyplot as plt

class DataController:

    def __init__(self):

        self.data = Data()

    def gerar_grafico(self):

        residuos_filtrados, colunas = self.data.load_data()
        
        agrupado = residuos_filtrados.groupby('anoGeracao')['quantidadeGerada'].sum().reset_index()

        return agrupado


    def gerar_tabela(self):

        return self.data.load_data()



        