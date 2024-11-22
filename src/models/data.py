from src.models.api_request import APIRequest
import pandas as pd

class Data:

    def __init__(self):
        self.api = APIRequest()
        self.data = None

    def load_data(self):
        # carrega os dados 
        if self.data is None:
            self.data = self.api.get_data()

        if 'data' in self.data:
            print(f"Dados carregados com sucesso: {len(self.data['data'])} registros.")

            # define as colunas para leitura
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

            # le apenas as colunas necessárias
            result = pd.json_normalize(
                self.data['data'],
                max_level=0  # evita processamento desnecessário de níveis aninhados 
            )[colunas]

            # aplica o filtro e limita os dados 
            residuos_filtrados = result[colunas][result['classificacaoResiduo'] == 'Perigoso'].head(100)

            return residuos_filtrados, colunas
