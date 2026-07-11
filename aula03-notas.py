n1 = float(input("Nota 1: \t"))
n2 = float(input("Nota 2: \t"))
n3 = float(input("Nota 3: \t"))
total = n1 + n2 + n3
if (n1 + n2 + n3)/3 < 7:
    print("TÁ DE Reposição""")
    reposicao = float(input("Nota da reposição: \t"))
else:
    print("Aprovada")
media = total + reposicao - min ([n1, n2, n3, reposicao])/3
print("Média anterior:", total/3, "Menor nota:", min([n1,n2,n3]))
print("Média Final:", round(media, 1))