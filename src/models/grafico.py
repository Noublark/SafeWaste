from src.controllers.data_controller import DataController

class Grafico:

    def __init__(self):

        self.data_controller = DataController()

    def exibir_grafico(self):
        
        return self.data_controller.gerar_grafico()

    def exibir_dados_em_tabela(self):

        return self.data_controller.gerar_tabela()

