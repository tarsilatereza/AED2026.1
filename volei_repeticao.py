equipe1 = 0
equipe2 = 0
fim_partida = False
set = 0

while not fim_partida:
    print("=="*20)
    print(f"Equipe 1: {equipe1} x {equipe2} Equipe 2")
    print("=="*20)
    
    set = set + 1
    print(f"Set {set}")
    placar1 = int(input("Equipe 1: \t"))
    placar2 = int(input("Equipe 2: \t"))
    
    if placar1 > placar2:
        equipe1 = equipe1 + 1
    else:
        equipe2 = equipe2 + 1
    
    if equipe1 == 3 or equipe2 == 3:
        fim_partida = True
    

    
    

print("Final da partida")
print(f"Equipe 1: {equipe1} x {equipe2} Equipe 2")