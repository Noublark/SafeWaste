from customtkinter import *
from . import app, tela_cadastro, tela_redefinir_senha


def mostrar_tela_login(app, frame_inicial):
    
    app.unbind("<Button-1>")

    frame_inicial.pack_forget()

    global login_frame
    login_frame = CTkFrame(master=app, fg_color="red", border_color="black")
    login_frame.pack(fill=BOTH, expand=TRUE)

    btn = CTkButton(master=app, text="teste", command=lambda: tela_cadastro.mostrar_tela_cadastro(app, login_frame))
    btn.place(relx=0.5, rely=0.5, anchor = "center")
    
    btn1 = CTkButton(master=app, text="teste1", command=lambda: tela_redefinir_senha.mostrar_tela_redefinir_senha(app, login_frame))
    btn1.place(relx=0.5, rely=0.6, anchor = "center")
