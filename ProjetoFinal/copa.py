from dados import selecoes
import random

# Menu de Seleção
menu = """
[1] Listar seleções
[2] Adicionar seleções
[3] Editar dicas
[4] Remover seleções
[5] Jogo de pistas
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
        print("="*9 + "\033[32mADICIONAR SELEÇÃO\033[m" + "="*9)
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
    # Obs.3: Consultei IA para entender como editar elementos do dicionário "dados.py"
    elif opcao == '3':
        print("="*9 + "\033[33mEDITAR SELEÇÃO\033[m" + "="*9)
        pais = input("Digite o nome da seleção que deseja editar: ").title()
        if pais in selecoes:
            print(f"Editando os dados de {pais}.")
            print("ATENÇÃO: deixe em branco e aperte [Enter] para manter os dados atuais.")

            atual_grupo = selecoes[pais]['grupo']
            novo_grupo = input(f"Grupo atual [{atual_grupo}]: ").upper()
            if novo_grupo != "":
                selecoes[pais]['grupo'] = novo_grupo
            atual_titulos = selecoes[pais]['titulos']
            novo_titulos = input(f"Títulos atuais [{atual_titulos}]: ")
            if novo_titulos != "":
                selecoes[pais]['titulos'] = int(novo_titulos)
            atual_continente = selecoes[pais]['continente']
            novo_continente = input(f"Continente atual [{atual_continente}]: ").title()
            if novo_continente != "":
                selecoes[pais]['continente'] = novo_continente
            atual_lingua = selecoes[pais]['lingua']
            novo_lingua = input(f"Língua atual [{atual_lingua}]: ").title()
            if novo_lingua != "":
                selecoes[pais]['lingua'] = novo_lingua
                print(f"Os dados de {pais} foram atualizados!")

            print("="*20)
    
            print(f"Essas são as novas dicas da seleção: {selecoes[pais].items()}")
            
        else:
            print(f"ATENÇÃO! A seleção '{pais}' não está cadastrada.")
            nova_opcao = input("Deseja ir para a tela de adicionar seleção [S/N]? ")
            if nova_opcao.upper() == "S":
                print("Redirecionando para o MENU. Digite a opção 2 no menu a seguir.")
                continue # Uso do 'continue' como sugestão de IA, não conhecia
            else:
                print("\n-> Operação cancelada. Voltando ao menu principal...")
                continue       

    # Opção para remover seleções da lista
    elif opcao == '4':
        print("="*9 + "\033[31mELIMINAR SELEÇÃO\033[m" + "="*9)
        pais = input("Informe o nome da seleção que deseja eliminar: ").title()
        if pais in selecoes:
            del selecoes[pais]
            print(f"{pais} deletado")
        else:
            print("Este país não está no sistema. Por favor, verifique a grafia ou adicione uma nova seleção.")

# Fim das operações do MENU

# Jogo de adivinhação
    elif opcao == '5':
        print("="*9 + "\033[95mJOGO DE ADIVINHAÇÃO - SELEÇÃO SECRETA\033[m" + "="*9)
        #Obs.4: Uso de IA para entender como funciona as operações da biblioteca "random"
        pais_secreto = random.choice(list(selecoes.keys()))
        dados_secretos = selecoes[pais_secreto]
        pistas = [
            f"Continente: {dados_secretos['continente']}",
            f"Número de títulos: {dados_secretos['titulos']}",
            f"Grupo na Copa do Mundo de 2026: {dados_secretos['grupo']}",
            f"Principais Jogadores: {', '.join(dados_secretos['principais_jogadores'])}"
        ]
        print("Tente adivinhar a seleção secreta! Você receberá 4 dicas.")
        print("Se não souber, clique em [Enter] para ver a próxima dica.\n")
        
        acertou = False
        #Obs.5: Uso de IA neste laço
        for i in range(len(pistas)):
            print(f"-> Dica {i+1}: {pistas[i]}")
            chute = input("Qual é o seu chute? ").title()
            if chute == pais_secreto:
                print(f"Você acertou :) A seleção era {pais_secreto}.")
                acertou = True
                break
            elif chute != "":
                print("Errou :( Vamos para a próxima dica...\n")
                if not acertou:
                    print("As dicas acabaram. Você perdeu.")
                    print(f"A seleção secreta era: {pais_secreto}")
                

        input("\nAperte [Enter] para voltar ao menu principal...")


