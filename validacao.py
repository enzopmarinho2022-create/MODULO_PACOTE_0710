#função responsavel por verificar e validar a idade.
def validar_idade (idade):

    # validar se a idade esta correta. 
    if idade < 0:

        #cria uma exeção quando a idade e negativa 
        raise ValueError ("A idade não pode ser negativa .")

    # Se chega até aqui sem falhas.
        return True
