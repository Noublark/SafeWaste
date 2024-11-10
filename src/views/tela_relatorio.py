from customtkinter import *
from PIL import Image, ImageTk

class TelaRelatorio:
    def __init__(self, app):
        self.app = app
        self.tela_relatorio_frame = None
        self.img_label_voltar = None
        self.tela_ver_relatorio_frame = None
        self.img_label_voltar_ver_relatorio = None
        # Imagens otimizadas
        self.img_voltar = self.carregar_imagem("src/resources/static/back arrow.png", (40, 50))
        self.img_ver = self.carregar_imagem("src/resources/static/olho.png", (30, 30))
        self.img_baixar = self.carregar_imagem("src/resources/static/download.png", (30, 30))

    def carregar_imagem(self, caminho, tamanho):
        img = Image.open(caminho)
        img = img.resize(tamanho, Image.LANCZOS)
        return ImageTk.PhotoImage(img)

    def mostrar_tela_relatorio(self, frame, frame2):
        frame.place_forget()
        frame2.place_forget()

        self.tela_relatorio_frame = CTkFrame(master=self.app, width=500, height=400, corner_radius=15, border_color="")
        self.tela_relatorio_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.img_label_voltar = CTkLabel(self.app, image=self.img_voltar, text="", cursor="hand2")
        self.img_label_voltar.bind("<Button-1>", lambda event: self.voltar(frame, frame2))
        self.img_label_voltar.place(x=20, y=20)

        titulo = CTkLabel(self.tela_relatorio_frame, text="Relatórios", font=('Century Ghotic', 32))
        titulo.place(x=200, y=25)

        relatorios = CTkFrame(self.tela_relatorio_frame, width=300, height=300, corner_radius=8, fg_color="#080808")
        relatorios.place(x=25, y=80)

        relatorios_config = CTkFrame(self.tela_relatorio_frame, width=150, height=300, corner_radius=8, fg_color="#985698")
        relatorios_config.place(x=325, y=80)

        self.adicionar_labels_e_imagens(relatorios, relatorios_config, quantidade=3)

    def adicionar_labels_e_imagens(self, relatorios, relatorios_config, quantidade):
        y_inicial = 10
        espacamento_y = 60

        for i in range(quantidade):
            label = CTkLabel(relatorios, text="teste", font=('Century Gothic', 16))
            label.place(x=10, y=y_inicial + i * espacamento_y)

            img_label_ver = CTkLabel(relatorios_config, image=self.img_ver, text="", cursor="hand2")
            img_label_ver.bind("<Button-1>", lambda event: self.ver_relatorio())
            img_label_ver.place(x=35, y=y_inicial + i * espacamento_y)

            img_label_baixar = CTkLabel(relatorios_config, image=self.img_baixar, text="", cursor="hand2")
            img_label_baixar.place(x=95, y=y_inicial + i * espacamento_y)

    def ver_relatorio(self):
        self.tela_ver_relatorio_frame = CTkFrame(master=self.app, width=500, height=400, corner_radius=15, border_color="")
        self.tela_ver_relatorio_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        titulo = CTkLabel(self.tela_ver_relatorio_frame, text="Visualizar Relatório", font=('Century Ghotic', 32))
        titulo.place(x=150, y=25)

        relatorio_texto = CTkLabel(self.tela_ver_relatorio_frame, text="Conteúdo do Relatório", font=('Century Gothic', 16))
        relatorio_texto.place(x=150, y=100)

        # Inicializa o botão "voltar" apenas quando a tela de relatório for visualizada
        self.img_label_voltar_ver_relatorio = CTkLabel(self.app, image=self.img_voltar, text="", cursor="hand2")
        self.img_label_voltar_ver_relatorio.bind("<Button-1>", lambda event: self.voltar_relatorio())
        self.img_label_voltar_ver_relatorio.place(x=20, y=20)

    def voltar(self, frame_anterior, img_label_anterior):
        from .tela_home import TelaHome
        self.tela_relatorio_frame.place_forget()
        self.img_label_voltar.place_forget()
        TelaHome(self.app).mostrar_tela_home(frame_anterior, img_label_anterior)

    def voltar_relatorio(self):
        # Verifica se a variável foi inicializada antes de tentar usá-la
        if self.img_label_voltar_ver_relatorio:
            self.tela_ver_relatorio_frame.place_forget()
            self.img_label_voltar_ver_relatorio.place_forget()
        self.mostrar_tela_relatorio(self.tela_relatorio_frame, self.img_label_voltar)
