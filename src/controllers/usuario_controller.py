from src.models.usuario import Usuario

'''FAZER CODIGO DO CONTROLLER DE USUARIO AQUI, MEU PLANO É FAZER UMA LISTA ENCADEADA COM OS USUARIOS
QUE VAO SER REGISTRADOS E DPS MANDAR PRO BANCO DE DADOS'''


def cadastro(nome, email, senha, nivel_acesso):

    usuario = Usuario(nome, email, senha)
    resultado = usuario.cadastro(nivel_acesso)
    return resultado

def login(email, senha):

    usuario = Usuario(nome="", email=email, senha=senha)
    
    resultado = usuario.login()
    return resultado

def redefinir_senha(email, nova_senha):

    usuario = Usuario(nome="", email=email, senha=nova_senha)

    resultado = usuario.redefinir_senha()
    return resultado



