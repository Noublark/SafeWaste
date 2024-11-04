from customtkinter import *

def mostrar_tela_redefinir_senha(app, login_frame):
    
    login_frame.pack_forget()

    global redefinir_senha_frame
    redefinir_senha_frame = CTkFrame(master=app, fg_color="green", border_color="black")
    redefinir_senha_frame.pack(fill=BOTH, expand=TRUE)