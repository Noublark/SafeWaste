from PIL import Image, ImageTk
from customtkinter import CTk, CTkFrame, CTkLabel, set_appearance_mode, set_default_color_theme, BOTH, TRUE
from .tela_login import TelaLogin

class App:
    def __init__(self):
        set_appearance_mode("dark")
        set_default_color_theme("src/resources/theme/DaynNight.json")

        self.app = CTk()
        self.app.title("SafeWaste")

        self.app.iconbitmap("src/resources/static/icon.ico")

        # centraliza a janela na tela
        self.width = 800
        self.height = 600
        pos_x = (self.app.winfo_screenwidth() - self.width) // 2
        pos_y = (self.app.winfo_screenheight() - self.height) // 2
        self.app.geometry(f"{self.width}x{self.height}+{pos_x}+{pos_y}")

        self.frame_inicial = None
        self.tela_login = TelaLogin(self.app)

    def start(self):
        self.setup_frame_inicial()
        self.app.mainloop()

    def setup_frame_inicial(self):
       
        for widget in self.app.winfo_children():
            widget.destroy()

        self.frame_inicial = CTkFrame(master=self.app, fg_color="black", border_color="black")
        self.frame_inicial.pack(fill=BOTH, expand=TRUE)

        img = Image.open("src/resources/static/icon title.png")
        img = img.resize((250, 255), Image.LANCZOS)
        img_tk = ImageTk.PhotoImage(img)

        self.img_label = CTkLabel(self.frame_inicial, image=img_tk, text="")
        self.img_label.image = img_tk 
        self.img_label.image = img_tk
        self.img_label.place(relx=0.5, rely=0.5, anchor="center")

        self.app.bind("<Button-1>", lambda event: self.mostrar_tela_login(event))

    def mostrar_tela_login(self, event):
        self.frame_inicial.place_forget()
        self.img_label.place_forget()
        self.tela_login.mostrar_tela_login()
