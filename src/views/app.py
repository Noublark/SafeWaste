from PIL import Image, ImageTk
from customtkinter import *
from . import tela_login


set_appearance_mode("White")
set_default_color_theme("src/resources/theme/DaynNight.json")


app = CTk()
app.title("SafeWaste")

largura, altura = 800, 600
pos_x = (app.winfo_screenwidth() - largura) // 2
pos_y = (app.winfo_screenheight() - altura) // 2
app.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")

def app_start():

    global frame_inicial
    frame_inicial = CTkFrame(master=app, fg_color="black", border_color="black")
    frame_inicial.pack(fill= BOTH, expand=TRUE)
    app.bind("<Button-1>", lambda event: tela_login.mostrar_tela_login(app, frame_inicial))

    img = Image.open("img_teste.png")
    img = img.resize((320, 300), Image.LANCZOS) 
    img_tk = ImageTk.PhotoImage(img)

    img_label = CTkLabel(frame_inicial, image=img_tk, text="")
    img_label.image = img_tk
    img_label.place(relx=0.5, rely=0.4, anchor="center")

    msg = CTkLabel(frame_inicial, text="Clique em qualquer lugar.", font=("Arial", 24), text_color="#B0B0B0")
    msg.place(relx=0.5, rely=0.7, anchor="center")

    app.mainloop()