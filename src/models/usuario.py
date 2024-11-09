from src.controllers import operador_controller, gestor_residuos_controller
from src.services.servicos_usuarios import Servicos_Usuario

servicos = Servicos_Usuario()

class Usuario:
    '''classe para o usuario do SafeWaste'''

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

    def cadastro(self, nivel_acesso): # função pra realizar o cadastro
        

        print(f"Nome: {self.nome}")
        print(f"Email: {self.email}")
        print("Cadastro realizado com sucesso!")

        resultado = servicos.cadastrar_usuario(self.nome, self.email, self.senha, nivel_acesso)  # Chamando o método de cadastro
        
      
        if nivel_acesso == "operador":
            operador_controller.inicializacao_operador(self.nome, self.email, self.senha)
        elif nivel_acesso == "gestor_residuos":
            gestor_residuos_controller.inicializacao_gestor_residuos(self.nome, self.email, self.senha)

        return resultado


    def login(self): # função pra realizar o login
        
        resultado = servicos.login(self.email, self.senha)
        print(resultado)  # Para depuração, mas você pode remover essa linha
        return resultado 

    def redefinir_senha(self): # função para redefinir a senha
        
        resultado = servicos.redefinir_senha(self.email, self.senha)
        return resultado
