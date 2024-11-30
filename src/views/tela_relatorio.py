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
        self.mensagens_temporarias = {} 

        self.img_voltar = self._carregar_imagem("src/resources/static/back arrow.png", (40, 50))
        self.img_ver = self._carregar_imagem("src/resources/static/olho.png", (30, 30))
        self.img_baixar = self._carregar_imagem("src/resources/static/download.png", (30, 30))

    def _carregar_imagem(self, caminho, tamanho): 
        return ImageTk.PhotoImage(Image.open(caminho).resize(tamanho, Image.LANCZOS))

    def esconder_todos_frames(self): # função para esconder todos os frames
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

            msg_label = CTkLabel(relatorios, text="", font=('Century Gothic', 12), text_color="green")
            msg_label.grid(row=i, column=2, padx=5, pady=55, sticky="w")
            self.mensagens_temporarias[nome] = msg_label

            img_ver = CTkLabel(relatorios_config, image=self.img_ver, text="", cursor="hand2")
            img_ver.bind("<Button-1>", lambda e, n=nome: self.ver_relatorio(n))
            img_ver.grid(row=i, column=0, padx=5, pady=55, sticky="nsew")

            img_baixar = CTkLabel(relatorios_config, image=self.img_baixar, text="", cursor="hand2")
            img_baixar.bind("<Button-1>", lambda e, n=nome: self._baixar_com_confirmacao(n))
            img_baixar.grid(row=i, column=1, padx=5, pady=55, sticky="nsew")

            for frame in (relatorios, relatorios_config):
                frame.grid_columnconfigure((0,1), weight=1)
                frame.grid_rowconfigure(i, weight=1)

    def ver_relatorio(self, nome_relatorio):
        self.esconder_todos_frames()
        
        self.tela_ver_relatorio_frame = CTkScrollableFrame(
            master=self.app,
            width=600, 
            height=500,
            corner_radius=15,
            fg_color="#080808"
        )
        self.tela_ver_relatorio_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        # Frame para o título
        titulo_frame = CTkFrame(
            self.tela_ver_relatorio_frame,
            fg_color="#985698",
            corner_radius=8
        )
        titulo_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        CTkLabel(
            titulo_frame, 
            text=f"Visualizar {nome_relatorio}",
            font=('Century Gothic', 32),
            text_color="white"
        ).pack(pady=10)

        # Frame para o conteúdo
        conteudo_frame = CTkFrame(
            self.tela_ver_relatorio_frame,
            fg_color="#1a1a1a",
            corner_radius=8
        )
        conteudo_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        conteudo = self.servicos_relatorio.obter_conteudo_relatorio(nome_relatorio)
        texto = self.relatorio.carregar_relatorio(conteudo)
        
        # Quebra o texto em linhas nos pontos e vírgulas
        texto_formatado = texto.replace(';', ';\n')
        
        CTkLabel(
            conteudo_frame,
            text=texto_formatado,
            font=('Century Gothic', 14),
            justify="left", 
            wraplength=550,
            fg_color="#1a1a1a",
            text_color="white"
        ).pack(padx=20, pady=20, expand=True, fill="both")

        # Configurar expansão da coluna
        self.tela_ver_relatorio_frame.grid_columnconfigure(0, weight=1)

        # Botão voltar
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

    def _baixar_com_confirmacao(self, nome_relatorio):
        nome_arquivo = self.relatorio.baixar_relatorio(nome_relatorio)
        msg_label = self.mensagens_temporarias.get(nome_relatorio)
        if msg_label:
            msg_label.configure(text=f"Salvo em {nome_arquivo}")
            self.app.after(2000, lambda: msg_label.configure(text=""))
