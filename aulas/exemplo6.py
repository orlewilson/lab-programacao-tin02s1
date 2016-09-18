"""
Disciplina:	Laboratório de Programação
Professor:	Orlewilson B. Maia

Autor:		Orlewilson B. Maia
Data:		14/09/2016
Descrição:	Exemplos repetição (while).

"""

"""
Sintaxe do while

while <condição>:
	bloco

"""

x = 1
while (x <= 5):
	print(x)
	x = x + 1


palavra = ""
while (palavra.lower() != "q"):
	palavra = input ("Digite alguma palavra: ")
	print(palavra)


# média = (n1 + n2 + n3)/3

# sem while
n1 = int(input("Digite uma nota: "))
n2 = int(input("Digite uma nota: "))
n3 = int(input("Digite uma nota: "))

media = (n1 + n2 + n3)/3

print("Média é igual a %2.2f" %media)

# com while

soma = 0
cont = 1

while (cont <= 3):
	valor = int(input("Digite uma nota: "))
	soma = soma + valor
	cont = cont + 1

media = soma/3
print("Média é igual a %2.2f" %media)

soma = 0
cont = 1

while True:
	valor = int(input("Digite uma nota: "))
	soma = soma + valor
	cont += 1 # igual a cont = cont + 1

	if (cont > 3):
		break

media = soma/3
print("Média é igual a %2.2f" %media)