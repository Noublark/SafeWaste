from src.controllers.sessao import SessaoUsuario
from src.services.servicos_coleta import ServicosColeta

class Coleta:
    """classe que representa as coletas do SafeWaste"""

    def __init__(self, tipo_residuo=None, data=None, endereco=None):
        self.tipo_residuo = tipo_residuo
        self.data = data
        self.endereco = endereco

    def agendar_coleta(self):
        """agendar uma nova coleta"""
        usuario_logado = SessaoUsuario().get_usuario_logado()
        
        if usuario_logado:
            # verifica se o tipo de usuário é 'Operador'
            if usuario_logado.get('tipo_usuario') == 'Operador':
                id_usuario = usuario_logado['id_usuario']
                resultado = ServicosColeta().salvar_coleta_db(self.tipo_residuo, self.data, self.endereco, id_usuario)
                return resultado
            else:
                return "Erro: Somente usuários do tipo 'Operador' podem agendar coletas."
        else:
            return "Erro: Usuário não logado ou sem permissão."

    def concluir_coleta(self, id_coleta):
        """concluir uma coleta"""
        resultado = ServicosColeta().concluir_coleta_db(id_coleta)
        return resultado

    def editar_coleta(self, id_coleta, novo_tipo_residuo, nova_data, novo_endereco):
        """editar uma coleta existente"""
        resultado = ServicosColeta().editar_coleta_db(id_coleta, novo_tipo_residuo, nova_data, novo_endereco)
        return resultado

    def cancelar_coleta(self, id_coleta):
        """cancelar uma coleta"""
        resultado = ServicosColeta().cancelar_coleta_db(id_coleta)
        return resultado

    def exibir_coletas(self):
        """exibir todas as coletas do usuário logado"""
        usuario_logado = SessaoUsuario().get_usuario_logado()
        
        if usuario_logado:
            if usuario_logado.get('tipo_usuario') == 'Operador':
                id_usuario = usuario_logado['id_usuario']
                return ServicosColeta().obter_coletas_usuario(id_usuario)
            else:
                return "Erro: Somente usuários do tipo 'Operador' podem visualizar as coletas."
        else:
            return "Erro: Usuário não logado ou sem permissão."