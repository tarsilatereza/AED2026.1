# Uma loja virtual oferece frete grátis para compras a partir de 150 reais. Faça um algoritmo que receba o valor total da compra de um cliente e informe se ele tem direito ao frete grátis ou nao (True ou False)

# Entrada
compra = float(input("Qual o valor da sua compra? "))

# Processamento

tem_frete_gratis = compra < 150
if tem_frete_gratis:

# Saída
	print(f"Sua compra foi no valor de R${compra:.2f}. Portanto, você NÃO tem direito frete grátis")
else:
	print(f"Sua compra foi no valor de R${compra:.2f}. Portanto, você TEM direito ao frete grátis")
