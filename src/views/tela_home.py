from customtkinter import *
from .tela_grafico import TelaGrafico
from .tela_coleta import TelaColeta
from .tela_relatorio import TelaRelatorio
from src.common import common
from PIL import Image, ImageTk
import tkinter


class TelaHome:
    def __init__(self, app):
        self.app = app
        self.tela_home_frame = None
        self.tela_home_frame_lateral = None
        self.img_label_sair = None
        self.img_label_alerta = None
        self.img_label_agenda = None
        self.img_label_grafico = None
        self.img_label_relatorio = None
        self.msg_label = None
        self.tela_grafico = TelaGrafico(self.app)
        self.tela_coleta = TelaColeta(self.app)
        self.tela_relatorio = TelaRelatorio(self.app)

    def mostrar_tela_home(self, frame, img_label):
        # Esconde a tela anterior
        frame.place_forget()
        img_label.place_forget()

        # Verifica o nível de acesso e cria a tela correspondente
        if common.nivel_acesso == "Operador":
            self.criar_tela_home_operador()
        elif common.nivel_acesso == "Gestor_Residuos":
            self.criar_tela_home_gestor_residuos()

    def criar_tela_home_operador(self):
        # Cria o frame principal
        self.tela_home_frame = CTkFrame(master=self.app, width=500, height=400, corner_radius=15, border_color="")
        self.tela_home_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        # Cria o frame lateral
        self.tela_home_frame_lateral = CTkFrame(master=self.app, width=65, height=300, corner_radius=10, border_color="", fg_color="#985698")
        self.tela_home_frame_lateral.place(relx=1.0, rely=0.5, anchor=tkinter.E)

        # Botão de sair
        img_sair = self.carregar_imagem("src/resources/static/logout.png", (20, 20))
        self.img_label_sair = CTkLabel(self.app, image=img_sair, text="", cursor="hand2")
        self.img_label_sair.image = img_sair
        self.img_label_sair.bind("<Button-1>", lambda event: self.sair())
        self.img_label_sair.place(x=25, y=20)

        # Imagem de alerta
        img_alerta = self.carregar_imagem("src/resources/static/safe.png", (100, 100))
        self.img_label_alerta = CTkLabel(self.tela_home_frame, image=img_alerta, text="")
        self.img_label_alerta._image = img_alerta
        self.img_label_alerta.place(x=200, y=110)

        # Mensagem
        self.msg_label = CTkLabel(self.tela_home_frame, text="Resíduos em nível ok!", font=('Century Ghotic', 16))
        self.msg_label.place(x=175, y=240)

        # Botão para agenda
        img_agenda = self.carregar_imagem("src/resources/static/agenda.png", (40, 40))
        self.img_label_agenda = CTkLabel(self.tela_home_frame_lateral, image=img_agenda, text="", fg_color="#985698", cursor="hand2")
        self.img_label_agenda._image = img_agenda
        self.img_label_agenda.bind("<Button-1>", lambda event: self.tela_coleta.mostrar_tela_coleta(self.tela_home_frame, self.tela_home_frame_lateral))
        self.img_label_agenda.place(x=15, y=72.5)

        # Botão para gráfico
        img_grafico = self.carregar_imagem("src/resources/static/grafico.png", (40, 40))
        self.img_label_grafico = CTkLabel(self.tela_home_frame_lateral, image=img_grafico, text="", fg_color="#985698", cursor="hand2")
        self.img_label_grafico._image = img_grafico
        self.img_label_grafico.bind("<Button-1>", lambda event: self.tela_grafico.mostrar_tela_grafico(self.tela_home_frame, self.tela_home_frame_lateral))
        self.img_label_grafico.place(x=12.5, y=187.5)

    def criar_tela_home_gestor_residuos(self):
        # Cria o frame principal
        self.tela_home_frame = CTkFrame(master=self.app, width=500, height=400, corner_radius=15, border_color="")
        self.tela_home_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        # Cria o frame lateral
        self.tela_home_frame_lateral = CTkFrame(master=self.app, width=65, height=300, corner_radius=10, border_color="", fg_color="#985698")
        self.tela_home_frame_lateral.place(relx=1.0, rely=0.5, anchor=tkinter.E)

        # Botão de sair
        img_sair = self.carregar_imagem("src/resources/static/logout.png", (20, 20))
        self.img_label_sair = CTkLabel(self.app, image=img_sair, text="", cursor="hand2")
        self.img_label_sair.image = img_sair
        self.img_label_sair.bind("<Button-1>", lambda event: self.sair())
        self.img_label_sair.place(x=25, y=20)

        # Imagem de alerta
        img_alerta = self.carregar_imagem("src/resources/static/safe.png", (100, 100))
        self.img_label_alerta = CTkLabel(self.tela_home_frame, image=img_alerta, text="")
        self.img_label_alerta._image = img_alerta
        self.img_label_alerta.place(x=200, y=110)

        # Mensagem
        self.msg_label = CTkLabel(self.tela_home_frame, text="Resíduos em nível ok!", font=('Century Ghotic', 16))
        self.msg_label.place(x=175, y=240)

        # Botão para relatórios
        img_relatorio = self.carregar_imagem("src/resources/static/relatorio.png", (40, 40))
        self.img_label_relatorio = CTkLabel(self.tela_home_frame_lateral, image=img_relatorio, text="", fg_color="#985698", cursor="hand2")
        self.img_label_relatorio._image = img_relatorio
        self.img_label_relatorio.bind("<Button-1>", lambda event: self.tela_relatorio.mostrar_tela_relatorio(self.tela_home_frame, self.tela_home_frame_lateral))
        self.img_label_relatorio.place(x=15, y=72.5)

        # Botão para gráfico
        img_grafico = self.carregar_imagem("src/resources/static/grafico.png", (40, 40))
        self.img_label_grafico = CTkLabel(self.tela_home_frame_lateral, image=img_grafico, text="", fg_color="#985698", cursor="hand2")
        self.img_label_grafico._image = img_grafico
        self.img_label_grafico.bind("<Button-1>", lambda event: self.tela_grafico.mostrar_tela_grafico(self.tela_home_frame, self.tela_home_frame_lateral))
        self.img_label_grafico.place(x=12.5, y=187.5)

    def carregar_imagem(self, caminho, tamanho):
        img = Image.open(caminho)
        img = img.resize(tamanho, Image.LANCZOS)
        return ImageTk.PhotoImage(img)

    def sair(self):
        from src.common.reset import reset_app
        reset_app(self.app)
