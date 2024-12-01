from src.models.data import Data
from src.services.servicos_relatorio import ServicosRelatorio
import pandas as pd
import os

class Relatorio:

    def __init__(self):
        
        self.data = Data()
        self.servicos = ServicosRelatorio()

    def gerar_relatorio(self):
        
        # carrega os dados e as colunas
        residuos_filtrados = self.data.load_data()
        
        # usa os dados filtrados diretamente
        if residuos_filtrados.empty:
            print("Nenhum dado encontrado após o filtro.")
            return

        # converte o tipo da coluna 'anoGeracao' para inteiro
        anos = [ano for ano in residuos_filtrados['anoGeracao'].dt.year.unique() if ano >= 2012]
    
        for ano in anos:
            # filtra dados para o ano específico
            dados_ano = residuos_filtrados[residuos_filtrados['anoGeracao'].dt.year == ano]
        
            if dados_ano.empty:
                print(f"Nenhum dado encontrado para o ano {ano}.")
                continue

            # exibe o relatório
            print(f"Relatório do ano {ano}:\n{dados_ano}")

            # salva no banco de dados
            self.servicos.salvar_relatorio_bd(dados_ano, ano)
    
    def carregar_relatorio(self, conteudo_relatorio):

        if isinstance(conteudo_relatorio, pd.DataFrame):
            conteudo_relatorio_str = conteudo_relatorio.to_string(index=False) 
        else:
            conteudo_relatorio_str = str(conteudo_relatorio)

        return conteudo_relatorio_str


    def baixar_relatorio(self, nome_relatorio):
        
        conteudo_relatorio = self.servicos.obter_conteudo_relatorio(nome_relatorio)

    # obtém o caminho para a pasta padrão de Downloads
        caminho_downloads = os.path.join(os.path.expanduser('~'), 'Downloads')

    # cria o caminho completo do arquivo
        nome_arquivo = os.path.join(caminho_downloads, f"relatorio_{nome_relatorio}.csv")

    # salva o conteúdo .csv
        with open(nome_arquivo, "w") as arquivo:
            arquivo.write(conteudo_relatorio)
        
            return nome_arquivo 


