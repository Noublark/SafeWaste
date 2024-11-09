from src.models.usuario import Usuario
from src.common.common import NIVEL_ACESSO_GESTOR_RESIDUOS

class Gestor_Residuos(Usuario):
    '''classe para o gestor de residuos que herda de usuario'''

    def __init__(self, nome, email, senha):
        super().__init__(nome, email, senha)
        self.nivel_acesso = NIVEL_ACESSO_GESTOR_RESIDUOS

    def exibir_grafico(self):
        pass

    def gerar_relatorio(self):
        pass

    def receber_alerta(self):
        pass