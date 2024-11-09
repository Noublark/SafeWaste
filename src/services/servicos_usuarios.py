from hashlib import sha256
import sqlite3
from src.resources.db.conexao_sqlite import ConexaoSQLite

class Servicos_Usuario:
    def __init__(self):
        self.conexao_db = ConexaoSQLite()

    def criar_tabela_usuario(self):
        """Cria a tabela 'usuario' no banco de dados, caso não exista."""
        conn = self.conexao_db.conexao()
        if conn is None:
            return "Erro ao conectar ao banco de dados."

        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuario (
                id_usuario INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                nome TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                senha TEXT NOT NULL,
                tipo_usuario TEXT CHECK(tipo_usuario IN ('Operador', 'Gestor_Residuos')) NOT NULL
            );
        """)
        conn.commit()
        conn.close()

    def cadastrar_usuario(self, nome, email, senha, tipo_usuario):
        """Realiza o cadastro de um novo usuário no banco de dados."""
        
        if not self.validar_email(email):
            return "Erro: O email já está registrado."

        senha_hash = self.hash_senha(senha)
        
        conn = self.conexao_db.conexao()
        if conn is None:
            return "Erro ao conectar ao banco de dados."

        cursor = conn.cursor()
        try:
            cursor.execute("""
                INSERT INTO usuario (nome, email, senha, tipo_usuario) 
                VALUES (?, ?, ?, ?);
            """, (nome, email, senha_hash, tipo_usuario))
            conn.commit()
            return "Cadastro realizado com sucesso!"
        except sqlite3.IntegrityError as e:
            if 'UNIQUE constraint failed: usuario.email' in str(e):
                return "Erro: O email já está registrado."
            else:
                return f"Erro desconhecido: {e}"
        finally:
            conn.close()

    def login(self, email, senha):
        """Realiza o login verificando o email e senha do usuário."""
        senha_hash = self.hash_senha(senha)
        
        conn = self.conexao_db.conexao()
        if conn is None:
            return "Erro ao conectar ao banco de dados."

        cursor = conn.cursor()
        cursor.execute("""
            SELECT id_usuario, nome, tipo_usuario FROM usuario 
            WHERE email = ? AND senha = ?;
        """, (email, senha_hash))
        usuario = cursor.fetchone()
        
        if usuario:
            tipo_usuario = usuario[2]  # Obtém o tipo de usuário (ex: "operador", "gestor_residuos")
            return f"Login bem-sucedido! Bem-vindo, {usuario[1]}.", tipo_usuario
        else:
            return "Erro: Email ou senha incorretos.", None
        conn.close()

    def redefinir_senha(self, email, nova_senha):
        """Redefine a senha do usuário, dado o email e a nova senha."""
        senha_hash = self.hash_senha(nova_senha)
        
        conn = self.conexao_db.conexao()
        if conn is None:
            return "Erro ao conectar ao banco de dados."

        cursor = conn.cursor()
        cursor.execute("""
            UPDATE usuario 
            SET senha = ? 
            WHERE email = ?;
        """, (senha_hash, email))
        
        if cursor.rowcount > 0:
            conn.commit()
            return "Senha redefinida com sucesso!"
        else:
            return "Erro: Email não encontrado."
        conn.close()

    def hash_senha(self, senha):
        """Retorna o hash da senha usando SHA-256."""
        return sha256(senha.encode()).hexdigest()

    def validar_email(self, email):
        """Verifica se o email já está registrado no banco de dados."""
        conn = self.conexao_db.conexao()
        if conn is None:
            return False

        cursor = conn.cursor()
        cursor.execute("SELECT email FROM usuario WHERE email = ?;", (email,))
        result = cursor.fetchone()
        conn.close()
        return result is None
