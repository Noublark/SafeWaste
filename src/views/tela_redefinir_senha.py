from customtkinter import *
import tkinter
from PIL import Image, ImageTk
from . import tela_login
from src.controllers import usuario_controller

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
    
    global redefinir_senha_frame, campo_email, campo_senha, campo_senha2
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

    btn_redefinir_senha = CTkButton(redefinir_senha_frame, text="Redefinir", command= lambda: redefinir_senha(), corner_radius=10, fg_color= "#985698", hover_color="#ee82ee", width=220)
    btn_redefinir_senha.place(x=95, y=405)

    
def voltar(app, frame, img_label, img_label_voltar):

    frame.place_forget()
    img_label_voltar.place_forget()
    tela_login.mostrar_tela_login(app, frame, img_label)


def redefinir_senha():

    email = campo_email.get()
    nova_senha = campo_senha.get()
    nova_senha2 = campo_senha2.get()

    if email == "" or nova_senha == "" or nova_senha2 == "":
        label_erro = CTkLabel(redefinir_senha_frame, text="Erro: Preencha todos os campos", text_color="red")
        label_erro.place(x=115, y=445)
        redefinir_senha_frame.after(1500, label_erro.place_forget)
        return

    if nova_senha != nova_senha2:
        label_erro = CTkLabel(redefinir_senha_frame, text="Erro: Senhas diferentes", text_color="red")
        label_erro.place(x=140, y=445)
        redefinir_senha_frame.after(1500, label_erro.place_forget)
        return
    
    resultado = usuario_controller.redefinir_senha(email, nova_senha)
    
    if "Senha redefinida com sucesso!" in resultado:
        label_sucesso = CTkLabel(redefinir_senha_frame, text=resultado, text_color="green")
        label_sucesso.place(x=120, y=445)
        redefinir_senha_frame.after(2000, label_sucesso.place_forget)
        return
    else:
        label_erro = CTkLabel(redefinir_senha_frame, text=resultado, text_color="red")
        label_erro.place(x=130, y=445)
        redefinir_senha_frame.after(1500, label_erro.place_forget)



