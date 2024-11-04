from customtkinter import *
from . import app

def mostrar_tela_cadastro(app, login_frame):
    
    login_frame.pack_forget()

    global cadastro_frame
    cadastro_frame = CTkFrame(master=app, fg_color="blue", border_color="black")
    cadastro_frame.pack(fill=BOTH, expand=TRUE)