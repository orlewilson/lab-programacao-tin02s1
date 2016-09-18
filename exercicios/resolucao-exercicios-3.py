"""
Disciplina: Laboratório de Programação
Professor:	Orlewilson B. Maia

Autor:		Orlewilson B. Maia
Data:		13/09/2016
Descrição:	Resolução exercícios realizados em sala 
			de aula.

"""
"""
a
# Questão 1: Fermat

a = int(input("digite um valor para a: "))

b = int(input("digite um valor para b: "))

c = int(input("digite um valor para c: "))

n = int(input("digite um valor para n: "))

if (n > 2):
	if ((a**n + b**n) == c**n):
		print("Holy smokes, Fermat was wrong!")
	else:
		print("No, that doesn´t work.")


a = float(input("Digite seu salário: "))

if (a > 1250):
	b = a * 0.1 + a
else:
	b = a * 0.15 + a

print("Salário com aumento R$ %2.2f" %b)

"""

a = int(input("Digite o valor consumido: "))
b = input("Informe o tipo da instalação: ")

valor = 0

if (b == "R"):
	if (a <= 500):
		valor = a * 0.4
	else:
		valor = a * 0.65

print("O valor consumido foi de R$ %2.2f" %valor)