from customtkinter import CTkFrame, CTkLabel
from PIL import Image, ImageTk
from src.models.grafico import Grafico
import tkinter as tk
import matplotlib.pyplot as plt 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class TelaGrafico:
    def __init__(self, app):
        self.app = app
        self.tela_grafico_frame = None
        self.img_label_voltar = None
        self.grafico = Grafico()
        self.tabela_frame = None
        self.img_label_voltar_tabela = None
        self.tela_grafico_frame_lateral = None
        self.img_label_tabela = None

    def esconder_todos_frames(self): # função para esconder todos os frames
        frames = [
            self.tela_grafico_frame,
            self.tabela_frame,
            self.tela_grafico_frame_lateral
        ]
        
        labels = [
            self.img_label_voltar,
            self.img_label_voltar_tabela,
            self.img_label_tabela
        ]
        
        for frame in frames:
            if frame:
                frame.destroy()
                
        for label in labels:
            if label:
                label.destroy()

    def mostrar_tela_grafico(self, frame):
        
        self.esconder_todos_frames()

        if frame:
            frame.destroy()

        self.tela_grafico_frame = CTkFrame(master=self.app, width=500, height=400, corner_radius=15, border_color="")
        self.tela_grafico_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.tela_grafico_frame_lateral = CTkFrame(master=self.app, width=65, height=300, corner_radius=10, fg_color="#985698", border_color="")
        self.tela_grafico_frame_lateral.place(relx=1.0, rely=0.5, anchor=tk.E)

        img_voltar = self.carregar_imagem("src/resources/static/back arrow.png", (40, 50))

        self.img_label_voltar = CTkLabel(self.app, image=img_voltar, text="", cursor="hand2")
        self.img_label_voltar.image = img_voltar
        self.img_label_voltar.bind("<Button-1>", lambda event: self.voltar())
        self.img_label_voltar.place(x=20, y=20)

        img_tabela = self.carregar_imagem("src/resources/static/tabela.png", (40, 40))
        self.img_label_tabela = CTkLabel(self.tela_grafico_frame_lateral, image=img_tabela, text="", fg_color="#985698", cursor="hand2")
        self.img_label_tabela._image = img_tabela
        self.img_label_tabela.bind("<Button-1>", lambda event: self.mostrar_tabela())
        self.img_label_tabela.place(x=12, y=120)

        self.mostrar_grafico(self.tela_grafico_frame)

    def mostrar_tabela(self):
        self.esconder_todos_frames()

        residuos_filtrados, colunas = self.grafico.exibir_dados_em_tabela()

        self.tabela_frame = CTkFrame(master=self.app, width=600, height=400, corner_radius=15, border_color="")
        self.tabela_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Canvas para rolagem bidirecional
        self.canvas = tk.Canvas(self.tabela_frame, width=580, height=380, bg="#080808")
        self.canvas.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        # Frame interno dentro da Canvas
        self.scrollable_frame = CTkFrame(self.canvas, bg_color="#080808", corner_radius=15, border_color="")
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        # Scrollbars
        horizontal_scrollbar = tk.Scrollbar(self.tabela_frame, orient="horizontal", command=self.canvas.xview)
        horizontal_scrollbar.grid(row=1, column=0, sticky="ew", padx=10)
        vertical_scrollbar = tk.Scrollbar(self.tabela_frame, orient="vertical", command=self.canvas.yview)
        vertical_scrollbar.grid(row=0, column=1, sticky="ns", pady=10)

        self.canvas.configure(xscrollcommand=horizontal_scrollbar.set, yscrollcommand=vertical_scrollbar.set)

        # Cabeçalhos da tabela
        for i, coluna in enumerate(colunas):
            header_label = CTkLabel(
                self.scrollable_frame, 
                text=coluna,
                width=80,
                height=25,
                fg_color="#985698",
                corner_radius=8,
                font=("Century Gothic", 11, "bold")
            )
            header_label.grid(row=0, column=i, padx=2, pady=2, sticky="nsew")

        # Dados da tabela
        for row_index, row in residuos_filtrados.iterrows():
            for col_index, item in enumerate(row):
                cell_label = CTkLabel(
                    self.scrollable_frame,
                    text=str(item),
                    width=80,
                    height=20,
                    fg_color="#1a1a1a",
                    corner_radius=4,
                    font=("Century Gothic", 10)
                )
                cell_label.grid(row=row_index + 1, column=col_index, padx=2, pady=1, sticky="nsew")

        # Configurar expansão das células
        for i in range(len(colunas)):
            self.scrollable_frame.grid_columnconfigure(i, weight=1)
        for i in range(len(residuos_filtrados) + 1):
            self.scrollable_frame.grid_rowconfigure(i, weight=1)

        # Atualiza o tamanho do scrollable_frame
        self.scrollable_frame.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

        # Botão voltar
        img_voltar_tabela = self.carregar_imagem("src/resources/static/back arrow.png", (40, 50))
        self.img_label_voltar_tabela = CTkLabel(self.app, image=img_voltar_tabela, text="", cursor="hand2")
        self.img_label_voltar_tabela.image = img_voltar_tabela
        self.img_label_voltar_tabela.bind("<Button-1>", lambda event: self.voltar_grafico())
        self.img_label_voltar_tabela.place(x=20, y=20)

    def voltar(self):
        from .tela_home import TelaHome
        self.esconder_todos_frames()
        TelaHome(self.app).mostrar_tela_home()

    def voltar_grafico(self):
        self.esconder_todos_frames()
        self.mostrar_tela_grafico(None)

    def carregar_imagem(self, caminho, tamanho):
        img = Image.open(caminho)
        img = img.resize(tamanho, Image.LANCZOS)
        return ImageTk.PhotoImage(img)

    def mostrar_grafico(self, tela_grafico_frame):
        dados_grafico = self.grafico.exibir_grafico()

        if dados_grafico is not None:
            # gerar o gráfico
            fig, ax = plt.subplots(figsize=(10, 6))
            fig.patch.set_facecolor('#080808')
            ax.set_facecolor('white')
            ax.bar(dados_grafico['anoGeracao'], dados_grafico['quantidadeGerada'], color='#985698')
            ax.set_xlabel('Ano de Geração', color='white', fontsize=6)
            ax.set_ylabel('Quantidade Gerada', color='white', fontsize=6)
            ax.set_title('Quantidade de Resíduos Perigosos Gerados por Ano', color='white', fontsize=12)
            ax.tick_params(axis='x', colors='white', rotation=45)
            ax.tick_params(axis='y', colors='white')

            # adicionar o gráfico ao canvas da tabela
            canvas = FigureCanvasTkAgg(fig, master=tela_grafico_frame)
            canvas.draw()
            canvas.get_tk_widget().place(relx=0.5, rely=0.5, anchor="center", width=475, height=375)