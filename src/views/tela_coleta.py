from customtkinter import *

from . import tela_home
from PIL import Image, ImageTk
import tkinter

def mostrar_tela_coleta(app, frame, frame2):

    global tela_coleta_frame

    frame.place_forget()
    frame2.place_forget()

    tela_coleta_frame = CTkFrame(master=app, width=500, height=400, corner_radius=15, border_color="")
    tela_coleta_frame.place(relx=0.5, rely= 0.5, anchor=CENTER)

    img_voltar = Image.open("src/resources/static/back arrow.png")
    img_voltar = img_voltar.resize((40, 50), Image.LANCZOS)
    img_tk = ImageTk.PhotoImage(img_voltar)

    img_label_voltar = CTkLabel(app, image=img_tk, text="", cursor="hand2")
    img_label_voltar.image = img_tk
    img_label_voltar.bind("<Button-1>", lambda event: voltar(app, tela_coleta_frame, img_label_voltar))
    img_label_voltar.place(x=20, y=20)

    titulo = CTkLabel(tela_coleta_frame, text="Coletas", font=('Century Ghotic', 32))
    titulo.place(x=200, y=25)

    coletas = CTkFrame(tela_coleta_frame, width=300, height=300, corner_radius=8, fg_color="#080808", border_color="")
    coletas.place(x=25, y=80)

    coletas_config = CTkFrame(tela_coleta_frame, width=150, height=300, corner_radius=8, fg_color="#985698", border_color="")
    coletas_config.place(x=325, y=80)

    adicionar_labels_e_imagens(coletas, coletas_config,quantidade=3)

def adicionar_labels_e_imagens(coletas, coletas_config, quantidade):
   
    y_inicial = 10
    espacamento_y = 60

    for i in range(quantidade):

        label = CTkLabel(coletas, text="teste", font=('Century Gothic', 16))
        label.place(x=10, y=y_inicial + i * espacamento_y)

        img_concluido = Image.open("src/resources/static/concluido.png").resize((30, 30), Image.LANCZOS)
        img_tk1 = ImageTk.PhotoImage(img_concluido)
        img_label_concluido = CTkLabel(coletas_config, image=img_tk1, text="", cursor="hand2")
        img_label_concluido.image = img_tk1
        img_label_concluido.place(x=13, y=y_inicial + i * espacamento_y)

        img_editar = Image.open("src/resources/static/lapis.png").resize((30, 30), Image.LANCZOS)
        img_tk2 = ImageTk.PhotoImage(img_editar)
        img_label_editar = CTkLabel(coletas_config, image=img_tk2, text="", cursor="hand2")
        img_label_editar.image = img_tk2
        img_label_editar.place(x=63, y=y_inicial + i * espacamento_y)

        img_remover = Image.open("src/resources/static/lixeira.png").resize((30, 30), Image.LANCZOS)
        img_tk3 = ImageTk.PhotoImage(img_remover)
        img_label_remover = CTkLabel(coletas_config, image=img_tk3, text="", cursor="hand2")
        img_label_remover.image = img_tk3
        img_label_remover.place(x=113, y=y_inicial + i * espacamento_y)


def voltar(app, frame, img_label_voltar):

    frame.place_forget()
    tela_home.mostrar_tela_home(app, frame, img_label_voltar)