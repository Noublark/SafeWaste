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
        self.tela_agendar_coleta_frame = None
        self.tela_editar_coleta_frame = None
        self.mostrar_popup_concluido_frame = None
        self.mostrar_popup_remover_frame = None
        self.img_label_voltar = None
        self.img_label_voltar_coleta = None
        self.img_label_voltar_coleta1 = None
        self.img_label_adicionar = None
        
        self.img_voltar = Image.open("src/resources/static/back arrow.png")
        self.img_voltar = self.img_voltar.resize((40, 50), Image.LANCZOS)
        self.img_tk = ImageTk.PhotoImage(self.img_voltar)

    def esconder_todos_frames(self): #Função para esconder todos os frames
        frames = [
            self.tela_coleta_frame,
            self.tela_agendar_coleta_frame, 
            self.tela_editar_coleta_frame,
            self.mostrar_popup_concluido_frame,
            self.mostrar_popup_remover_frame
        ]
        
        labels = [
            self.img_label_voltar,
            self.img_label_voltar_coleta,
            self.img_label_voltar_coleta1
        ]
        
        for frame in frames:
            if frame:
                frame.destroy()
                
        for label in labels:
            if label:
                label.destroy()

    def mostrar_tela_coleta(self, frame):
        self.esconder_todos_frames()
        
        if frame:
            frame.destroy()

        self.tela_coleta_frame = CTkFrame(master=self.app, width=500, height=400, corner_radius=15, border_color="")
        self.tela_coleta_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.img_label_voltar = CTkLabel(self.app, image=self.img_tk, text="", cursor="hand2")
        self.img_label_voltar.image = self.img_tk
        self.img_label_voltar.bind("<Button-1>", lambda event: self.voltar())
        self.img_label_voltar.place(x=20, y=20)

        img_adicionar = Image.open("src/resources/static/adicionar.png")
        img_adicionar = img_adicionar.resize((25,25), Image.LANCZOS)
        img_tk1 = ImageTk.PhotoImage(img_adicionar)

        self.img_label_adicionar = CTkLabel(self.tela_coleta_frame, image=img_tk1, text="", cursor="hand2")
        self.img_label_adicionar.bind("<Button-1>", lambda event: self.mostrar_tela_agendar())
        self.img_label_adicionar.place(x=460, y=30)

        titulo = CTkLabel(self.tela_coleta_frame, text="Coletas", font=('Century Ghotic', 32))
        titulo.place(x=200, y=25)

        coletas = CTkFrame(self.tela_coleta_frame, width=300, height=300, corner_radius=8, fg_color="#080808", border_color="")
        coletas.place(x=25, y=80)

        coletas_config = CTkFrame(self.tela_coleta_frame, width=150, height=300, corner_radius=8, fg_color="#985698", border_color="")
        coletas_config.place(x=325, y=80)

        self.adicionar_labels_e_imagens(coletas, coletas_config)

    def adicionar_labels_e_imagens(self, coletas, coletas_config):
        y_inicial = 10
        espacamento_y = 60
        
        coletas_usuario = Coleta().exibir_coletas()
        
        if not coletas_usuario:
            label_vazio = CTkLabel(coletas, text="Nenhuma coleta agendada", font=('Century Gothic', 16))
            label_vazio.place(x=10, y=y_inicial)
        else:
            for i, coleta in enumerate(coletas_usuario):
                id_coleta = coleta[0]  # Coluna id_coleta (garanta que o id esteja sendo retornado pela consulta)
                tipo_residuo = coleta[1]  # Coluna tipo_residuo
                data = coleta[2]  # Coluna data
                endereco = coleta[3]  # Coluna endereco

                label_text = f"{tipo_residuo} - {data} - {endereco}"
                label = CTkLabel(coletas, text=label_text, font=('Century Gothic', 16))
                label.place(x=10, y=y_inicial + i * espacamento_y)

                # Adiciona as imagens para ações

                img_concluido = Image.open("src/resources/static/concluido.png").resize((30, 30), Image.LANCZOS)
                img_tk1 = ImageTk.PhotoImage(img_concluido)
                img_label_concluido = CTkLabel(coletas_config, image=img_tk1, text="", cursor="hand2")
                img_label_concluido.image = img_tk1
                img_label_concluido.bind("<Button-1>", lambda event, id=id_coleta: self.mostrar_popup_concluido(id))
                img_label_concluido.place(x=13, y=y_inicial + i * espacamento_y)

                img_editar = Image.open("src/resources/static/lapis.png").resize((30, 30), Image.LANCZOS)
                img_tk2 = ImageTk.PhotoImage(img_editar)
                img_label_editar = CTkLabel(coletas_config, image=img_tk2, text="", cursor="hand2")
                img_label_editar.image = img_tk2
                img_label_editar.bind("<Button-1>", lambda event, id=id_coleta: self.mostrar_tela_editar(id))
                img_label_editar.place(x=63, y=y_inicial + i * espacamento_y)

                img_remover = Image.open("src/resources/static/lixeira.png").resize((30, 30), Image.LANCZOS)
                img_tk3 = ImageTk.PhotoImage(img_remover)
                img_label_remover = CTkLabel(coletas_config, image=img_tk3, text="", cursor="hand2")
                img_label_remover.image = img_tk3
                img_label_remover.bind("<Button-1>", lambda event, id=id_coleta: self.mostrar_popup_remover(id))
                img_label_remover.place(x=113, y=y_inicial + i * espacamento_y)

    def voltar(self):
        from .tela_home import TelaHome
        self.esconder_todos_frames()
        TelaHome(self.app).mostrar_tela_home()

    def mostrar_tela_agendar(self):
        self.esconder_todos_frames()

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

        self.img_label_voltar_coleta = CTkLabel(self.app, image=self.img_tk, text="", cursor="hand2")
        self.img_label_voltar_coleta.bind("<Button-1>", lambda event: self.mostrar_tela_coleta(None))
        self.img_label_voltar_coleta.place(x=20, y=20)

    def agendar(self):
        tipo_residuo = self.campo_tipo_residuo.get()
        data = self.campo_data.get()
        endereco = self.campo_endereco.get()

        if tipo_residuo == "" or data == "" or endereco == "":
            label_erro = CTkLabel(self.tela_agendar_coleta_frame, text="Erro: Preencha todos os campos", text_color="red")
            label_erro.place(x=100, y=320)
            self.tela_agendar_coleta_frame.after(1500, label_erro.destroy)
            return

        data_formatada = self.formatar_data(data)

        if data_formatada:
            coleta = Coleta(tipo_residuo=tipo_residuo, data=data, endereco=endereco)
            resultado = coleta.agendar_coleta()

            if "Coleta agendada com sucesso!" in resultado:
                label_resultado = CTkLabel(self.tela_agendar_coleta_frame, text=resultado, text_color="green")
                label_resultado.place(x=180, y=330)
                self.tela_agendar_coleta_frame.after(1500, lambda: self.mostrar_tela_coleta(None, None, None))
            else:
                label_resultado = CTkLabel(self.tela_agendar_coleta_frame, text=resultado, text_color="red")
                label_resultado.place(x=180, y=330)
                self.tela_agendar_coleta_frame.after(1500, label_resultado.destroy)
        else:
            label_erro1 = CTkLabel(self.tela_agendar_coleta_frame, text="Data inválida! O formato correto é DD/MM/YYYY.", text_color="red")
            label_erro1.place(x=130, y=330)
            self.tela_agendar_coleta_frame.after(1500, label_erro1.destroy)

    def mostrar_popup_concluido(self, id_coleta):
        self.mostrar_popup_concluido_frame = CTkFrame(master=self.tela_coleta_frame, width=400, height=250, corner_radius=15, border_color="grey", fg_color="#080808")
        self.mostrar_popup_concluido_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        titulo2 = CTkLabel(self.mostrar_popup_concluido_frame, text="Concluir coleta?", font=('Century Ghotic', 32))
        titulo2.place(relx=0.5, rely=0.3, anchor=CENTER)

        btn_concluir = CTkButton(master=self.mostrar_popup_concluido_frame, text="Sim", command=lambda: self.concluir_coleta(id_coleta), corner_radius=10, fg_color="#985698", hover_color="#ee82ee", width=125)
        btn_concluir.place(x=225, y=150)

        btn_cancelar = CTkButton(master=self.mostrar_popup_concluido_frame, text="Cancelar", command=self.mostrar_popup_concluido_frame.destroy, corner_radius=10, fg_color="#b20000", hover_color="#e50000", width=125)
        btn_cancelar.place(x=50, y=150)

    def mostrar_tela_editar(self, id_coleta):
        self.esconder_todos_frames()

        self.tela_editar_coleta_frame = CTkFrame(master=self.app, width=500, height=400, corner_radius=15, border_color="")
        self.tela_editar_coleta_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        titulo4 = CTkLabel(self.tela_editar_coleta_frame, text="Editar Coleta", font=('Century Ghotic', 32))
        titulo4.place(relx=0.55, rely=0.2, anchor=CENTER)

        self.campo_novo_tipo_residuo = CTkEntry(self.tela_editar_coleta_frame, placeholder_text="Digite o tipo do resíduo", width=330, height=30, corner_radius=10)
        self.campo_novo_tipo_residuo.place(x=100, y=125)

        self.campo_nova_data = CTkEntry(self.tela_editar_coleta_frame, placeholder_text="Digite a data da coleta", width=330, height=30, corner_radius=10)
        self.campo_nova_data.place(x=100, y=180)

        self.campo_novo_endereco = CTkEntry(self.tela_editar_coleta_frame, placeholder_text="Digite o endereço da coleta", width=330, height=30, corner_radius=10)
        self.campo_novo_endereco.place(x=100, y=235)

        btn_editar = CTkButton(master=self.tela_editar_coleta_frame, text="Concluir", command=lambda: self.editar_coleta(id_coleta), corner_radius=10, fg_color="#985698", hover_color="#ee82ee", width=330)
        btn_editar.place(x=100, y=290)

        self.img_label_voltar_coleta1 = CTkLabel(self.app, image=self.img_tk, text="", cursor="hand2")
        self.img_label_voltar_coleta1.bind("<Button-1>", lambda event: self.mostrar_tela_coleta(None))
        self.img_label_voltar_coleta1.place(x=20, y=20)

    def mostrar_popup_remover(self, id_coleta):
        self.mostrar_popup_remover_frame = CTkFrame(master=self.tela_coleta_frame, width=400, height=250, corner_radius=15, border_color="grey", fg_color="#080808")
        self.mostrar_popup_remover_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        titulo3 = CTkLabel(self.mostrar_popup_remover_frame, text="Remover Coleta?", font=('Century Ghotic', 32))
        titulo3.place(relx=0.5, rely=0.3, anchor=CENTER)

        btn_concluir = CTkButton(master=self.mostrar_popup_remover_frame, text="Sim", command=lambda: self.remover_coleta(id_coleta), corner_radius=10, fg_color="#985698", hover_color="#ee82ee", width=125)
        btn_concluir.place(x=225, y=150)

        btn_cancelar = CTkButton(master=self.mostrar_popup_remover_frame, text="Cancelar", command=self.mostrar_popup_remover_frame.destroy, corner_radius=10, fg_color="#b20000", hover_color="#e50000", width=125)
        btn_cancelar.place(x=50, y=150)

    def formatar_data(self, data):
        """
        Formata a data no formato DD/MM/YYYY para YYYY-MM-DD, caso não esteja no formato correto.
        Retorna None se a data for inválida.
        """
        padrao = r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$"
        if re.match(padrao, data):
            try:
                data_obj = datetime.strptime(data, "%d/%m/%Y")
                return data_obj.strftime("%Y-%m-%d")
            except ValueError:
                return None
        else:
            return None

    def editar_coleta(self, id_coleta):
        tipo_residuo = self.campo_novo_tipo_residuo.get()
        data = self.campo_nova_data.get()
        endereco = self.campo_novo_endereco.get()

        if tipo_residuo == "" or data == "" or endereco == "":
            label_erro = CTkLabel(self.tela_editar_coleta_frame, text="Erro: Preencha todos os campos", text_color="red")
            label_erro.place(x=100, y=320)
            self.tela_editar_coleta_frame.after(1500, label_erro.destroy)
            return

        data_formatada = self.formatar_data(data)

        if data_formatada:
            coleta = Coleta(tipo_residuo=tipo_residuo, data=data_formatada, endereco=endereco)
            resultado = coleta.editar_coleta(id_coleta, tipo_residuo, data, endereco)

            if "Coleta editada com sucesso!" in resultado:
                label_resultado = CTkLabel(self.tela_editar_coleta_frame, text=resultado, text_color="green")
                label_resultado.place(x=185, y=330)
                label_resultado.update()
                self.tela_editar_coleta_frame.after(1500, self.mostrar_tela_coleta(None, None, None))
            else:
                label_resultado = CTkLabel(self.tela_editar_coleta_frame, text=resultado, text_color="red")
                label_resultado.place(x=180, y=330)
                self.tela_editar_coleta_frame.after(1500, self.mostrar_tela_coleta(None, None, None))
        else:
            label_erro1 = CTkLabel(self.tela_editar_coleta_frame, text="Data inválida! O formato correto é DD/MM/YYYY.", text_color="red")
            label_erro1.place(x=130, y=330)
            self.tela_editar_coleta_frame.after(1500, label_erro1.destroy)

    def concluir_coleta(self, id_coleta):
        coleta = Coleta()
        resultado = coleta.concluir_coleta(id_coleta)
        
        if "Coleta concluída com sucesso!" in resultado:
            label_concluido = CTkLabel(self.mostrar_popup_concluido_frame, text=resultado, text_color="green")
            label_concluido.place(x=115, y=200)
            self.mostrar_popup_concluido_frame.after(1500, lambda: self.mostrar_tela_coleta(None, None, None))
        else:
            label_erro = CTkLabel(self.mostrar_popup_concluido_frame, text=resultado, text_color="red")
            label_erro.place(x=115, y=200)
            self.mostrar_popup_concluido_frame.after(1500, lambda: self.mostrar_tela_coleta(None, None, None))

    def remover_coleta(self, id_coleta):
        coleta = Coleta()
        resultado = coleta.cancelar_coleta(id_coleta)
        
        if "Coleta cancelada com sucesso!" in resultado:
            label_removido = CTkLabel(self.mostrar_popup_remover_frame, text=resultado, text_color="green")
            label_removido.place(x=115, y=200)
            self.mostrar_popup_remover_frame.after(1500, lambda: self.mostrar_tela_coleta(None, None, None))
        else:
            label_erro = CTkLabel(self.mostrar_popup_remover_frame, text=resultado, text_color="red") 
            label_erro.place(x=115, y=200)
            self.mostrar_popup_remover_frame.after(1500, lambda: self.mostrar_tela_coleta(None, None, None))
