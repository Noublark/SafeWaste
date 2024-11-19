from customtkinter import *
from PIL import Image, ImageTk
from src.services.servicos_relatorio import ServicosRelatorio
from src.models.relatorio import Relatorio

class TelaRelatorio:
    def __init__(self, app):
        self.app = app
        self.tela_relatorio_frame = None
        self.img_label_voltar = None
        self.tela_ver_relatorio_frame = None
        self.servicos_relatorio = ServicosRelatorio()
        self.relatorio = Relatorio()

        # Carrega imagens uma única vez
        self.img_voltar = self._carregar_imagem("src/resources/static/back arrow.png", (40, 50))
        self.img_ver = self._carregar_imagem("src/resources/static/olho.png", (30, 30))
        self.img_baixar = self._carregar_imagem("src/resources/static/download.png", (30, 30))

    def _carregar_imagem(self, caminho, tamanho):
        return ImageTk.PhotoImage(Image.open(caminho).resize(tamanho, Image.LANCZOS))

    def esconder_todos_frames(self):
        frames = [
            self.tela_relatorio_frame,
            self.tela_ver_relatorio_frame
        ]
        
        labels = [
            self.img_label_voltar
        ]
        
        for frame in frames:
            if frame:
                frame.destroy()
                
        for label in labels:
            if label:
                label.destroy()

    def mostrar_tela_relatorio(self, frame):
        self.esconder_todos_frames()

        if frame:
            frame.destroy()
            frame = None

        self.tela_relatorio_frame = CTkScrollableFrame(
            master=self.app, 
            width=500, 
            height=400, 
            corner_radius=15,
            border_color=""
        )
        self.tela_relatorio_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.img_label_voltar = CTkLabel(self.app, image=self.img_voltar, text="", cursor="hand2")
        self.img_label_voltar.bind("<Button-1>", lambda event: self.voltar())
        self.img_label_voltar.place(x=20, y=20)

        titulo = CTkLabel(self.tela_relatorio_frame, text="Relatórios", font=('Century Ghotic', 32))
        titulo.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="n")

        relatorios = CTkFrame(self.tela_relatorio_frame, corner_radius=8, fg_color="#080808", border_color="")
        relatorios.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        relatorios_config = CTkFrame(self.tela_relatorio_frame, corner_radius=8, fg_color="#985698", border_color="")
        relatorios_config.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

        self.tela_relatorio_frame.grid_columnconfigure(0, weight=8)
        self.tela_relatorio_frame.grid_columnconfigure(1, weight=2)

        nomes_relatórios = self.servicos_relatorio.obter_nomes_relatorios()
        self._adicionar_labels_e_imagens(relatorios, relatorios_config, nomes_relatórios)

    def _adicionar_labels_e_imagens(self, relatorios, relatorios_config, nomes_relatórios):
        for i, nome in enumerate(nomes_relatórios):
            CTkLabel(relatorios, text=nome, font=('Century Gothic', 16)).grid(
                row=i, column=0, padx=5, pady=55, sticky="w", columnspan=2
            )

            img_ver = CTkLabel(relatorios_config, image=self.img_ver, text="", cursor="hand2")
            img_ver.bind("<Button-1>", lambda e, n=nome: self.ver_relatorio(n))
            img_ver.grid(row=i, column=0, padx=5, pady=55, sticky="nsew")

            img_baixar = CTkLabel(relatorios_config, image=self.img_baixar, text="", cursor="hand2")
            img_baixar.bind("<Button-1>", lambda e, n=nome: self.relatorio.baixar_relatorio(n))
            img_baixar.grid(row=i, column=1, padx=5, pady=55, sticky="nsew")

            for frame in (relatorios, relatorios_config):
                frame.grid_columnconfigure((0,1), weight=1)
                frame.grid_rowconfigure(i, weight=1)

    def ver_relatorio(self, nome_relatorio):
        self.esconder_todos_frames()
        
        self.tela_ver_relatorio_frame = CTkScrollableFrame(
            master=self.app,
            width=500, 
            height=400,
            corner_radius=15,
            fg_color="#080808"
        )
        self.tela_ver_relatorio_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        CTkLabel(
            self.tela_ver_relatorio_frame, 
            text=f"Visualizar {nome_relatorio}",
            font=('Century Ghotic', 32)
        ).place(relx=0.5, rely=0.2, anchor=CENTER)

        conteudo = self.servicos_relatorio.obter_conteudo_relatorio(nome_relatorio)
        texto = self.relatorio.carregar_relatorio(conteudo)
        
        CTkLabel(
            self.tela_ver_relatorio_frame,
            text=texto,
            font=('Century Gothic', 14),
            justify="left",
            fg_color="#080808"
        ).grid(row=1, column=0, padx=10, pady=80, sticky="w")

        self.img_label_voltar = CTkLabel(self.app, image=self.img_voltar, text="", cursor="hand2")
        self.img_label_voltar.bind("<Button-1>", lambda e: self.voltar_relatorio())
        self.img_label_voltar.place(x=20, y=20)

    def voltar(self):
        from .tela_home import TelaHome
        self.tela_relatorio_frame.place_forget()
        self.esconder_todos_frames()
        TelaHome(self.app).mostrar_tela_home()

    def voltar_relatorio(self):
        if self.img_label_voltar:
            self.tela_relatorio_frame.place_forget()
            self.tela_ver_relatorio_frame.place_forget()
            self.img_label_voltar.place_forget()
        self.mostrar_tela_relatorio(None)
