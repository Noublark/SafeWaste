from api_request import APIRequest
import pandas as pd

class Data:

    def __init__(self):
        self.api = APIRequest()
        self.data = None

    def load_data(self):

        self.data = self.api.get_data()

        if 'data' in self.data:
        
            result = pd.json_normalize(self.data['data'])

        result = result.head(100000)  # Limitando a leitura para as primeiras 100.000 linhas

        colunas = [
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

        residuos_filtrados = result[colunas][result['classificacaoResiduo'] == 'Perigoso']

        print(residuos_filtrados) #remover dps

data = Data()
data.load_data() #remover dps
        