from src.models.data import Data
from src.services.servicos_relatorio import ServicosRelatorio
import pandas as pd
import os

class Relatorio:

    def __init__(self):
        
        self.data = Data()
        self.servicos = ServicosRelatorio()

    def gerar_relatorio(self):
        print("testando")
        
        # Carrega os dados e as colunas
        residuos_filtrados, colunas = self.data.load_data()
    
        # Converte o tipo da coluna 'anoGeracao' para inteiro, caso não esteja
        anos = [ano for ano in residuos_filtrados['anoGeracao'].unique() if ano.isdigit() and int(ano) >= 2012]
    
        for ano in anos:
            # Filtra dados para o ano específico
            dados_ano = residuos_filtrados[residuos_filtrados['anoGeracao'] == ano]
        
            if dados_ano.empty:
                print(f"Nenhum dado encontrado para o ano {ano}.")
                continue

            # Exibe o relatório
            print(f"Relatório do ano {ano}:\n{dados_ano}")

            # Salva no banco de dados e como arquivos TXT e CSV
            self.servicos.salvar_relatorio_bd(dados_ano, ano)

            print("testando 2")

    
    def carregar_relatorio(self, conteudo_relatorio):

        if isinstance(conteudo_relatorio, pd.DataFrame):
            conteudo_relatorio_str = conteudo_relatorio.to_string(index=False) 
        else:
            conteudo_relatorio_str = str(conteudo_relatorio)

        return conteudo_relatorio_str


    def baixar_relatorio(self, nome_relatorio):
    # Exemplo de código para baixar o relatório em CSV
        conteudo_relatorio = self.servicos.obter_conteudo_relatorio(nome_relatorio)

    # Obtém o caminho para o diretório padrão de Downloads
        caminho_downloads = os.path.join(os.path.expanduser('~'), 'Downloads')

    # Cria o caminho completo do arquivo
        nome_arquivo = os.path.join(caminho_downloads, f"relatorio_{nome_relatorio}.csv")

    # Salva o conteúdo no arquivo CSV
        with open(nome_arquivo, "w") as arquivo:
            arquivo.write(conteudo_relatorio)
        
            return nome_arquivo 


