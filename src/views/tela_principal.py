from customtkinter import *

def mostrar_tela_principal(app, login_frame):

    login_frame.pack_forget()

    global tela_principal_frame
    tela_principal_frame = CTkFrame(master=app, fg_color="black", border_color="black")
    tela_principal_frame.pack(fill=BOTH, expand=TRUE)
    
     
