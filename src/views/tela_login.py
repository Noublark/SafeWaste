from customtkinter import *
import tkinter
from . import tela_cadastro, tela_redefinir_senha, tela_principal
from PIL import Image, ImageTk

def mostrar_tela_login(app, frame_inicial):
    app.unbind("<Button-1>")
    frame_inicial.pack_forget()

    global login_frame
    login_frame = CTkFrame(master=app, width=436, height=500, corner_radius=15, border_color="")
    login_frame.place(relx=0.5, rely= 0.5, anchor=tkinter.CENTER)

    img = Image.open("img_teste.png")
    img = img.resize((220, 200), Image.LANCZOS) 
    img_tk = ImageTk.PhotoImage(img)

    img_label = CTkLabel(login_frame, image=img_tk, text="")
    img_label.image = img_tk
    img_label.place(x= 103, y= 5)

    titulo = CTkLabel(login_frame, text="Faça Login", font=('Century Ghotic', 32))
    titulo.place(x=140, y=205)

    campo_email = CTkEntry(login_frame, placeholder_text="Digite seu email", width=330, corner_radius=10)
    campo_email.place(x=50, y=275)

    campo_senha = CTkEntry(login_frame, placeholder_text="Digite sua senha", width=330, show="*", corner_radius=10)
    campo_senha.place(x=50, y=330)

    hyperlink_redefinir_senha = CTkLabel(login_frame, text="Esqueceu a senha?", text_color="lightblue", cursor="hand2")
    hyperlink_redefinir_senha.bind("<Button-1>", lambda event: tela_redefinir_senha.mostrar_tela_redefinir_senha(app, login_frame))
    hyperlink_redefinir_senha.place(x=260, y=360)

    btn_login = CTkButton(master=login_frame, text="Entrar", command=lambda: tela_principal.mostrar_tela_principal(app, login_frame), corner_radius=10, fg_color= "#985698", hover_color="#ee82ee", width=330)
    btn_login.place(x=50, y=410)

    label = CTkLabel(login_frame, text="Não tem uma conta?", font=('Century Ghotic', 12))
    label.place(x=50, y=450)

    hyperlink_cadastro = CTkLabel(login_frame, text="Cadastre-se", text_color="lightblue", cursor="hand2")
    hyperlink_cadastro.bind("<Button-1>", lambda event: tela_cadastro.mostrar_tela_cadastro(app, login_frame))
    hyperlink_cadastro.place(x=170, y=450)
    

    

