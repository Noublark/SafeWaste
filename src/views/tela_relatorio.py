from customtkinter import *

from . import tela_home

from PIL import Image, ImageTk

def mostrar_tela_relatorio(app, frame, frame2):

    global tela_relatorio_frame

    frame.place_forget()
    frame2.place_forget()

    tela_relatorio_frame = CTkFrame(master=app, width=500, height=400, corner_radius=15, border_color="")
    tela_relatorio_frame.place(relx=0.5, rely= 0.5, anchor=CENTER)

    img_voltar = Image.open("src/resources/static/back arrow.png")
    img_voltar = img_voltar.resize((40, 50), Image.LANCZOS)
    img_tk = ImageTk.PhotoImage(img_voltar)

    img_label_voltar = CTkLabel(app, image=img_tk, text="", cursor="hand2")
    img_label_voltar.image = img_tk
    img_label_voltar.bind("<Button-1>", lambda event: voltar(app, tela_relatorio_frame, img_label_voltar))
    img_label_voltar.place(x=20, y=20)

    titulo = CTkLabel(tela_relatorio_frame, text="Relatórios", font=('Century Ghotic', 32))
    titulo.place(x=200, y=25)
    
    relatorios = CTkFrame(tela_relatorio_frame, width=300, height=300, corner_radius=8, fg_color="#080808")
    relatorios.place(x=25, y=80)

    relatorios_config = CTkFrame(tela_relatorio_frame, width=150, height=300, corner_radius=8, fg_color="#985698")
    relatorios_config.place(x=325, y=80)

    adicionar_labels_e_imagens(app, relatorios, relatorios_config, img_label_voltar, quantidade=3)



def ver_relatorio(app, frame, img_label_voltar):

    frame.place_forget()
    img_label_voltar.place_forget()

    tela_ver_relatorio_frame = CTkFrame(master=app, width=500, height=400, corner_radius=15, border_color="")
    tela_ver_relatorio_frame.place(relx=0.5, rely= 0.5, anchor=CENTER)

    img_voltar = Image.open("src/resources/static/back arrow.png")
    img_voltar = img_voltar.resize((40, 50), Image.LANCZOS)
    img_tk = ImageTk.PhotoImage(img_voltar)

    img_label_voltar = CTkLabel(app, image=img_tk, text="", cursor="hand2")
    img_label_voltar.image = img_tk
    img_label_voltar.bind("<Button-1>", lambda event: voltar_relatorio(app, tela_ver_relatorio_frame, tela_relatorio_frame, img_label_voltar))
    img_label_voltar.place(x=20, y=20)


def adicionar_labels_e_imagens(app, relatorios, relatorios_config, img_label_voltar, quantidade):
   
    y_inicial = 10
    espacamento_y = 60

    for i in range(quantidade):

        label = CTkLabel(relatorios, text="teste", font=('Century Gothic', 16))
        label.place(x=10, y=y_inicial + i * espacamento_y)

        img_ver = Image.open("src/resources/static/olho.png").resize((30, 30), Image.LANCZOS)
        img_tk1 = ImageTk.PhotoImage(img_ver)
        img_label_ver = CTkLabel(relatorios_config, image=img_tk1, text="", cursor="hand2")
        img_label_ver.image = img_tk1
        img_label_ver.bind("<Button-1>", lambda event: ver_relatorio(app, tela_relatorio_frame, img_label_voltar))
        img_label_ver.place(x=35, y=y_inicial + i * espacamento_y)

        img_baixar = Image.open("src/resources/static/download.png").resize((30, 30), Image.LANCZOS)
        img_tk2 = ImageTk.PhotoImage(img_baixar)
        img_label_baixar = CTkLabel(relatorios_config, image=img_tk2, text="", cursor="hand2")
        img_label_baixar.image = img_tk2
        img_label_baixar.place(x=95, y=y_inicial + i * espacamento_y)

    

def voltar(app, frame, img_label_voltar):

    frame.place_forget()
    tela_home.mostrar_tela_home(app, frame, img_label_voltar)


def voltar_relatorio(app, frame, tela_relatorio_frame, img_label_voltar):
    
    frame.place_forget()
    img_label_voltar.place_forget()
    mostrar_tela_relatorio(app, tela_relatorio_frame, frame)