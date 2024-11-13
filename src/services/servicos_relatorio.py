import sqlite3
from src.resources.db.conexao_sqlite import ConexaoSQLite
from src.models.data import Data
import pandas as pd

class ServicosRelatorio:
    
    def __init__(self):
        self.conexao_db = ConexaoSQLite()
        self.data = Data()

    def criar_tabela(self):
        conn = self.conexao_db.conexao()
        cursor = conn.cursor()

        try:
            # Carrega os dados do JSON
            residuos_filtrados, _ = self.data.load_data()

            residuos_filtrados['anoGeracao'] = pd.to_numeric(residuos_filtrados['anoGeracao'], errors='coerce')

            # Obtém o intervalo de anos para criação das tabelas
            ultimo_ano = residuos_filtrados['anoGeracao'].max()
            anos = range(2012, int(ultimo_ano) + 1)

            # Cria uma tabela para cada ano no intervalo de 2012 até o último ano
            for ano in anos:
                cursor.execute(f"""
                    CREATE TABLE IF NOT EXISTS relatorio_{ano} (
                        cnpjGerador TEXT,
                        detalhe TEXT,
                        estado TEXT,
                        municipio TEXT,
                        anoGeracao TEXT,
                        tipoResiduo TEXT,
                        quantidadeGerada TEXT,
                        unidade TEXT,
                        classificacaoResiduo TEXT
                    )
                """)
                conn.commit()
                print(f"Tabela relatorio_{ano} criada ou já existente.")

        except (sqlite3.Error) as erro:
            print(f"Erro ao criar as tabelas: {erro}")
        finally:
            conn.close()

    def salvar_relatorio_bd(self, dados, ano):
        conn = self.conexao_db.conexao()
        cursor = conn.cursor()

        try:
            # Insere os dados do ano na tabela correspondente
            for _, row in dados.iterrows():
                print(f"Inserindo dados para o CNPJ {row['cnpjGerador']} no ano {ano}: {tuple(row)}")
                
                cursor.execute(f"""
                    INSERT INTO relatorio_{ano} (cnpjGerador, detalhe, estado, municipio, anoGeracao, 
                    tipoResiduo, quantidadeGerada, unidade, classificacaoResiduo)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, tuple(row))

            # Commit após todos os inserts
            conn.commit()
            print(f"Relatório de {ano} salvo no banco de dados.")
        except sqlite3.Error as erro:
            print(f"Erro ao salvar o relatório do ano {ano} no banco de dados: {erro}")
        finally:
            conn.close()

    def salvar_como_txt(self, dados_ano, ano):
        # Salva o relatório do ano em formato TXT
        nome_arquivo = f"relatorio_{ano}.txt"
        with open(nome_arquivo, "w") as f:
            f.write(dados_ano.to_string(index=False))
        print(f"Relatório salvo como {nome_arquivo}.")

    # Função para obter os nomes dos relatórios (tabelas) no banco de dados
    def obter_nomes_relatorios(self):
        conn = self.conexao_db.conexao()
        cursor = conn.cursor()
        try:
            # Consulta para obter os nomes das tabelas no banco de dados
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name LIKE 'relatorio_%';")
            tabelas = cursor.fetchall()
            # Extrai apenas os anos dos nomes das tabelas (assumindo que os nomes começam com 'relatorio_')
            anos = [tabela[0].replace("relatorio_", "") for tabela in tabelas]
            return anos
        except sqlite3.Error as erro:
            print(f"Erro ao obter os nomes dos relatórios: {erro}")
            return []
        finally:
            conn.close()

    # Função para obter o conteúdo de um relatório específico
    def obter_conteudo_relatorio(self, nome_relatorio):
        conn = self.conexao_db.conexao()
        cursor = conn.cursor()

        try:
            # Garante que o nome da tabela começa com "relatorio_"
            if not nome_relatorio.startswith("relatorio_"):
                nome_relatorio = f"relatorio_{nome_relatorio}"
            
            # Prepara a consulta para acessar a tabela com o nome correto
            query = f"SELECT * FROM {nome_relatorio}"

            # Executa a consulta
            cursor.execute(query)
            
            # Obtém os resultados da consulta
            conteudo = cursor.fetchall()

            # Se os dados foram encontrados, converte para um formato legível
            if conteudo:
                conteudo_str = "\n".join([str(row) for row in conteudo])  # Converte todas as linhas para string
                return conteudo_str
            else:
                print(f"Nenhum dado encontrado para o relatório {nome_relatorio}.")
                return "Nenhum dado encontrado."

        except sqlite3.Error as erro:
            print(f"Erro ao obter o conteúdo do relatório {nome_relatorio}: {erro}")
            return f"Erro: {erro}"

        finally:
            conn.close()

    # Função para apagar todas as tabelas de relatórios
    def apagar_tabelas(self):
        conn = self.conexao_db.conexao()
        cursor = conn.cursor()
        try:
            # Consulta para apagar todas as tabelas de relatórios
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name LIKE 'relatorio_%';")
            tabelas = cursor.fetchall()
            for tabela in tabelas:
                cursor.execute(f"DROP TABLE IF EXISTS {tabela[0]}")
            conn.commit()
            print("Todas as tabelas de relatórios foram apagadas.")
        except sqlite3.Error as erro:
            print(f"Erro ao apagar as tabelas de relatórios: {erro}")
        finally:
            conn.close()
