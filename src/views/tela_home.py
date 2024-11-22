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

    def esconder_frames(self): # função para esconder todos os frames
        if self.tela_home_frame:
            self.tela_home_frame.place_forget()
        if self.tela_home_frame_lateral:
            self.tela_home_frame_lateral.place_forget()
        if self.img_label_sair:
            self.img_label_sair.place_forget()
        if self.img_label_alerta:
            self.img_label_alerta.place_forget()
        if self.img_label_agenda:
            self.img_label_agenda.place_forget()
        if self.img_label_grafico:
            self.img_label_grafico.place_forget()
        if self.img_label_relatorio:
            self.img_label_relatorio.place_forget()
        if self.msg_label:
            self.msg_label.place_forget()

    def mostrar_tela_home(self):

        self.esconder_frames()

        # verifica o nível de acesso e cria a tela correspondente
        if common.nivel_acesso == "Operador":
            self.criar_tela_home_operador()
        elif common.nivel_acesso == "Gestor_Residuos":
            self.criar_tela_home_gestor_residuos()

    def criar_tela_home_operador(self):
        self.tela_home_frame = CTkFrame(master=self.app, width=500, height=400, corner_radius=15, border_color="")
        self.tela_home_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.tela_home_frame_lateral = CTkFrame(master=self.app, width=65, height=300, corner_radius=10, border_color="", fg_color="#985698")
        self.tela_home_frame_lateral.place(relx=1.0, rely=0.5, anchor=tkinter.E)

        img_sair = self.carregar_imagem("src/resources/static/logout.png", (20, 20))
        self.img_label_sair = CTkLabel(self.app, image=img_sair, text="", cursor="hand2")
        self.img_label_sair.image = img_sair
        self.img_label_sair.bind("<Button-1>", lambda event: self.sair())
        self.img_label_sair.place(x=25, y=20)

        img_alerta = self.carregar_imagem("src/resources/static/safe.png", (100, 100))
        self.img_label_alerta = CTkLabel(self.tela_home_frame, image=img_alerta, text="")
        self.img_label_alerta._image = img_alerta
        self.img_label_alerta.place(x=200, y=110)

        self.msg_label = CTkLabel(self.tela_home_frame, text="Resíduos em nível ok!", font=('Century Ghotic', 16))
        self.msg_label.place(x=175, y=240)

        img_agenda = self.carregar_imagem("src/resources/static/agenda.png", (45, 45))
        self.img_label_agenda = CTkLabel(self.tela_home_frame_lateral, image=img_agenda, text="", fg_color="#985698", cursor="hand2")
        self.img_label_agenda._image = img_agenda
        self.img_label_agenda.bind("<Button-1>", lambda event: self.tela_coleta.mostrar_tela_coleta(self.tela_home_frame_lateral))
        self.img_label_agenda.place(x=10, y=72.5)

        img_grafico = self.carregar_imagem("src/resources/static/grafico.png", (40, 40))
        self.img_label_grafico = CTkLabel(self.tela_home_frame_lateral, image=img_grafico, text="", fg_color="#985698", cursor="hand2")
        self.img_label_grafico._image = img_grafico
        self.img_label_grafico.bind("<Button-1>", lambda event: self.tela_grafico.mostrar_tela_grafico(self.tela_home_frame_lateral))
        self.img_label_grafico.place(x=12.5, y=187.5)

    def criar_tela_home_gestor_residuos(self):
        self.tela_home_frame = CTkFrame(master=self.app, width=500, height=400, corner_radius=15, border_color="")
        self.tela_home_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.tela_home_frame_lateral = CTkFrame(master=self.app, width=65, height=300, corner_radius=10, border_color="", fg_color="#985698")
        self.tela_home_frame_lateral.place(relx=1.0, rely=0.5, anchor=tkinter.E)

        img_sair = self.carregar_imagem("src/resources/static/logout.png", (20, 20))
        self.img_label_sair = CTkLabel(self.app, image=img_sair, text="", cursor="hand2")
        self.img_label_sair.image = img_sair
        self.img_label_sair.bind("<Button-1>", lambda event: self.sair())
        self.img_label_sair.place(x=25, y=20)

        img_alerta = self.carregar_imagem("src/resources/static/safe.png", (100, 100))
        self.img_label_alerta = CTkLabel(self.tela_home_frame, image=img_alerta, text="")
        self.img_label_alerta._image = img_alerta
        self.img_label_alerta.place(x=200, y=110)

        self.msg_label = CTkLabel(self.tela_home_frame, text="Resíduos em nível ok!", font=('Century Ghotic', 16))
        self.msg_label.place(x=175, y=240)

        img_relatorio = self.carregar_imagem("src/resources/static/relatorio.png", (50, 50))
        self.img_label_relatorio = CTkLabel(self.tela_home_frame_lateral, image=img_relatorio, text="", fg_color="#985698", cursor="hand2")
        self.img_label_relatorio._image = img_relatorio
        self.img_label_relatorio.bind("<Button-1>", lambda event: self.tela_relatorio.mostrar_tela_relatorio(self.tela_home_frame_lateral))
        self.img_label_relatorio.place(x=8, y=72.5)

        img_grafico = self.carregar_imagem("src/resources/static/grafico.png", (40, 40))
        self.img_label_grafico = CTkLabel(self.tela_home_frame_lateral, image=img_grafico, text="", fg_color="#985698", cursor="hand2")
        self.img_label_grafico._image = img_grafico
        self.img_label_grafico.bind("<Button-1>", lambda event: self.tela_grafico.mostrar_tela_grafico(self.tela_home_frame_lateral))
        self.img_label_grafico.place(x=12.5, y=187.5)

    
    def abrir_tela_coleta(self):
        self.esconder_frames()
        self.tela_coleta.mostrar_tela_coleta(self.tela_home_frame_lateral)

    def abrir_tela_grafico(self):
        self.esconder_frames()
        self.tela_grafico.mostrar_tela_grafico(self.tela_home_frame_lateral)

    def abrir_tela_relatorio(self):
        self.esconder_frames()
        self.tela_relatorio.mostrar_tela_relatorio(self.tela_home_frame_lateral)
    
    def mostrar_popup_sair(self):
        self.mostrar_popup_sair_frame = CTkFrame(master=self.tela_home_frame, width=400, height=250, corner_radius=15, border_color="", fg_color="#080808")
        self.mostrar_popup_sair_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        titulo3 = CTkLabel(self.mostrar_popup_sair_frame, text="Deseja sair?", font=('Century Ghotic', 32))
        titulo3.place(relx=0.52, rely=0.3, anchor=CENTER)

        btn_sim = CTkButton(master=self.mostrar_popup_sair_frame, text="Sim", command=lambda: self.sair(), corner_radius=10, fg_color="#985698", hover_color="#ee82ee", width=125)
        btn_sim.place(x=225, y=150)

        btn_não = CTkButton(master=self.mostrar_popup_sair_frame, text="Não", command=self.mostrar_popup_sair_frame.destroy, corner_radius=10, fg_color="#b20000", hover_color="#e50000", width=125)
        btn_não.place(x=50, y=150)
    
    
    def carregar_imagem(self, caminho, tamanho):
        try:
            img = Image.open(caminho)
            img = img.resize(tamanho, Image.LANCZOS)
            return ImageTk.PhotoImage(img)
        except Exception as e:
            print(f"Erro ao carregar imagem {caminho}: {str(e)}")
            return None

    def sair(self):
        try:
            from src.common.reset import reset_app
            self.esconder_frames()
            reset_app(self.app)
        except Exception as e:
            print(f"Erro ao sair: {str(e)}")
