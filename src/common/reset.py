from src.controllers.sessao import SessaoUsuario

def reset_app(app):
    """realiza o logout e retorna para a tela de login"""
    SessaoUsuario.deslogar(app)