from customtkinter import *
import tkinter
from PIL import Image, ImageTk
from . import tela_login

def mostrar_tela_cadastro(app, login_frame):
    
    login_frame.pack_forget()

    img_voltar = Image.open("src/resources/static/back arrow.png")
    img_voltar = img_voltar.resize((40, 50), Image.LANCZOS)
    img_tk1 = ImageTk.PhotoImage(img_voltar)

    img_label_voltar = CTkLabel(app, image=img_tk1, text="", cursor="hand2")
    img_label_voltar.image = img_tk1
    img_label_voltar.bind("<Button-1>", lambda event: voltar(app, cadastro_frame, img_label_voltar))
    img_label_voltar.place(x=20, y=20)

    global cadastro_frame
    cadastro_frame = CTkFrame(master=app, width=436, height=500, corner_radius=15, border_color="")
    cadastro_frame.place(relx=0.5, rely= 0.5, anchor=tkinter.CENTER)

    img = Image.open("img_teste.png")
    img = img.resize((220, 200), Image.LANCZOS) 
    img_tk = ImageTk.PhotoImage(img)

    img_label = CTkLabel(cadastro_frame, image=img_tk, text="")
    img_label.image = img_tk
    img_label.place(x= 103, y= 5)

    titulo = CTkLabel(cadastro_frame, text="Cadastro", font=('Century Ghotic', 32))
    titulo.place(x=150, y=200)

    campo_nome = CTkEntry(cadastro_frame, placeholder_text="Digite seu nome", width=330, corner_radius=10)
    campo_nome.place(x=50, y=250)

    campo_email = CTkEntry(cadastro_frame, placeholder_text="Digite seu email", width=330, corner_radius=10)
    campo_email.place(x=50, y=290)

    campo_senha = CTkEntry(cadastro_frame, placeholder_text="Digite sua senha", width=330, show="*", corner_radius=10)
    campo_senha.place(x=50, y=330)

    campo_senha2 = CTkEntry(cadastro_frame, placeholder_text="Digite sua senha novamente", width=330, show="*", corner_radius=10)
    campo_senha2.place(x=50, y=370)

    marcacao_operador = tkinter.IntVar(value=0)
    marcacao_gestor_residuos = tkinter.IntVar(value=0)

    checkbox_operador = CTkCheckBox(cadastro_frame, text="Operador", variable=marcacao_operador, onvalue=1, offvalue=0, command=lambda: marcacao_checkbox(marcacao_operador, marcacao_gestor_residuos))
    checkbox_operador.place(x=100, y=410)

    checkbox_gestor_residuos = CTkCheckBox(cadastro_frame, text="Gestor de Resíduos", variable=marcacao_gestor_residuos, onvalue=1, offvalue=0, command=lambda: marcacao_checkbox(marcacao_gestor_residuos, marcacao_operador))
    checkbox_gestor_residuos.place(x=200, y=410)

    btn_cadastrar = CTkButton(cadastro_frame, text="Cadastrar", command= lambda: print("testando"), corner_radius=10, fg_color= "#985698", hover_color="#ee82ee", width=220)
    btn_cadastrar.place(x=105, y=450)


def marcacao_checkbox(checkbox_marcada, outra_checkbox):

    if checkbox_marcada.get() == 1:
        outra_checkbox.set(0)


def voltar(app, cadastro_frame, img_label_voltar):

    cadastro_frame.place_forget()
    img_label_voltar.place_forget()
    tela_login.mostrar_tela_login(app, cadastro_frame)