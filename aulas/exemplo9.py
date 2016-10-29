"""
Disciplina:	Laboratório de Programação
Professor:	Orlewilson B. Maia

Autor:		Orlewilson B. Maia
Data:		28/10/2016
Descrição:	Exemplos de funções

"""

"""
Sintaxe

def nome_da_funcao(arg1, arg2, ..., argN):
	comando
	...
	comando


def nome_da_funcao():
	comando
	...
	comando
"""

#soma de dois números
def soma (x, y):
	global z
	z = x + y
	return z

z = 10
print(z)

a = soma(5,2)
print(a)

print(soma(7,5))

print(z)

# exemplo de função para verificar se uma
# palavra é palíndromo

# sem função
a = "arara"
b = a[::-1]

if (a == b):
	print("A palavra %s é palíndroma" %a)
else:
	print("A palavra %s não é palíndroma" %a)

c = "1011"
d = c[::-1]

if (c == d):
	print("A palavra %s é palíndroma" %c)
else:
	print("A palavra %s não é palíndroma" %c)


# com função

def verifica_palindromo(palavra):
	palavra_invertida = palavra[::-1]
	if (palavra == palavra_invertida):
		return ("A palavra %s é palíndroma" %palavra)
	else:
		return ("A palavra %s não é palíndroma" %palavra)

a = "arara"
b = "1010"

print(verifica_palindromo(a))
print(verifica_palindromo(b))


