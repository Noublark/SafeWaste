def inicializacao_operador(nome, email, senha, senha2): # apagar depois

    from src.models.operador import Operador
    from src.models.usuario import Usuario

    usuario = Usuario(nome, email, senha, senha2)

    operador = Operador(usuario.nome, usuario.email, usuario.senha, usuario.senha2)