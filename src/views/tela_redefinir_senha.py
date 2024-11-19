from customtkinter import CTk, CTkFrame, CTkLabel, CTkEntry, CTkButton
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

    def esconder_todos_frames(self):
        frames = [
            self.redefinir_senha_frame
        ]
        
        labels = [
            self.img_label_voltar,
            self.img_label
        ]
        
        for frame in frames:
            if frame:
                frame.destroy()
                
        for label in labels:
            if label:
                label.destroy()

    def mostrar_tela_redefinir_senha(self):
        
        self.esconder_todos_frames()

        # Botão voltar
        img_voltar = Image.open("src/resources/static/back arrow.png").resize((40, 50), Image.LANCZOS)
        img_tk = ImageTk.PhotoImage(img_voltar)
        self.img_label_voltar = CTkLabel(self.app, image=img_tk, text="", cursor="hand2")
        self.img_label_voltar.image = img_tk
        self.img_label_voltar.bind("<Button-1>", lambda e: self.voltar())
        self.img_label_voltar.place(x=20, y=20)

        # Frame principal
        self.redefinir_senha_frame = CTkFrame(self.app, width=400, height=605, corner_radius=15, border_color="")
        self.redefinir_senha_frame.place(relx=1.0, rely=0.5, anchor=tkinter.E)

        # Imagem
        img = Image.open("src/resources/static/icon.png").resize((220, 200), Image.LANCZOS)
        img_tk = ImageTk.PhotoImage(img)
        self.img_label = CTkLabel(self.app, image=img_tk, text="")
        self.img_label.image = img_tk
        self.img_label.place(relx=0.135, rely=0.5, anchor=tkinter.W)

        # Campos
        CTkLabel(self.redefinir_senha_frame, text="Redefinir Senha", font=('Century Gothic', 32)).place(x=100, y=150)
        
        self.campo_email = CTkEntry(self.redefinir_senha_frame, placeholder_text="Digite seu email", width=330, corner_radius=10)
        self.campo_email.place(x=40, y=235)
        
        self.campo_senha = CTkEntry(self.redefinir_senha_frame, placeholder_text="Digite sua senha", width=330, show="*", corner_radius=10)
        self.campo_senha.place(x=40, y=290)
        
        self.campo_senha2 = CTkEntry(self.redefinir_senha_frame, placeholder_text="Digite sua senha novamente", width=330, show="*", corner_radius=10)
        self.campo_senha2.place(x=40, y=345)

        # Botão redefinir
        CTkButton(self.redefinir_senha_frame, text="Redefinir", command=self.redefinir_senha,
                 fg_color="#985698", hover_color="#ee82ee", width=220, corner_radius=10).place(x=95, y=405)

    def voltar(self):
        from .tela_login import TelaLogin
        self.esconder_todos_frames()
        TelaLogin(self.app).mostrar_tela_login()

    def redefinir_senha(self):
        email = self.campo_email.get()
        nova_senha = self.campo_senha.get()
        nova_senha2 = self.campo_senha2.get()

        if not all([email, nova_senha, nova_senha2]):
            self.mostrar_mensagem("Erro: Preencha todos os campos", "red")
            return

        if nova_senha != nova_senha2:
            self.mostrar_mensagem("Erro: Senhas diferentes", "red")
            return

        resultado = self.usuario_controller.redefinir_senha(email, nova_senha)
        cor = "green" if "sucesso" in resultado.lower() else "red"
        tempo = 2000 if "sucesso" in resultado.lower() else 1500
        self.mostrar_mensagem(resultado, cor, tempo)

    def mostrar_mensagem(self, mensagem, cor, tempo=1500):
        label = CTkLabel(self.redefinir_senha_frame, text=mensagem, text_color=cor)
        label.place(x=115, y=445)
        self.redefinir_senha_frame.after(tempo, label.place_forget)
