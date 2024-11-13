import sqlite3

class ConexaoSQLite:
    
    def conexao(self):
        conn = None
        try:
            url = "src/resources/db/safewaste.db"
            conn = sqlite3.connect(url)
        except sqlite3.Error as erro:
            print(f"Erro na conexão: {erro}")
        return conn
    