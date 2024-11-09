def inicializacao_gestor_residuos(nome, email, senha, senha2):

    from src.models.gestor_residuos import Gestor_Residuos
    from src.models.usuario import Usuario

    usuario = Usuario(nome, email, senha, senha2)

    gestor_residuo = Gestor_Residuos(usuario.nome, usuario.email, usuario.senha, usuario.senha2)