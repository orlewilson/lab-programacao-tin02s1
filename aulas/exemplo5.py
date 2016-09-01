"""
Disciplina:	Laboratório de Programação
Professor:	Orlewilson B. Maia

Autor:		Orlewilson B. Maia
Data:		31/08/2016
Descrição:	Exemplos com condições (if).

"""

"""
Sintaxe

if (condição):
	bloco verdadeiro
else:
	bloco falso

if (condição):
	bloco verdadeiro
else:
	if (condição):
		bloco verdadeiro

if (condição):
	bloco verdadeiro
elif (condição):
	bloco verdadeiro
else:
	bloco falso

"""

# Exemplos com if

x = int(input("Digite um valor para x: "))

y = int(input("Digite um valor para y: "))

if (x < y):
	print("%d é menor que %d" %(x,y))

if (x >= y):
	print("%d é maior ou igual a %d" %(x,y))

if (x < y):
	print("%d é menor que %d" %(x,y))
else:
	print("%d é maior ou igual a %d" %(x,y))

# --------------------------------

categoria = int(input("Digite a categoria do produto: "))

preco = 0.0

# Solução 1
if (categoria == 1):
	preco = 10.0

if (categoria == 2):
	preco = 18.0

if (categoria == 3):
	preco = 23.0

if (categoria == 4):
	preco = 26.0

if (categoria == 5):
	preco = 31.0

# Solução 2
if (categoria == 1):
	preco = 10.0

else:
	if (categoria == 2):
		preco = 18.0

	else:
		if (categoria == 3):
			preco = 23.0

		else:
			if (categoria == 4):
				preco = 26.0

			else:
				if (categoria == 5):
					preco = 31.0

# Solução 3
if (categoria == 1):
	preco = 10.0

elif (categoria == 2):
	preco = 18.0

elif (categoria == 3):
	preco = 23.0

elif (categoria == 4):
	preco = 26.0

elif (categoria == 5):
	preco = 31.0

print("O preço da categoria %d é R$ %2.2f. " %(categoria, preco))