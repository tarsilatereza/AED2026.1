numero = int(input("Insira o número: "))

def quadrado_perfeito(numero):
    if numero < 0:
        return False
        
    raiz_inteira = int(numero**0.5)
    # Se ao multiplicarmos a raiz intera por ela mesma voltarmos ao 'numero', é perfeito

    if raiz_inteira * raiz_inteira == numero:
        print(f"{numero} quadrado é perfeito. Pois, {raiz_inteira} é a raiz inteira dele")
        return True
    else:
        print(f"{numero} não é quadrado perfeito.")
        return False

quadrado_perfeito(numero)