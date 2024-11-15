import sqlite3
from src.resources.db.conexao_sqlite import ConexaoSQLite

class ServicosColeta:

    def __init__(self):
        self.conexao_db = ConexaoSQLite()

    def criar_tabela(self):
        """Cria a tabela de coleta, caso ainda não exista."""
        conn = self.conexao_db.conexao()
        if conn is None:
            return "Erro ao conectar ao banco de dados."

        cursor = conn.cursor()

        try:
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS coleta (
                id_coleta INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                tipo_residuo TEXT NOT NULL,
                data DATE NOT NULL,
                endereco TEXT NOT NULL,
                id_usuario INTEGER NOT NULL,
                status TEXT DEFAULT 'pendente',  -- Adiciona status com valor padrão 'pendente'
                FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario)
                    ON DELETE CASCADE
                    ON UPDATE CASCADE
            );
            """)
            conn.commit()
            print("Tabela 'coleta' criada ou já existente.")
        except sqlite3.Error as erro:
            print(f"Erro ao criar a tabela: {erro}")
        finally:
            conn.close()

    def salvar_coleta_db(self, tipo_residuo, data, endereco, id_usuario):
        """Salva uma nova coleta no banco de dados."""
        conn = self.conexao_db.conexao()
        if conn is None:
            return "Erro ao conectar ao banco de dados."

        cursor = conn.cursor()

        try:
            cursor.execute("""
            INSERT INTO coleta (tipo_residuo, data, endereco, id_usuario)
            VALUES (?, ?, ?, ?);
            """, (tipo_residuo, data, endereco, id_usuario))
            conn.commit()
            return "Coleta agendada com sucesso!"
        except sqlite3.Error as erro:
            return f"Erro ao agendar a coleta: {erro}"
        finally:
            conn.close()

    def concluir_coleta_db(self, id_coleta):
        """Marca uma coleta como concluída."""
        conn = self.conexao_db.conexao()
        if conn is None:
            return "Erro ao conectar ao banco de dados."

        cursor = conn.cursor()

        try:
            cursor.execute("""
            UPDATE coleta
            SET status = 'concluída'
            WHERE id_coleta = ?;
            """, (id_coleta,))
            conn.commit()
            return "Coleta concluída com sucesso!"
        except sqlite3.Error as erro:
            return f"Erro ao concluir a coleta: {erro}"
        finally:
            conn.close()

    def editar_coleta_db(self, id_coleta, novo_tipo_residuo, nova_data, novo_endereco):
        """Edita uma coleta existente."""
        conn = self.conexao_db.conexao()
        if conn is None:
            return "Erro ao conectar ao banco de dados."

        cursor = conn.cursor()

        try:
            cursor.execute("""
            UPDATE coleta
            SET tipo_residuo = ?, data = ?, endereco = ?
            WHERE id_coleta = ?;
            """, (novo_tipo_residuo, nova_data, novo_endereco, id_coleta))
            conn.commit()
            return "Coleta editada com sucesso!"
        except sqlite3.Error as erro:
            return f"Erro ao editar a coleta: {erro}"
        finally:
            conn.close()

    def cancelar_coleta_db(self, id_coleta):
        """Cancela uma coleta, removendo-a do banco de dados."""
        conn = self.conexao_db.conexao()
        if conn is None:
            return "Erro ao conectar ao banco de dados."

        cursor = conn.cursor()

        try:
            cursor.execute("DELETE FROM coleta WHERE id_coleta = ?;", (id_coleta,))
            conn.commit()
            return "Coleta cancelada com sucesso!"
        except sqlite3.Error as erro:
            return f"Erro ao cancelar a coleta: {erro}"
        finally:
            conn.close()

    def obter_coletas_usuario(self, id_usuario):
        """Obtém todas as coletas associadas a um usuário específico."""
        conn = self.conexao_db.conexao()
        if conn is None:
            return "Erro ao conectar ao banco de dados."

        cursor = conn.cursor()

        try:
            cursor.execute("SELECT * FROM coleta WHERE id_usuario = ?;", (id_usuario,))
            coletas = cursor.fetchall()
            return coletas
        except sqlite3.Error as erro:
            return f"Erro ao obter coletas: {erro}"
        finally:
            conn.close()
