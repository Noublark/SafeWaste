from src.services.servicos_usuarios import Servicos_Usuario

class Usuario:
    '''Classe para o usuário do SafeWaste'''

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

    def cadastro(self, nivel_acesso):
        '''Método para realizar o cadastro do usuário'''
        
        # Chama o serviço de cadastro
        resultado = Servicos_Usuario().cadastrar_usuario(self.nome, self.email, self.senha, nivel_acesso)
        return resultado

    def login(self):
        '''Método para realizar o login do usuário'''

        # Chama o serviço de login
        resultado = Servicos_Usuario().login(self.email, self.senha)
        return resultado

    def redefinir_senha(self, nova_senha):
        '''Método para redefinir a senha do usuário'''

        # Chama o serviço para redefinir a senha
        resultado = Servicos_Usuario().redefinir_senha(self.email, nova_senha)
        return resultado