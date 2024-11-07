from customtkinter import *

from . import tela_login, tela_agenda, tela_grafico
from src.common import common
from PIL import Image, ImageTk
import tkinter



def mostrar_tela_home(app, frame, img_label):

    teste = TRUE

    global tela_home_frame
    
    if teste:
        
        frame.place_forget()
        img_label.place_forget() 

        
        tela_home_frame = CTkFrame(master=app, width=500, height=400, corner_radius=15, border_color="")
        tela_home_frame.place(relx=0.5, rely= 0.5, anchor=CENTER)

        tela_home_frame_lateral = CTkFrame(master=app, width=65, height=300, corner_radius=10, border_color="", fg_color="#985698")
        tela_home_frame_lateral.place(relx=1.0, rely= 0.5, anchor=tkinter.E)

        img_sair = Image.open("src/resources/static/logout.png")
        img_sair = img_sair.resize((20, 20), Image.LANCZOS)
        img_tk = ImageTk.PhotoImage(img_sair)

        img_label_sair = CTkLabel(app, image=img_tk, text="", cursor="hand2")
        img_label_sair.image = img_tk
        img_label_sair.bind("<Button-1>", lambda event: sair(app))
        img_label_sair.place(x=25, y=20)

        img_alerta = Image.open("src/resources/static/safe.png")
        img_alerta = img_alerta.resize((100,100), Image.LANCZOS)
        img_tk1 = ImageTk.PhotoImage(img_alerta)

        img_label_alerta = CTkLabel(tela_home_frame, image=img_tk1, text="")
        img_label_alerta._image = img_tk1
        img_label_alerta.place(x=200, y=110)

        msg_label = CTkLabel(tela_home_frame, text="Resíduos em nível ok!", font=('Century Ghotic', 16))
        msg_label.place(x=175, y=240)

        img_agenda = Image.open("src/resources/static/agenda.png")
        img_agenda = img_agenda.resize((40,40), Image.LANCZOS)
        img_tk2 = ImageTk.PhotoImage(img_agenda)

        img_label_agenda = CTkLabel(tela_home_frame_lateral, image=img_tk2, text="", fg_color="#985698", cursor="hand2")
        img_label_agenda._image = img_tk2
        img_label_agenda.bind("<Button-1>", lambda event: tela_agenda.mostrar_tela_agenda(app, tela_home_frame, tela_home_frame_lateral))
        img_label_agenda.place(x=15, y=72.5)

        img_grafico = Image.open("src/resources/static/grafico.png")
        img_grafico = img_grafico.resize((40,40), Image.LANCZOS)
        img_tk3 = ImageTk.PhotoImage(img_grafico)

        img_label_grafico = CTkLabel(tela_home_frame_lateral, image=img_tk3, text="", fg_color="#985698", cursor="hand2")
        img_label_grafico._image = img_tk3
        img_label_grafico.bind("<Button-1>", lambda event: tela_grafico.mostrar_tela_grafico(app, tela_home_frame, tela_home_frame_lateral))
        img_label_grafico.place(x=12.5, y=187.5)

    
    else:

        frame.place_forget()
        img_label.place_forget() 

        
        tela_home_frame = CTkFrame(master=app, width=500, height=400, corner_radius=15, border_color="", fg_color="white")
        tela_home_frame.place(relx=0.5, rely= 0.5, anchor=CENTER)

        img_sair = Image.open("src/resources/static/logout.png")
        img_sair = img_sair.resize((20, 20), Image.LANCZOS)
        img_tk = ImageTk.PhotoImage(img_sair)

        img_label_sair = CTkLabel(app, image=img_tk, text="", cursor="hand2")
        img_label_sair.image = img_tk
        img_label_sair.bind("<Button-1>", lambda event: sair(app))
        img_label_sair.place(x=25, y=20)


def sair(app):

    from src.common.reset import reset_app
    reset_app(app)
    
     
