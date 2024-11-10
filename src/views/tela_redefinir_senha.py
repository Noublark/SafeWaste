from customtkinter import *
import tkinter
from PIL import Image, ImageTk
from src.controllers.usuario_controller import UsuarioController


class TelaRedefinirSenha:
    def __init__(self, app):
        self.app = app
        self.redefinir_senha_frame = None
        self.campo_email = None
        self.campo_senha = None
        self.campo_senha2 = None
        self.img_label_voltar = None
        self.img_label = None
        self.usuario_controller = UsuarioController()

    def mostrar_tela_redefinir_senha(self, frame, img_label):
        # Esconde o frame e a imagem anteriores
        frame.place_forget()
        img_label.place_forget()

        # Configura imagem do botão de voltar
        img_voltar = Image.open("src/resources/static/back arrow.png")
        img_voltar = img_voltar.resize((40, 50), Image.LANCZOS)
        img_tk = ImageTk.PhotoImage(img_voltar)

        self.img_label_voltar = CTkLabel(self.app, image=img_tk, text="", cursor="hand2")
        self.img_label_voltar.image = img_tk
        self.img_label_voltar.bind("<Button-1>", lambda event: self.voltar(self.redefinir_senha_frame, self.img_label, self.img_label_voltar))
        self.img_label_voltar.place(x=20, y=20)

        # Cria o frame de redefinir senha
        self.redefinir_senha_frame = CTkFrame(master=self.app, width=400, height=605, corner_radius=15, border_color="")
        self.redefinir_senha_frame.place(relx=1.0, rely=0.5, anchor=tkinter.E)

        # Configura imagem da tela
        img = Image.open("img_teste.png")
        img = img.resize((220, 200), Image.LANCZOS)
        img_tk = ImageTk.PhotoImage(img)

        self.img_label = CTkLabel(self.app, image=img_tk, text="")
        self.img_label.image = img_tk
        self.img_label.place(relx=0.12, rely=0.5, anchor=tkinter.W)

        # Configura título
        titulo = CTkLabel(self.redefinir_senha_frame, text="Redefinir Senha", font=('Century Ghotic', 32))
        titulo.place(x=100, y=150)

        # Campos de entrada
        self.campo_email = CTkEntry(self.redefinir_senha_frame, placeholder_text="Digite seu email", width=330, corner_radius=10)
        self.campo_email.place(x=40, y=235)

        self.campo_senha = CTkEntry(self.redefinir_senha_frame, placeholder_text="Digite sua senha", width=330, show="*", corner_radius=10)
        self.campo_senha.place(x=40, y=290)

        self.campo_senha2 = CTkEntry(self.redefinir_senha_frame, placeholder_text="Digite sua senha novamente", width=330, show="*", corner_radius=10)
        self.campo_senha2.place(x=40, y=345)

        # Botão de redefinir senha
        btn_redefinir_senha = CTkButton(self.redefinir_senha_frame, text="Redefinir", command=self.redefinir_senha, corner_radius=10, fg_color="#985698", hover_color="#ee82ee", width=220)
        btn_redefinir_senha.place(x=95, y=405)

    def voltar(self, frame, img_label, img_label_voltar):
        from .tela_login import TelaLogin
        frame.place_forget()
        img_label_voltar.place_forget()
        TelaLogin(self.app).mostrar_tela_login(frame, img_label)

    def redefinir_senha(self):
        email = self.campo_email.get()
        nova_senha = self.campo_senha.get()
        nova_senha2 = self.campo_senha2.get()

        # Validações
        if email == "" or nova_senha == "" or nova_senha2 == "":
            self.mostrar_mensagem("Erro: Preencha todos os campos", "red")
            return

        if nova_senha != nova_senha2:
            self.mostrar_mensagem("Erro: Senhas diferentes", "red")
            return

        resultado = self.usuario_controller.redefinir_senha(email, nova_senha)

        if "Senha redefinida com sucesso!" in resultado:
            self.mostrar_mensagem(resultado, "green", tempo=2000)
        else:
            self.mostrar_mensagem(resultado, "red")

    def mostrar_mensagem(self, mensagem, cor, tempo=1500):
        label_erro = CTkLabel(self.redefinir_senha_frame, text=mensagem, text_color=cor)
        label_erro.place(x=115, y=445)
        self.redefinir_senha_frame.after(tempo, label_erro.place_forget)
