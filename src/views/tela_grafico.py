from customtkinter import CTkFrame, CTkLabel, CTkButton
from PIL import Image, ImageTk
import tkinter as tk
import matplotlib.pyplot as plt 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import subprocess


class TelaGrafico:
    def __init__(self, app):
        self.app = app
        self.tela_grafico_frame = None
        self.img_label_voltar = None

    def esconder_todos_frames(self): # função para esconder todos os frames
        frames = [
            self.tela_grafico_frame,
        ]
        
        labels = [
            self.img_label_voltar,
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

        img_voltar = self.carregar_imagem("src/resources/static/back arrow.png", (40, 50))

        self.img_label_voltar = CTkLabel(self.app, image=img_voltar, text="", cursor="hand2")
        self.img_label_voltar.image = img_voltar
        self.img_label_voltar.bind("<Button-1>", lambda event: self.voltar())
        self.img_label_voltar.place(x=20, y=20)

        img_icon = self.carregar_imagem("src/resources/static/icon.png", (130, 120))
        self.img_label_icon = CTkLabel(self.tela_grafico_frame, image=img_icon, text="")
        self.img_label_icon._image = img_icon
        self.img_label_icon.place(relx=0.52, rely=0.45, anchor=tk.CENTER)

        self.botao_streamlit = CTkButton(self.tela_grafico_frame, text="Abrir Dashboard", command=self.executar_streamlit, corner_radius=10, fg_color="#985698", hover_color="#a66da6", width=125)
        self.botao_streamlit.place(relx=0.5, rely=0.70, anchor=tk.CENTER)

    def voltar(self):
        from .tela_home import TelaHome
        self.esconder_todos_frames()
        TelaHome(self.app).mostrar_tela_home()

    def carregar_imagem(self, caminho, tamanho):
        img = Image.open(caminho)
        img = img.resize(tamanho, Image.LANCZOS)
        return ImageTk.PhotoImage(img)

    def executar_streamlit(self):
        subprocess.Popen(["python", "-m", "streamlit", "run", "app_streamlit.py"])
