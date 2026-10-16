# Importa as funções disponibilizadas pelo pacote sistem
from sistema import cadastrar_aluno, validar_idade

try:
    # Solicitar os dados ao usuario
    nome = input("Digite o nome do aluno: ").strip()
    idade = int(input("Digite a idade do aluno" ))

    # Verifica se o nome foi preenchido
    if not nome:
        raise ValueError ("O nome não pode ficar vazio.")

        # Valida a idade antes de concluir o cadastro 
        validade_idade(idade)

        # Chama a função que cria o cadastro 
        aluno = cadastrar_aluno (nome, idade)

        # Exibir dados cadastrados
        print("\n Castro realizado com sucesso!")
        print("Nome: ",aluno[nome])
        print("Idade: ",aluno["idade"])

        # Exeções de erros
finally:
    print ("Processo de cadastro finalizado.")
