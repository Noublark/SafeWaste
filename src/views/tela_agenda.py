from customtkinter import *
from . import tela_home
from PIL import Image, ImageTk

def mostrar_tela_agenda(app, frame, frame2):

    global tela_agenda_frame

    frame.place_forget()
    frame2.place_forget()

    tela_agenda_frame = CTkFrame(master=app, width=500, height=400, corner_radius=15, border_color="")
    tela_agenda_frame.place(relx=0.5, rely= 0.5, anchor=CENTER)

    img_voltar = Image.open("src/resources/static/back arrow.png")
    img_voltar = img_voltar.resize((40, 50), Image.LANCZOS)
    img_tk = ImageTk.PhotoImage(img_voltar)

    img_label_voltar = CTkLabel(app, image=img_tk, text="", cursor="hand2")
    img_label_voltar.image = img_tk
    img_label_voltar.bind("<Button-1>", lambda event: voltar(app, tela_agenda_frame, img_label_voltar))
    img_label_voltar.place(x=20, y=20)


def voltar(app, frame, img_label_voltar):

    frame.place_forget()
    tela_home.mostrar_tela_home(app, frame, img_label_voltar)