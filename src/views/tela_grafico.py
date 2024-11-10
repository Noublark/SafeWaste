from customtkinter import *
from PIL import Image, ImageTk
from . import tela_home

class TelaGrafico:
    def __init__(self, app):
        self.app = app
        self.tela_grafico_frame = None
        self.img_label_voltar = None

    def mostrar_tela_grafico(self, frame, frame2):
        # Esconde os frames atuais
        frame.place_forget()
        frame2.place_forget()

        # Criação do frame da tela de gráfico
        self.tela_grafico_frame = CTkFrame(master=self.app, width=500, height=400, corner_radius=15, border_color="")
        self.tela_grafico_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        # Carrega e ajusta a imagem do botão "voltar"
        img_voltar = Image.open("src/resources/static/back arrow.png")
        img_voltar = img_voltar.resize((40, 50), Image.LANCZOS)
        img_tk = ImageTk.PhotoImage(img_voltar)

        # Criação do botão "voltar"
        self.img_label_voltar = CTkLabel(self.app, image=img_tk, text="", cursor="hand2")
        self.img_label_voltar.image = img_tk
        self.img_label_voltar.bind("<Button-1>", lambda event: self.voltar(frame, frame2))
        self.img_label_voltar.place(x=20, y=20)

    def voltar(self, frame_anterior, img_label_anterior):
        from .tela_home import TelaHome
        self.tela_grafico_frame.place_forget()
        self.img_label_voltar.place_forget()
        TelaHome(self.app).mostrar_tela_home(frame_anterior, img_label_anterior)

