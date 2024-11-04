from src.models.usuario import Usuario

class Gestor_Residuos(Usuario):
    '''classe para o gestor de residuos que herda de usuario'''

    def __init__(self, nome, email, senha):
        super().__init__(nome, email, senha)

    def exibir_grafico(self):
        pass

    def gerar_relatorio(self):
        pass

    def receber_alerta(self):
        pass