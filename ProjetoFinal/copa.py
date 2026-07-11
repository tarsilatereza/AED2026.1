from dados import selecoes

# Menu de Seleção
menu = """
[1] Listar seleções
[2] Adicionar seleções
[3] Editar dicas
[4] Remover seleções
[X] Sair
"""

while True:
    opcao = input(menu)
    if opcao.upper() == "X":
      print("Programa encerrado.")
      break

    # Opção para mostrar as seleções participantes  
    elif opcao == '1':
        print("="*9 + " SELEÇÕES " + "="*9)
        for pais in selecoes:
            print(f"{pais}")

    # Opção para adicionar seleções e suas dicas
    elif opcao == '2':
        print("="*9 + " ADICIONAR SELEÇÃO " + "="*9)
        pais = input("Nome da seleção: ").title()
        grupo = input("Grupo: ").upper()
        titulos = int(input("Quantidade de títulos: "))
        continente = input("Continente: ").title()
        lingua = input("Língua: ").title()
        jogador = input("Principal jogadores: ").title()

        # Obs.2: No trecho abaixo consultei IA
        selecoes[pais] = {
            'grupo': grupo, 
            'titulos': titulos, 
            'continente': continente, 
            'lingua': lingua, 
            'principais_jogadores': jogador
        }
        print("Seleção adicionada com sucesso!")
        



    # Opção para editar dicas e nomes das seleções já existentes
    #elif opcao == '3':
        

    elif opcao == '4':
            cod = input("Informe o código que deseja editar ")

            novo_codigo = input(f"Digite o código ou enter para manter '{cod}'")
            novo_nome = input(f"Digite o NOME ou enter para manter '{selecoes[cod]}'")

            if cod != novo_codigo:
                selecoes[novo_codigo] = novo_nome
                del selecoes[cod]
            else:
                selecoes[cod] = novo_nome

    elif opcao == '5':
        cod = input("Informe o código que deseja deletar ")
        # VERIFICAR SE cod existe 
        # del
        # print( ) - > Deletado com sucesso
