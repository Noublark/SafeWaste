from customtkinter import *
from . import tela_cadastro, tela_redefinir_senha, tela_principal
from PIL import Image, ImageTk

def mostrar_tela_login(app, frame_inicial):
    app.unbind("<Button-1>")
    frame_inicial.pack_forget()

    global login_frame
    login_frame = CTkFrame(master=app, fg_color="black", border_color="black")
    login_frame.pack(fill=BOTH, expand=TRUE)

    img = Image.open("img_teste.png")
    img = img.resize((220, 200), Image.LANCZOS) 
    img_tk = ImageTk.PhotoImage(img)

    img_label = CTkLabel(login_frame, image=img_tk, fg_color="black", text="")
    img_label.image = img_tk
    img_label.place(relx=0.5, rely=0.25, anchor="center")

    titulo = CTkLabel(login_frame, text="Faça Login", font=("Verdana", 32))
    titulo.place(relx=0.5, rely=0.47, anchor="center")

    campo_email = CTkEntry(login_frame, placeholder_text="Digite seu email", width=200, corner_radius=15)
    campo_email.place(relx=0.5, rely=0.57, anchor="center") 

    campo_senha = CTkEntry(login_frame, placeholder_text="Digite sua senha", width=200, show="*", corner_radius=15)
    campo_senha.place(relx=0.5, rely=0.65, anchor="center")

    buttons_frame = CTkFrame(login_frame, fg_color="black", border_color="black", border_width=0)
    buttons_frame.place(relx=0.5, rely=0.75, anchor="center")

    btn_cadastro = CTkButton(master=buttons_frame, text="Cadastrar", command=lambda: tela_cadastro.mostrar_tela_cadastro(app, login_frame), corner_radius=15, fg_color= "transparent", border_color="white", border_width=1)
    btn_cadastro.pack(side=LEFT, padx=5)

    btn_login = CTkButton(master=buttons_frame, text="Entrar", command=lambda: tela_principal.mostrar_tela_principal(app, login_frame), corner_radius=15, fg_color= "#985698", hover_color="#ee82ee")
    btn_login.pack(side=LEFT, padx=5)

    hyperlink_redefinir_senha = CTkLabel(
        login_frame,
        text="Esqueceu a senha?",
        text_color="#0000EE",
        cursor="hand2"
    )
    hyperlink_redefinir_senha.bind("<Button-1>", lambda event: tela_redefinir_senha.mostrar_tela_redefinir_senha(app, login_frame))
    hyperlink_redefinir_senha.place(relx=0.5, rely=0.85, anchor="center")

