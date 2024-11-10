from PIL import Image, ImageTk
from customtkinter import *
from .tela_login import TelaLogin


class App:
    
    def __init__(self):
        set_appearance_mode("dark")
        set_default_color_theme("src/resources/theme/DaynNight.json")

        self.app = CTk()
        self.app.title("SafeWaste")

        self.width, self.height = 800, 600
        self.pos_x = (self.app.winfo_screenwidth() - self.width) // 2
        self.pos_y = (self.app.winfo_screenheight() - self.height) // 2
        self.app.geometry(f"{self.width}x{self.height}+{self.pos_x}+{self.pos_y}")

        self.frame_inicial = None
        self.img_label = None
        self.img_tk = None
        self.tela_login = TelaLogin(self.app)

    def start(self):

        self.setup_frame_inicial()  # Configura o frame inicial
        self.app.mainloop()

    def setup_frame_inicial(self):
        # Limpa todos os widgets na janela antes de configurar o novo frame
        for widget in self.app.winfo_children():
            widget.destroy()

        # Cria o frame inicial
        self.frame_inicial = CTkFrame(master=self.app, fg_color="black", border_color="black")
        self.frame_inicial.pack(fill=BOTH, expand=TRUE)

        # Carrega e configura a imagem dentro do contexto da janela principal
        img_path = "img_teste.png"
        img = Image.open(img_path)
        img = img.resize((320, 300), Image.LANCZOS)
        self.img_tk = ImageTk.PhotoImage(img)   # A imagem é agora um atributo da classe

        # Exibe a imagem na tela inicial
        self.img_label = CTkLabel(self.frame_inicial, image=self.img_tk, text="")
        self.img_label.image = self.img_tk  # Mantém a referência da imagem no atributo da classe
        self.img_label.place(relx=0.5, rely=0.5, anchor="center")

        # Configura evento de clique para chamar tela_login
        self.app.bind("<Button-1>", self.mostrar_tela_login)

    def mostrar_tela_login(self, event):
        self.tela_login.mostrar_tela_login(self.frame_inicial, self.img_label)
