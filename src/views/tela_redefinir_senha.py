from customtkinter import *
import tkinter
from PIL import Image, ImageTk
from . import tela_login

def mostrar_tela_redefinir_senha(app, frame, img_label):
    
    frame.place_forget()
    img_label.place_forget() 

    img_voltar = Image.open("src/resources/static/back arrow.png")
    img_voltar = img_voltar.resize((40, 50), Image.LANCZOS)
    img_tk = ImageTk.PhotoImage(img_voltar)

    img_label_voltar = CTkLabel(app, image=img_tk, text="", cursor="hand2")
    img_label_voltar.image = img_tk
    img_label_voltar.bind("<Button-1>", lambda event: voltar(app, redefinir_senha_frame, img_label, img_label_voltar))
    img_label_voltar.place(x=20, y=20)
    
    global redefinir_senha_frame
    redefinir_senha_frame = CTkFrame(master=app, width=400, height=605, corner_radius=15, border_color="")
    redefinir_senha_frame.place(relx=1.0, rely= 0.5, anchor=tkinter.E)

    img = Image.open("img_teste.png")
    img = img.resize((220, 200), Image.LANCZOS) 
    img_tk = ImageTk.PhotoImage(img)

    img_label = CTkLabel(app, image=img_tk, text="")
    img_label.image = img_tk
    img_label.place(relx=0.12, rely=0.5, anchor=tkinter.W) 

    titulo = CTkLabel(redefinir_senha_frame, text="Redefinir Senha", font=('Century Ghotic', 32))
    titulo.place(x=100, y=150)

    campo_email = CTkEntry(redefinir_senha_frame, placeholder_text="Digite seu email", width=330, corner_radius=10)
    campo_email.place(x=40, y=235)

    campo_senha = CTkEntry(redefinir_senha_frame, placeholder_text="Digite sua senha", width=330, show="*", corner_radius=10)
    campo_senha.place(x=40, y=290)

    campo_senha2 = CTkEntry(redefinir_senha_frame, placeholder_text="Digite sua senha novamente", width=330, show="*", corner_radius=10)
    campo_senha2.place(x=40, y=345)

    btn_redefinir_senha = CTkButton(redefinir_senha_frame, text="Redefinir", command= lambda: print("testando"), corner_radius=10, fg_color= "#985698", hover_color="#ee82ee", width=220)
    btn_redefinir_senha.place(x=95, y=405)

    
def voltar(app, frame, img_label, img_label_voltar):

    frame.place_forget()
    img_label_voltar.place_forget()
    tela_login.mostrar_tela_login(app, frame, img_label)

