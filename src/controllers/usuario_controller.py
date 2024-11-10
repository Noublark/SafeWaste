from src.models.usuario import Usuario

class UsuarioController:

    def __init__(self):
        self.usuario = None

    def cadastro(self, nome, email, senha, nivel_acesso):
        self.usuario = Usuario(nome, email, senha)
        resultado = self.usuario.cadastro(nivel_acesso)
        return resultado

    def login(self, email, senha):
        self.usuario = Usuario(nome="", email=email, senha=senha)
        resultado = self.usuario.login()
        return resultado

    def redefinir_senha(self, email, nova_senha):
        self.usuario = Usuario(nome="", email=email, senha=nova_senha)
        resultado = self.usuario.redefinir_senha(nova_senha)
        return resultado
