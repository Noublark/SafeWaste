from customtkinter import *
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
        self.img_label1 = None
        self.tipo_usuario = None
        self.tela_cadastro = TelaCadastro(self.app)
        self.tela_redefinir_senha = TelaRedefinirSenha(self.app)
        self.tela_home = TelaHome(self.app)
        self.usuario_controller = UsuarioController()

    def mostrar_tela_login(self, frame, img_label):
        self.app.unbind("<Button-1>")
        frame.pack_forget()
        img_label.place_forget()

        # Configura frame de login
        self.login_frame = CTkFrame(master=self.app, width=400, height=605, corner_radius=15, border_color="")
        self.login_frame.place(relx=1.0, rely=0.5, anchor=tkinter.E)

        # Configura a imagem de login
        img = Image.open("img_teste.png").resize((220, 200), Image.LANCZOS)
        img_tk = ImageTk.PhotoImage(img)

        self.img_label1 = CTkLabel(self.app, image=img_tk, text="")
        self.img_label1.image = img_tk
        self.img_label1.place(relx=0.12, rely=0.5, anchor=tkinter.W)

        # Título de login
        titulo = CTkLabel(self.login_frame, text="Faça Login", font=('Century Gothic', 32))
        titulo.place(x=130, y=150)

        # Campos de entrada
        self.campo_email = CTkEntry(self.login_frame, placeholder_text="Digite seu email", width=330, height=30, corner_radius=10)
        self.campo_email.place(x=40, y=235)

        self.campo_senha = CTkEntry(self.login_frame, placeholder_text="Digite sua senha", width=330, height=30, show="*", corner_radius=10)
        self.campo_senha.place(x=40, y=290)

        # Link para redefinir senha
        hyperlink_redefinir_senha = CTkLabel(self.login_frame, text="Esqueceu a senha?", text_color="lightblue", cursor="hand2")
        hyperlink_redefinir_senha.bind("<Button-1>", lambda event: self.tela_redefinir_senha.mostrar_tela_redefinir_senha(self.login_frame, self.img_label1))
        hyperlink_redefinir_senha.place(x=250, y=320)

        # Botão de login
        btn_login = CTkButton(master=self.login_frame, text="Entrar", command=self.verificar_login, corner_radius=10, fg_color="#985698", hover_color="#ee82ee", width=330)
        btn_login.place(x=40, y=370)

        # Cadastro
        label = CTkLabel(self.login_frame, text="Não tem uma conta?", font=('Century Gothic', 12))
        label.place(x=40, y=410)

        hyperlink_cadastro = CTkLabel(self.login_frame, text="Cadastre-se", text_color="lightblue", cursor="hand2")
        hyperlink_cadastro.bind("<Button-1>", lambda event: self.tela_cadastro.mostrar_tela_cadastro(self.login_frame, self.img_label1))
        hyperlink_cadastro.place(x=160, y=410)

    def verificar_login(self):
        email = self.campo_email.get()
        senha = self.campo_senha.get()

        if email == "" or senha == "":
            label_erro = CTkLabel(self.login_frame, text="Erro: Preencha todos os campos", text_color="red")
            label_erro.place(x=45, y=320)
            self.login_frame.after(1500, label_erro.place_forget)
            return

        resultado, self.tipo_usuario = self.usuario_controller.login(email, senha)

        if "Login bem-sucedido" in resultado:
            common.nivel_acesso = self.tipo_usuario
            self.tela_home.mostrar_tela_home(self.login_frame, self.img_label1)
        else:
            label_erro = CTkLabel(self.login_frame, text=resultado, text_color="red")
            label_erro.place(x=45, y=320)
            self.login_frame.after(1500, label_erro.place_forget)
