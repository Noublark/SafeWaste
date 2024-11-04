from tkinter import PhotoImage
from customtkinter import *
from . import tela_login


set_appearance_mode("Dark")
set_default_color_theme("src/resources/theme/DaynNight.json")

app = CTk()
app.title("SafeWaste")

largura, altura = 800, 600
pos_x = (app.winfo_screenwidth() - largura) // 2
pos_y = (app.winfo_screenheight() - altura) // 2
app.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")

def app_start():

    global frame_inicial
    frame_inicial = CTkFrame(master=app, fg_color="white", border_color="black")
    frame_inicial.pack(fill= BOTH, expand=TRUE)
    app.bind("<Button-1>", lambda event: tela_login.mostrar_tela_login(app, frame_inicial))

    img = PhotoImage(file="img_teste.png")
    label_img = CTkLabel(master=frame_inicial, image=img, text="")
    label_img.place(relx=0.5, rely=0.5, anchor=CENTER)

    app.mainloop()