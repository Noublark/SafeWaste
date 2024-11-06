from customtkinter import *
import tkinter
from PIL import Image, ImageTk
from . import tela_login

def mostrar_tela_cadastro(app, frame, img_label):
    
    frame.place_forget()
    img_label.place_forget() 

    img_voltar = Image.open("src/resources/static/back arrow.png")
    img_voltar = img_voltar.resize((40, 50), Image.LANCZOS)
    img_tk = ImageTk.PhotoImage(img_voltar)

    img_label_voltar = CTkLabel(app, image=img_tk, text="", cursor="hand2")
    img_label_voltar.image = img_tk
    img_label_voltar.bind("<Button-1>", lambda event: voltar(app, cadastro_frame, img_label, img_label_voltar))
    img_label_voltar.place(x=20, y=20)

    global cadastro_frame
    cadastro_frame = CTkFrame(master=app, width=400, height=605, corner_radius=15, border_color="")
    cadastro_frame.place(relx=1.0, rely= 0.5, anchor=tkinter.E)

    img = Image.open("img_teste.png")
    img = img.resize((220, 200), Image.LANCZOS) 
    img_tk = ImageTk.PhotoImage(img)

    img_label = CTkLabel(app, image=img_tk, text="")
    img_label.image = img_tk
    img_label.place(relx=0.12, rely=0.5, anchor=tkinter.W) 

    titulo = CTkLabel(cadastro_frame, text="Cadastro", font=('Century Ghotic', 32))
    titulo.place(x=145, y=130)

    campo_nome = CTkEntry(cadastro_frame, placeholder_text="Digite seu nome", width=330, height=30, corner_radius=10)
    campo_nome.place(x=40, y=195)

    campo_email = CTkEntry(cadastro_frame, placeholder_text="Digite seu email", width=330,height=30 , corner_radius=10)
    campo_email.place(x=40, y=250)

    campo_senha = CTkEntry(cadastro_frame, placeholder_text="Digite sua senha", width=330,height=30 , show="*", corner_radius=10)
    campo_senha.place(x=40, y=305)

    campo_senha2 = CTkEntry(cadastro_frame, placeholder_text="Digite sua senha novamente", width=330,height=30,  show="*", corner_radius=10)
    campo_senha2.place(x=40, y=360)

    marcacao_operador = tkinter.IntVar(value=0)
    marcacao_gestor_residuos = tkinter.IntVar(value=0)

    checkbox_operador = CTkCheckBox(cadastro_frame, text="Operador", variable=marcacao_operador, onvalue=1, offvalue=0, command=lambda: marcacao_checkbox(marcacao_operador, marcacao_gestor_residuos))
    checkbox_operador.place(x=90, y=410)

    checkbox_gestor_residuos = CTkCheckBox(cadastro_frame, text="Gestor de Resíduos", variable=marcacao_gestor_residuos, onvalue=1, offvalue=0, command=lambda: marcacao_checkbox(marcacao_gestor_residuos, marcacao_operador))
    checkbox_gestor_residuos.place(x=190, y=410)

    btn_cadastrar = CTkButton(cadastro_frame, text="Cadastrar", command= lambda: print("testando"), corner_radius=10, fg_color= "#985698", hover_color="#ee82ee", width=220)
    btn_cadastrar.place(x=95, y=460)


def marcacao_checkbox(checkbox_marcada, outra_checkbox):

    if checkbox_marcada.get() == 1:
        outra_checkbox.set(0)


def voltar(app, frame, img_label, img_label_voltar):

    frame.place_forget()
    img_label_voltar.place_forget()
    tela_login.mostrar_tela_login(app, frame, img_label)