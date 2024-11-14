from customtkinter import *
from PIL import Image, ImageTk
import tkinter
import re
from datetime import datetime
from src.models.coleta import Coleta


class TelaColeta:
    def __init__(self, app):
        self.app = app
        self.tela_coleta_frame = None
        self.img_label_voltar = None
        self.img_label_adicionar = None

    def mostrar_tela_coleta(self, frame, frame2, img_label_sair):
        # Esconde os frames anteriores
        frame.place_forget()
        frame2.place_forget()
        img_label_sair.place_forget()

        # Criação do frame da tela de coleta
        self.tela_coleta_frame = CTkFrame(master=self.app, width=500, height=400, corner_radius=15, border_color="")
        self.tela_coleta_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        # Carregar e ajustar a imagem do botão "voltar"
        img_voltar = Image.open("src/resources/static/back arrow.png")
        img_voltar = img_voltar.resize((40, 50), Image.LANCZOS)
        img_tk = ImageTk.PhotoImage(img_voltar)

        # Criação do botão "voltar"
        self.img_label_voltar = CTkLabel(self.app, image=img_tk, text="", cursor="hand2")
        self.img_label_voltar.image = img_tk
        self.img_label_voltar.bind("<Button-1>", lambda event: self.voltar(frame, frame2))
        self.img_label_voltar.place(x=20, y=20)

        img_adicionar = Image.open("src/resources/static/adicionar.png")
        img_adicionar = img_adicionar.resize((25,25), Image.LANCZOS)
        img_tk1 = ImageTk.PhotoImage(img_adicionar)

        self.img_label_adicionar = CTkLabel(self.tela_coleta_frame, image=img_tk1, text="", cursor="hand2")
        self.img_label_adicionar.bind("<Button-1>", lambda event: self.tela_agendar(self.tela_coleta_frame, self.img_label_voltar))
        self.img_label_adicionar.place(x=460, y=30)

        # Título da tela de coleta
        titulo = CTkLabel(self.tela_coleta_frame, text="Coletas", font=('Century Ghotic', 32))
        titulo.place(x=200, y=25)

        # Frames para coletas e configurações
        coletas = CTkFrame(self.tela_coleta_frame, width=300, height=300, corner_radius=8, fg_color="#080808", border_color="")
        coletas.place(x=25, y=80)

        coletas_config = CTkFrame(self.tela_coleta_frame, width=150, height=300, corner_radius=8, fg_color="#985698", border_color="")
        coletas_config.place(x=325, y=80)

        # Adiciona labels e imagens
        self.adicionar_labels_e_imagens(coletas, coletas_config, quantidade=3)

    def adicionar_labels_e_imagens(self, coletas, coletas_config, quantidade):
        y_inicial = 10
        espacamento_y = 60

        for i in range(quantidade):
            # Criação de labels e imagens de coleta
            label = CTkLabel(coletas, text="teste", font=('Century Gothic', 16))
            label.place(x=10, y=y_inicial + i * espacamento_y)

            # Imagem de concluído
            img_concluido = Image.open("src/resources/static/concluido.png").resize((30, 30), Image.LANCZOS)
            img_tk1 = ImageTk.PhotoImage(img_concluido)
            img_label_concluido = CTkLabel(coletas_config, image=img_tk1, text="", cursor="hand2")
            img_label_concluido.image = img_tk1
            img_label_concluido.place(x=13, y=y_inicial + i * espacamento_y)

            # Imagem de editar
            img_editar = Image.open("src/resources/static/lapis.png").resize((30, 30), Image.LANCZOS)
            img_tk2 = ImageTk.PhotoImage(img_editar)
            img_label_editar = CTkLabel(coletas_config, image=img_tk2, text="", cursor="hand2")
            img_label_editar.image = img_tk2
            img_label_editar.place(x=63, y=y_inicial + i * espacamento_y)

            # Imagem de remover
            img_remover = Image.open("src/resources/static/lixeira.png").resize((30, 30), Image.LANCZOS)
            img_tk3 = ImageTk.PhotoImage(img_remover)
            img_label_remover = CTkLabel(coletas_config, image=img_tk3, text="", cursor="hand2")
            img_label_remover.image = img_tk3
            img_label_remover.place(x=113, y=y_inicial + i * espacamento_y)

    def voltar(self, frame_anterior, img_label_anterior):
        from .tela_home import TelaHome
        self.tela_coleta_frame.place_forget()
        self.img_label_voltar.place_forget()
        TelaHome(self.app).mostrar_tela_home(frame_anterior, img_label_anterior)

    
    def tela_agendar(self, frame, img_label):

        frame.place_forget()
        img_label.place_forget()

        self.tela_agendar_coleta_frame = CTkFrame(master=self.app, width=500, height=400, corner_radius=15, border_color="")
        self.tela_agendar_coleta_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        titulo1 = CTkLabel(self.tela_agendar_coleta_frame, text="Agendar Coleta", font=('Century Ghotic', 32))
        titulo1.place(relx=0.55, rely=0.2, anchor=CENTER)

        self.campo_tipo_residuo = CTkEntry(self.tela_agendar_coleta_frame, placeholder_text="Digite o tipo do resíduo", width=330, height=30, corner_radius=10)
        self.campo_tipo_residuo.place(x=100, y=125)

        self.campo_data = CTkEntry(self.tela_agendar_coleta_frame, placeholder_text="Digite a data da coleta", width=330, height=30, corner_radius=10)
        self.campo_data.place(x=100, y=180)

        self.campo_endereco = CTkEntry(self.tela_agendar_coleta_frame, placeholder_text="Digite o endereço da coleta", width=330, height=30, corner_radius=10)
        self.campo_endereco.place(x=100, y=235)

        btn_agendar = CTkButton(master=self.tela_agendar_coleta_frame, text="Agendar", command=self.agendar, corner_radius=10, fg_color="#985698", hover_color="#ee82ee", width=330)
        btn_agendar.place(x=100, y=290)



    def agendar(self):

        tipo_residuo = self.campo_tipo_residuo.get()
        data = self.campo_data.get()
        endereco = self.campo_endereco.get()

        if tipo_residuo == "" or data == "" or endereco == "":
            label_erro = CTkLabel(self.tela_agendar_coleta_frame, text="Erro: Preencha todos os campos", text_color="red")
            label_erro.place(x=100, y=320)
            self.tela_agendar_coleta_frame.after(1500, label_erro.place_forget)
            return

        data_formatada = self.formatar_data(data)

        if data_formatada:
            
            coleta = Coleta(tipo_residuo=tipo_residuo, data=data, endereco=endereco)
            resultado = coleta.agendar_coleta()

            if "Coleta agendada com sucesso!" in resultado:
                label_resultado = CTkLabel(self.tela_agendar_coleta_frame, text=resultado, text_color="green")
                label_resultado.place(x=100, y=320)
                self.tela_agendar_coleta_frame.after(1500, label_resultado.place_forget)
                return
            
            else:
                label_resultado = CTkLabel(self.tela_agendar_coleta_frame, text=resultado, text_color="red")
                label_resultado.place(x=100, y=320)
                self.tela_agendar_coleta_frame.after(1500, label_resultado.place_forget)
                return

        else:
            
            label_erro1 = CTkLabel(self.tela_agendar_coleta_frame, text="Data inválida! O formato correto é DD/MM/YYYY.", text_color="red")
            label_erro1.place(x=100, y=320)
            self.tela_agendar_coleta_frame.after(1500, label_erro1.place_forget)
            return


    def formatar_data(self, data):
        """
        Formata a data no formato DD/MM/YYYY para YYYY-MM-DD, caso não esteja no formato correto.
        Retorna None se a data for inválida.
        """
        # Verifica se a data está no formato DD/MM/YYYY
        padrao = r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$"
        if re.match(padrao, data):
            try:
                # Converte para o formato YYYY-MM-DD
                data_obj = datetime.strptime(data, "%d/%m/%Y")
                return data_obj.strftime("%Y-%m-%d")
            except ValueError:
                return None
        else:
            return None

        

