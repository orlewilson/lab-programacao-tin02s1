"""
Disciplina:	Laboratório de Programação
Professor:	Orlewilson B. Maia

Autor:		Orlewilson B. Maia
Data:		20/09/2016
Descrição:	Exemplos repetição (for).

"""

"""
Sintaxe do for

for <variavel> in <lista>:
	bloco

"""

L = [1, 2, 3]

x = 0
while x < len(L):
	e = L[x]
	print(e)
	x = x + 1

# imprime todos os valores de uma lista
for x in L:
	print(x)

# imprime todos os valores de 1 até 3
for x in range(1,4):
	print(x)

# imprime todos os valores de 0 até 3
for x in range(4):
	print(x)

# imprime todos os valores entre 0 e 9 incrementando
# de 2 em 2
for x in range(0,10,2):
	print(x)

# imprime todos os valores entre 0 e 10 incrementando
# de 2 em 2 menor que 5
for x in range(0,10,2):
	
	if (x < 5):
		print(x)
	else:
		break









# Números Pares
for x in range(1,101):
	if (x % 2 == 0):
		print(x)

for x in range(2,101,2):
	print(x)


# Números Ímpares
for x in range(1,101):
	if (x % 2 != 0):
		print(x)

for x in range(1,101,2):
	print(x)








# Números Primos
print(2)
for x in range(3,101):
	if (x % 2 != 0):
		cont = 0
		for y in range(3, x+1):
			if (x % y == 0):
				cont = cont + 1
			if (cont > 2):
				break

		if (cont == 1):
			print(x)
