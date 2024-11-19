from src.controllers.sessao import SessaoUsuario

def reset_app(app):
    """Realiza o logout e retorna para a tela de login"""
    SessaoUsuario.deslogar(app)