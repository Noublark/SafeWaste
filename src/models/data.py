from src.models.api_request import APIRequest
import pandas as pd

class Data:

    def __init__(self):
        self.api = APIRequest()
        self.data = None

    def load_data(self):
        # Carrega os dados apenas se ainda não foram carregados
        if self.data is None:
            self.data = self.api.get_data()

        if 'data' in self.data:
            print(f"Dados carregados com sucesso: {len(self.data['data'])} registros.")

            # Define as colunas que queremos ler
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

            # Lê apenas as colunas necessárias e já aplica o filtro durante a normalização
            result = pd.json_normalize(
                self.data['data'],
                max_level=0  # Evita processamento desnecessário de níveis aninhados
            )[colunas]

            # Aplica o filtro e limita os dados em uma única operação
            residuos_filtrados = result[colunas][result['classificacaoResiduo'] == 'Perigoso'].head(100)

            return residuos_filtrados, colunas
