from customtkinter import *
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
        self.marcacao_operador = tkinter.IntVar(value=0)
        self.marcacao_gestor_residuos = tkinter.IntVar(value=0)
        self.img_label_voltar = None
        self.img_label = None
        self.usuario_controller = UsuarioController()

    def mostrar_tela_cadastro(self, frame, img_label):
        # Esconde o frame e imagem anteriores
        frame.place_forget()
        img_label.place_forget()

        # Configura imagem do botão de voltar
        img_voltar = Image.open("src/resources/static/back arrow.png").resize((40, 50), Image.LANCZOS)
        img_tk = ImageTk.PhotoImage(img_voltar)

        self.img_label_voltar = CTkLabel(self.app, image=img_tk, text="", cursor="hand2")
        self.img_label_voltar.image = img_tk
        self.img_label_voltar.bind("<Button-1>", lambda event: self.voltar(self.cadastro_frame, self.img_label, self.img_label_voltar))
        self.img_label_voltar.place(x=20, y=20)

        # Cria o frame de cadastro
        self.cadastro_frame = CTkFrame(master=self.app, width=400, height=605, corner_radius=15, border_color="")
        self.cadastro_frame.place(relx=1.0, rely=0.5, anchor=tkinter.E)

        # Configura imagem da tela de cadastro
        img = Image.open("img_teste.png").resize((220, 200), Image.LANCZOS)
        img_tk = ImageTk.PhotoImage(img)
        self.img_label = CTkLabel(self.app, image=img_tk, text="")
        self.img_label.image = img_tk
        self.img_label.place(relx=0.12, rely=0.5, anchor=tkinter.W)

        # Campos de entrada e botões
        CTkLabel(self.cadastro_frame, text="Cadastro", font=('Century Ghotic', 32)).place(x=145, y=130)
        self.campo_nome = CTkEntry(self.cadastro_frame, placeholder_text="Digite seu nome", width=330, height=30, corner_radius=10)
        self.campo_nome.place(x=40, y=195)
        self.campo_email = CTkEntry(self.cadastro_frame, placeholder_text="Digite seu email", width=330, height=30, corner_radius=10)
        self.campo_email.place(x=40, y=250)
        self.campo_senha = CTkEntry(self.cadastro_frame, placeholder_text="Digite sua senha", width=330, height=30, show="*", corner_radius=10)
        self.campo_senha.place(x=40, y=305)
        self.campo_senha2 = CTkEntry(self.cadastro_frame, placeholder_text="Digite sua senha novamente", width=330, height=30, show="*", corner_radius=10)
        self.campo_senha2.place(x=40, y=360)

        # Checkboxes de nível de acesso
        operador_checkbox = CTkCheckBox(self.cadastro_frame, text="Operador", variable=self.marcacao_operador, onvalue=1, offvalue=0, command=self.atualizar_checkboxes)
        gestor_checkbox = CTkCheckBox(self.cadastro_frame, text="Gestor de Resíduos", variable=self.marcacao_gestor_residuos, onvalue=1, offvalue=0, command=self.atualizar_checkboxes)
        
        operador_checkbox.place(x=90, y=410)
        gestor_checkbox.place(x=190, y=410)
        
        # Botão de cadastro
        CTkButton(self.cadastro_frame, text="Cadastrar", command=self.cadastrar, corner_radius=10, fg_color="#985698", hover_color="#ee82ee", width=220).place(x=95, y=460)

    def atualizar_checkboxes(self):
        """Função que desmarca uma checkbox quando a outra é marcada"""
        if self.marcacao_operador.get() == 1:
            self.marcacao_gestor_residuos.set(0)  # Desmarcar "Gestor de Resíduos"
        elif self.marcacao_gestor_residuos.get() == 1:
            self.marcacao_operador.set(0)  # Desmarcar "Operador"

    def voltar(self, frame, img_label, img_label_voltar):
        from .tela_login import TelaLogin
        frame.place_forget()
        img_label_voltar.place_forget()
        TelaLogin(self.app).mostrar_tela_login(frame, img_label)

    def cadastrar(self):
        nome = self.campo_nome.get()    
        email = self.campo_email.get()
        senha = self.campo_senha.get()
        senha2 = self.campo_senha2.get()

        # Validações
        if not nome or not email or not senha or not senha2 or (self.marcacao_operador.get() == 0 and self.marcacao_gestor_residuos.get() == 0):
            self.mostrar_mensagem("Erro: Preencha todos os campos", "red")
            return

        if senha != senha2:
            self.mostrar_mensagem("Erro: Senhas diferentes", "red")
            return

        nivel_acesso = NIVEL_ACESSO_OPERADOR if self.marcacao_operador.get() == 1 else NIVEL_ACESSO_GESTOR_RESIDUOS
        resultado = self.usuario_controller.cadastro(nome, email, senha, nivel_acesso)

        if "Cadastro realizado com sucesso!" in resultado:
            self.mostrar_mensagem(resultado, "green")
        else:
            self.mostrar_mensagem(resultado, "red")

    def mostrar_mensagem(self, mensagem, cor):
        label_erro = CTkLabel(self.cadastro_frame, text=mensagem, text_color=cor)
        label_erro.place(x=115, y=500)
        self.cadastro_frame.after(1500, label_erro.place_forget)
