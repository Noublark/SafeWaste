import sqlite3
from src.resources.db.conexao_sqlite import ConexaoSQLite
from src.models.data import Data
import pandas as pd

class ServicosRelatorio:
    
    def __init__(self):
        self.conexao_db = ConexaoSQLite()
        self.data = Data()

    def criar_tabela(self): # remover essa função depois
        conn = self.conexao_db.conexao()
        cursor = conn.cursor()

        try:
            # carrega os dados do JSON
            resultado = self.data.load_data()

            
            if isinstance(resultado, pd.DataFrame):
                residuos_filtrados = resultado
            elif isinstance(resultado, tuple) and len(resultado) > 0:
                residuos_filtrados = resultado[0]  
            else:
                print("Erro: O retorno de load_data() não é um DataFrame ou tupla válida.")
                return

            residuos_filtrados['anoGeracao'] = pd.to_datetime(residuos_filtrados['anoGeracao'], errors='coerce')
            ultimo_ano = residuos_filtrados['anoGeracao'].dt.year.max()  # Extrai o ano do Timestamp
            anos = range(2012, int(ultimo_ano) + 1)
            
            colunas = ", ".join([f"{coluna} TEXT" for coluna in residuos_filtrados.columns])

            # cria uma tabela para cada ano no intervalo de 2012 até o último ano
            for ano in anos:
                cursor.execute(f"""
                    CREATE TABLE IF NOT EXISTS relatorio_{ano} (
                        {colunas}
                    )
                """)
                conn.commit()
                print(f"Tabela relatorio_{ano} criada ou já existente.")

        except (sqlite3.Error) as erro:
            print(f"Erro ao criar as tabelas: {erro}")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")
        finally:
            conn.close()

    def salvar_relatorio_bd(self, dados, ano):
        conn = self.conexao_db.conexao()
        cursor = conn.cursor()

        try:
            # insere os dados do ano na tabela correspondente
            for _, row in dados.iterrows():
                print(f"Inserindo dados para o CNPJ {row['cnpjGerador']} no ano {ano}: {tuple(row)}")
                
                ano_geracao_str = row['anoGeracao'].strftime('%Y-%m-%d') if isinstance(row['anoGeracao'], pd.Timestamp) else row['anoGeracao']
                
                cursor.execute(f"""
                    INSERT INTO relatorio_{ano} (cnpjGerador, estado, municipio, anoGeracao, 
                    tipoResiduo, quantidadeGerada, classificacaoResiduo)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                """, (row['cnpjGerador'], row['estado'], row['municipio'], ano_geracao_str, 
                      row['tipoResiduo'], row['quantidadeGerada'], row['classificacaoResiduo']))

            conn.commit()
            print(f"Relatório de {ano} salvo no banco de dados.")
        except sqlite3.Error as erro:
            print(f"Erro ao salvar o relatório do ano {ano} no banco de dados: {erro}")
        finally:
            conn.close()

    # função para obter os nomes dos relatórios no banco de dados
    def obter_nomes_relatorios(self):
        conn = self.conexao_db.conexao()
        cursor = conn.cursor()
        try:
            # consulta para obter os nomes das tabelas no banco de dados
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name LIKE 'relatorio_%';")
            tabelas = cursor.fetchall()
            # extrai apenas os anos dos nomes das tabelas 
            anos = [tabela[0].replace("relatorio_", "") for tabela in tabelas]
            return anos
        except sqlite3.Error as erro:
            print(f"Erro ao obter os nomes dos relatórios: {erro}")
            return []
        finally:
            conn.close()

    # função para obter o conteúdo de um relatório específico
    def obter_conteudo_relatorio(self, nome_relatorio):
        conn = self.conexao_db.conexao()
        cursor = conn.cursor()

        try:
            # garante que o nome da tabela começa com "relatorio_"
            if not nome_relatorio.startswith("relatorio_"):
                nome_relatorio = f"relatorio_{nome_relatorio}"
            
            # consulta para acessar a tabela, limitando a 50 linhas
            query = f"SELECT * FROM {nome_relatorio} LIMIT 50"
            cursor.execute(query)
            
            conteudo = cursor.fetchall()

            if conteudo:
                conteudo_str = "\n".join([str(row) for row in conteudo])  # converte todas as linhas para string
                return conteudo_str
            else:
                print(f"Nenhum dado encontrado para o relatório {nome_relatorio}.")
                return "Nenhum dado encontrado."

        except sqlite3.Error as erro:
            print(f"Erro ao obter o conteúdo do relatório {nome_relatorio}: {erro}")
            return f"Erro: {erro}"

        finally:
            conn.close()
