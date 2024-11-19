from customtkinter import CTk, CTkFrame, CTkLabel, CTkEntry, CTkButton
import tkinter
from PIL import Image, ImageTk
from src.controllers.usuario_controller import UsuarioController
from src.common import common
from .tela_cadastro import TelaCadastro
from .tela_redefinir_senha import TelaRedefinirSenha
from .tela_home import TelaHome


class TelaLogin:
    def __init__(self, app):
        self.app = app
        self.login_frame = None
        self.campo_email = None 
        self.campo_senha = None
        self.img_label = None
        self.tela_cadastro = TelaCadastro(app)
        self.tela_redefinir_senha = TelaRedefinirSenha(app)
        self.tela_home = TelaHome(app)
        self.usuario_controller = UsuarioController()

    def mostrar_tela_login(self, frame, img_label):
        # Remove tela anterior
        self.app.unbind("<Button-1>")
        frame.pack_forget()
        img_label.place_forget()

        # Configura frame de login
        self.login_frame = CTkFrame(self.app, width=400, height=605, corner_radius=15, border_color="")
        self.login_frame.place(relx=1.0, rely=0.5, anchor=tkinter.E)

        # Configura imagem
        img = Image.open("src/resources/static/icon.png").resize((220, 200), Image.LANCZOS)
        img_tk = ImageTk.PhotoImage(img)
        self.img_label = CTkLabel(self.app, image=img_tk, text="")
        self.img_label.image = img_tk
        self.img_label.place(relx=0.135, rely=0.5, anchor=tkinter.W)

        # Título
        CTkLabel(self.login_frame, text="Faça Login", font=('Century Gothic', 32)).place(x=130, y=150)

        # Campos de entrada
        self.campo_email = CTkEntry(self.login_frame, placeholder_text="Digite seu email", width=330, height=30, corner_radius=10)
        self.campo_email.place(x=40, y=235)

        self.campo_senha = CTkEntry(self.login_frame, placeholder_text="Digite sua senha", width=330, height=30, show="*", corner_radius=10)
        self.campo_senha.place(x=40, y=290)

        # Link redefinir senha
        link_senha = CTkLabel(self.login_frame, text="Esqueceu a senha?", text_color="lightblue", cursor="hand2")
        link_senha.bind("<Button-1>", lambda e: self.tela_redefinir_senha.mostrar_tela_redefinir_senha(self.login_frame, self.img_label))
        link_senha.place(x=250, y=320)

        # Botão login
        CTkButton(self.login_frame, text="Entrar", command=self.verificar_login, corner_radius=10, 
                 fg_color="#985698", hover_color="#ee82ee", width=330).place(x=40, y=370)

        # Links cadastro
        CTkLabel(self.login_frame, text="Não tem uma conta?", font=('Century Gothic', 12)).place(x=40, y=410)
        link_cadastro = CTkLabel(self.login_frame, text="Cadastre-se", text_color="lightblue", cursor="hand2")
        link_cadastro.bind("<Button-1>", lambda e: self.tela_cadastro.mostrar_tela_cadastro(self.login_frame, self.img_label))
        link_cadastro.place(x=160, y=410)

    def verificar_login(self):
        email = self.campo_email.get()
        senha = self.campo_senha.get()

        if not email or not senha:
            self._mostrar_erro("Erro: Preencha todos os campos")
            return

        resultado, tipo_usuario = self.usuario_controller.login(email, senha)

        if "Login bem-sucedido" in resultado:
            common.nivel_acesso = tipo_usuario
            self.tela_home.mostrar_tela_home(self.login_frame, self.img_label)
        else:
            self._mostrar_erro(resultado)

    def _mostrar_erro(self, mensagem):
        erro = CTkLabel(self.login_frame, text=mensagem, text_color="red")
        erro.place(x=45, y=320)
        self.login_frame.after(1500, erro.place_forget)
