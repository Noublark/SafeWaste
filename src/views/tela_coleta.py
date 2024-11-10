from customtkinter import *
from PIL import Image, ImageTk
from . import tela_home
import tkinter


class TelaColeta:
    def __init__(self, app):
        self.app = app
        self.tela_coleta_frame = None
        self.img_label_voltar = None

    def mostrar_tela_coleta(self, frame, frame2):
        # Esconde os frames anteriores
        frame.place_forget()
        frame2.place_forget()

        # Criação do frame da tela de coleta
        self.tela_coleta_frame = CTkFrame(master=self.app, width=500, height=400, corner_radius=15, border_color="")
        self.tela_coleta_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        # Carregar e ajustar a imagem do botão "voltar"
        img_voltar = Image.open("src/resources/static/back arrow.png")
        img_voltar = img_voltar.resize((40, 50), Image.LANCZOS)
        img_tk = ImageTk.PhotoImage(img_voltar)

        # Criação do botão "voltar"
        self.img_label_voltar = CTkLabel(self.app, image=img_tk, text="", cursor="hand2")
        self.img_label_voltar.image = img_tk
        self.img_label_voltar.bind("<Button-1>", lambda event: self.voltar(frame, frame2))
        self.img_label_voltar.place(x=20, y=20)

        # Título da tela de coleta
        titulo = CTkLabel(self.tela_coleta_frame, text="Coletas", font=('Century Ghotic', 32))
        titulo.place(x=200, y=25)

        # Frames para coletas e configurações
        coletas = CTkFrame(self.tela_coleta_frame, width=300, height=300, corner_radius=8, fg_color="#080808", border_color="")
        coletas.place(x=25, y=80)

        coletas_config = CTkFrame(self.tela_coleta_frame, width=150, height=300, corner_radius=8, fg_color="#985698", border_color="")
        coletas_config.place(x=325, y=80)

        # Adiciona labels e imagens
        self.adicionar_labels_e_imagens(coletas, coletas_config, quantidade=3)

    def adicionar_labels_e_imagens(self, coletas, coletas_config, quantidade):
        y_inicial = 10
        espacamento_y = 60

        for i in range(quantidade):
            # Criação de labels e imagens de coleta
            label = CTkLabel(coletas, text="teste", font=('Century Gothic', 16))
            label.place(x=10, y=y_inicial + i * espacamento_y)

            # Imagem de concluído
            img_concluido = Image.open("src/resources/static/concluido.png").resize((30, 30), Image.LANCZOS)
            img_tk1 = ImageTk.PhotoImage(img_concluido)
            img_label_concluido = CTkLabel(coletas_config, image=img_tk1, text="", cursor="hand2")
            img_label_concluido.image = img_tk1
            img_label_concluido.place(x=13, y=y_inicial + i * espacamento_y)

            # Imagem de editar
            img_editar = Image.open("src/resources/static/lapis.png").resize((30, 30), Image.LANCZOS)
            img_tk2 = ImageTk.PhotoImage(img_editar)
            img_label_editar = CTkLabel(coletas_config, image=img_tk2, text="", cursor="hand2")
            img_label_editar.image = img_tk2
            img_label_editar.place(x=63, y=y_inicial + i * espacamento_y)

            # Imagem de remover
            img_remover = Image.open("src/resources/static/lixeira.png").resize((30, 30), Image.LANCZOS)
            img_tk3 = ImageTk.PhotoImage(img_remover)
            img_label_remover = CTkLabel(coletas_config, image=img_tk3, text="", cursor="hand2")
            img_label_remover.image = img_tk3
            img_label_remover.place(x=113, y=y_inicial + i * espacamento_y)

    def voltar(self, frame_anterior, img_label_anterior):
        from .tela_home import TelaHome
        self.tela_coleta_frame.place_forget()
        self.img_label_voltar.place_forget()
        TelaHome(self.app).mostrar_tela_home(frame_anterior, img_label_anterior)
