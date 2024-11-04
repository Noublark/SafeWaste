from src.models.usuario import Usuario, usuario1
from src.common.common import NIVEL_ACESSO_OPERADOR

class Operador(Usuario):
    '''classe para o operador que herda de usuario'''

    def __init__(self, nome, email, senha, nivel_acesso):
        super().__init__(nome, email, senha)
        self.nivel_acesso = nivel_acesso

    def agendar_coleta(self):
        pass

    def editar_coleta(self):
        pass

    def cancelar_coleta(self):
        pass

    def concluir_coleta(self):
        pass

    def exibir_coletas(self):
        pass

    def eixibir_grafico(self):
        pass
