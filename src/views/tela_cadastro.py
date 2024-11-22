from customtkinter import CTk, CTkFrame, CTkLabel, CTkEntry, CTkButton, CTkCheckBox
import tkinter
from PIL import Image, ImageTk
from src.controllers.usuario_controller import UsuarioController
from src.common.common import NIVEL_ACESSO_OPERADOR, NIVEL_ACESSO_GESTOR_RESIDUOS


class TelaCadastro:
    def __init__(self, app):
        self.app = app
        self.cadastro_frame = None
        self.campo_nome = None
        self.campo_email = None
        self.campo_senha = None
        self.campo_senha2 = None
        self.marcacao_operador = tkinter.IntVar()
        self.marcacao_gestor_residuos = tkinter.IntVar() 
        self.img_label_voltar = None
        self.img_label = None
        self.usuario_controller = UsuarioController()

    def esconder_todos_frames(self): #Função para esconder todos os frames
        frames = [
            self.cadastro_frame
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

    def mostrar_tela_cadastro(self):
        
        self.esconder_todos_frames()

        img_voltar = Image.open("src/resources/static/back arrow.png").resize((40, 50), Image.LANCZOS)
        img_tk = ImageTk.PhotoImage(img_voltar)
        self.img_label_voltar = CTkLabel(self.app, image=img_tk, text="", cursor="hand2")
        self.img_label_voltar.image = img_tk
        self.img_label_voltar.bind("<Button-1>", lambda e: self.voltar())
        self.img_label_voltar.place(x=20, y=20)

        self.cadastro_frame = CTkFrame(self.app, width=400, height=605, corner_radius=15, border_color="")
        self.cadastro_frame.place(relx=1.0, rely=0.5, anchor=tkinter.E)

        img = Image.open("src/resources/static/icon.png").resize((220, 200), Image.LANCZOS)
        img_tk = ImageTk.PhotoImage(img)
        self.img_label = CTkLabel(self.app, image=img_tk, text="")
        self.img_label.image = img_tk
        self.img_label.place(relx=0.135, rely=0.5, anchor=tkinter.W)

        CTkLabel(self.cadastro_frame, text="Cadastro", font=('Century Gothic', 32)).place(x=145, y=130)
        
        self.campo_nome = CTkEntry(self.cadastro_frame, placeholder_text="Digite seu nome", width=330, height=30, corner_radius=10)
        self.campo_nome.place(x=40, y=195)
        
        self.campo_email = CTkEntry(self.cadastro_frame, placeholder_text="Digite seu email", width=330, height=30, corner_radius=10)
        self.campo_email.place(x=40, y=250)
        
        self.campo_senha = CTkEntry(self.cadastro_frame, placeholder_text="Digite sua senha", width=330, height=30, show="*", corner_radius=10)
        self.campo_senha.place(x=40, y=305)
        
        self.campo_senha2 = CTkEntry(self.cadastro_frame, placeholder_text="Digite sua senha novamente", width=330, height=30, show="*", corner_radius=10)
        self.campo_senha2.place(x=40, y=360)
        
        CTkCheckBox(self.cadastro_frame, text="Operador", variable=self.marcacao_operador, 
                   command=self.atualizar_checkboxes).place(x=90, y=410)
        CTkCheckBox(self.cadastro_frame, text="Gestor de Resíduos", variable=self.marcacao_gestor_residuos,
                   command=self.atualizar_checkboxes).place(x=190, y=410)
        
        CTkButton(self.cadastro_frame, text="Cadastrar", command=self.cadastrar, 
                 fg_color="#985698", hover_color="#ee82ee", width=220, corner_radius=10).place(x=95, y=460)

    def atualizar_checkboxes(self):
        if self.marcacao_operador.get():
            self.marcacao_gestor_residuos.set(0)
        elif self.marcacao_gestor_residuos.get():
            self.marcacao_operador.set(0)

    def voltar(self):
        from .tela_login import TelaLogin
        self.esconder_todos_frames()
        TelaLogin(self.app).mostrar_tela_login()

    def cadastrar(self):
        nome = self.campo_nome.get()    
        email = self.campo_email.get()
        senha = self.campo_senha.get()
        senha2 = self.campo_senha2.get()

        if not all([nome, email, senha, senha2]) or not (self.marcacao_operador.get() or self.marcacao_gestor_residuos.get()):
            self.mostrar_mensagem("Erro: Preencha todos os campos", "red")
            return

        if senha != senha2:
            self.mostrar_mensagem("Erro: Senhas diferentes", "red")
            return

        nivel_acesso = NIVEL_ACESSO_OPERADOR if self.marcacao_operador.get() else NIVEL_ACESSO_GESTOR_RESIDUOS
        resultado = self.usuario_controller.cadastro(nome, email, senha, nivel_acesso)
        
        cor = "green" if "sucesso" in resultado.lower() else "red"
        self.mostrar_mensagem(resultado, cor)

    def mostrar_mensagem(self, mensagem, cor):
        label = CTkLabel(self.cadastro_frame, text=mensagem, text_color=cor)
        label.place(x=115, y=500)
        self.cadastro_frame.after(1500, label.place_forget)
