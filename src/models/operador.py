from src.models.usuario import Usuario
from src.common.common import NIVEL_ACESSO_OPERADOR

class Operador(Usuario): # apagar depois
    '''classe para o operador que herda de usuario'''

    def __init__(self, nome, email, senha):
        super().__init__(nome, email, senha)
        self.nivel_acesso = NIVEL_ACESSO_OPERADOR

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
