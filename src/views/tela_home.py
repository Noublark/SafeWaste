from customtkinter import *

def mostrar_tela_home(app, login_frame):

    teste = TRUE

    global tela_home_frame
    
    if teste:
        
        login_frame.pack_forget()

        
        tela_home_frame = CTkFrame(master=app, fg_color="black", border_color="black")
        tela_home_frame.pack(fill=BOTH, expand=TRUE)
    
    else:

        login_frame.pack_forget()
        
        tela_home_frame = CTkFrame(master=app, fg_color="white", border_color="black")
        tela_home_frame.pack(fill=BOTH, expand=TRUE)


    
     
