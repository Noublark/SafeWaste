class SessaoUsuario:
    usuario_logado = None

    @classmethod
    def login(cls, usuario):
        cls.usuario_logado = usuario

    @classmethod
    def logout(cls):
        cls.usuario_logado = None

    @classmethod
    def get_usuario_logado(cls):
        return cls.usuario_logado
    
    @classmethod
    def obter_id_usuario(cls):
        """retorna o ID do usuário logado, caso exista"""
        if cls.usuario_logado:
            return cls.usuario_logado.id
        return None

    @classmethod
    def deslogar(cls, app):
        """realiza o logout do usuário e reinicia a aplicação"""
        cls.logout()  # limpa o usuário logado
        from src.views.tela_login import TelaLogin
        
        # limpa todos os widgets existentes
        for widget in app.winfo_children():
            widget.destroy()
            
        # mostra a tela de login
        tela_login = TelaLogin(app)
        tela_login.mostrar_tela_login()