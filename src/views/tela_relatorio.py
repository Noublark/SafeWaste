from customtkinter import *
from PIL import Image, ImageTk
from src.services.servicos_relatorio import ServicosRelatorio  # Importa o serviço de relatórios para interagir com o banco de dados
from src.models.relatorio import Relatorio

class TelaRelatorio:
    def __init__(self, app):
        self.app = app
        self.tela_relatorio_frame = None
        self.img_label_voltar = None
        self.tela_ver_relatorio_frame = None
        self.img_label_voltar_ver_relatorio = None
        self.servicos_relatorio = ServicosRelatorio()  # Instancia o serviço para conexão com o banco de dados
        self.relatorio = Relatorio()

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

        # Usando CTkScrollableFrame para permitir rolagem
        self.tela_relatorio_frame = CTkScrollableFrame(master=self.app, width=500, height=400, corner_radius=15, border_color="")
        self.tela_relatorio_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.img_label_voltar = CTkLabel(self.app, image=self.img_voltar, text="", cursor="hand2")
        self.img_label_voltar.bind("<Button-1>", lambda event: self.voltar(frame, frame2))
        self.img_label_voltar.place(x=20, y=20)

        titulo = CTkLabel(self.tela_relatorio_frame, text="Relatórios", font=('Century Ghotic', 32))
        #titulo.place(x=200, y=25)
        titulo.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="n")

        # Relatórios ocupando 70% da largura e configurações 30%
        relatorios = CTkFrame(self.tela_relatorio_frame, width=0, corner_radius=8, fg_color="#080808", border_color="")
        relatorios.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        relatorios_config = CTkFrame(self.tela_relatorio_frame, width=0, corner_radius=8, fg_color="#985698", border_color="")
        relatorios_config.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

        # Usando grid_columnconfigure para distribuir a largura de forma proporcional
        self.tela_relatorio_frame.grid_columnconfigure(0, weight=8)  # 70% para relatórios
        self.tela_relatorio_frame.grid_columnconfigure(1, weight=2)  # 30% para configurações

        # Carrega os nomes dos relatórios do banco de dados
        nomes_relatórios = self.servicos_relatorio.obter_nomes_relatorios()
        self.adicionar_labels_e_imagens(relatorios, relatorios_config, nomes_relatórios)

    def adicionar_labels_e_imagens(self, relatorios, relatorios_config, nomes_relatórios):
        espacamento_y = 55

        for i, nome in enumerate(nomes_relatórios):
            
            label = CTkLabel(relatorios, text=nome, font=('Century Gothic', 16))
            label.grid(row=i, column=0, padx=5, pady=espacamento_y, sticky="w", columnspan=2)

            # Imagem de visualização
            img_label_ver = CTkLabel(relatorios_config, image=self.img_ver, text="", cursor="hand2")
            img_label_ver.bind("<Button-1>", lambda event, nome=nome: self.ver_relatorio(nome))  # Chama a função de visualização
            img_label_ver.grid(row=i, column=0, padx=5, pady=espacamento_y, sticky="nsew", columnspan=1)

            # Imagem para baixar o relatório
            img_label_baixar = CTkLabel(relatorios_config, image=self.img_baixar, text="", cursor="hand2")
            img_label_baixar.bind("<Button-1>", lambda event, nome=nome: self.relatorio.baixar_relatorio(nome))  # Chama a função de download
            img_label_baixar.grid(row=i, column=1, padx=5, pady=espacamento_y, sticky="nsew", columnspan=1)

            # Ajusta as colunas para que elas se expandam igualmente
            relatorios_config.grid_columnconfigure(0, weight=1)
            relatorios_config.grid_columnconfigure(1, weight=1)

            relatorios.grid_rowconfigure(i, weight=1)
            relatorios_config.grid_rowconfigure(i, weight=1)
        
        relatorios.grid_rowconfigure(i, weight=1)
        relatorios_config.grid_rowconfigure(i, weight=1)

    def ver_relatorio(self, nome_relatorio):
        
        # Frame scrollable único para mostrar o conteúdo do relatório
        self.tela_ver_relatorio_frame = CTkScrollableFrame(master=self.app, width=500, height=400, corner_radius=15, fg_color="#080808", border_color="")
        self.tela_ver_relatorio_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        # Título dentro do frame scrollable, na primeira linha, centralizado
        titulo1 = CTkLabel(self.tela_ver_relatorio_frame, text=f"Visualizar {nome_relatorio}", font=('Century Ghotic', 32))
        titulo1.place(relx=0.5, rely=0.2, anchor=CENTER)  # Título centralizado e ocupa 3 colunas

        # Carrega o conteúdo do relatório específico do banco de dados
        conteudo_relatorio = self.servicos_relatorio.obter_conteudo_relatorio(nome_relatorio)
        conteudo_relatorio_str = self.relatorio.carregar_relatorio(conteudo_relatorio)
        texto_label = CTkLabel(self.tela_ver_relatorio_frame, text=conteudo_relatorio_str, font=('Century Gothic', 14), justify="left", fg_color="#080808")
        
        # Conteúdo do relatório na segunda linha
        texto_label.grid(row=1, column=0, padx=10, pady=80, sticky="w")  # Conteúdo abaixo do título

        # Botão de voltar para a tela de relatórios (fora do grid, no canto superior esquerdo)
        self.img_label_voltar_ver_relatorio = CTkLabel(self.app, image=self.img_voltar, text="", cursor="hand2")
        self.img_label_voltar_ver_relatorio.bind("<Button-1>", lambda event: self.voltar_relatorio())
        self.img_label_voltar_ver_relatorio.place(x=20, y=20)

    def voltar(self, frame_anterior, img_label_anterior):
        from .tela_home import TelaHome
        self.tela_relatorio_frame.place_forget()
        self.img_label_voltar.place_forget()
        TelaHome(self.app).mostrar_tela_home(frame_anterior, img_label_anterior)

    def voltar_relatorio(self):
        if self.img_label_voltar_ver_relatorio:
            self.tela_ver_relatorio_frame.place_forget()
            self.img_label_voltar_ver_relatorio.place_forget()
        self.mostrar_tela_relatorio(self.tela_relatorio_frame, self.img_label_voltar)
