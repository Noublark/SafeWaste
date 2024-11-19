from PIL import Image, ImageTk
from customtkinter import CTk, CTkFrame, CTkLabel, set_appearance_mode, set_default_color_theme, BOTH, TRUE
from .tela_login import TelaLogin

class App:
    def __init__(self):
        set_appearance_mode("dark")
        set_default_color_theme("src/resources/theme/DaynNight.json")

        self.app = CTk()
        self.app.title("SafeWaste")

        icon_image = ImageTk.PhotoImage(file="src/resources/static/icon.png")
        self.app.iconphoto(True, icon_image)

        # Centraliza a janela na tela
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
        # Limpa widgets existentes
        for widget in self.app.winfo_children():
            widget.destroy()

        # Configura frame inicial
        self.frame_inicial = CTkFrame(master=self.app, fg_color="black", border_color="black")
        self.frame_inicial.pack(fill=BOTH, expand=TRUE)

        # Carrega e exibe imagem
        img = Image.open("src/resources/static/icon title.png")
        img = img.resize((250, 255), Image.LANCZOS)
        img_tk = ImageTk.PhotoImage(img)

        img_label = CTkLabel(self.frame_inicial, image=img_tk, text="")
        img_label.image = img_tk  # Mantém uma referência forte para a imagem
        img_label.image = img_tk
        img_label.place(relx=0.5, rely=0.5, anchor="center")

        # Configura evento de clique
        self.app.bind("<Button-1>", lambda event: self.mostrar_tela_login(event, img_label))

    def mostrar_tela_login(self, event, img_label):
        self.tela_login.mostrar_tela_login(self.frame_inicial, img_label)
