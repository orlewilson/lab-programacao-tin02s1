"""
Disciplina:	Laboratório de Programação
Professor:	Orlewilson B. Maia

Autor:		Orlewilson B. Maia
Data:		30/08/2016
Descrição:	Exemplos com variáveis String.

"""


# função len retorna o tamanho da String

a = "A"

print(len(a))

b = "Orlewilson Maia"

print(len(b))

print(len(""))

print(len(" "))

# manipulando strings

a = "ABCDEFGHI"

print(a[0]) # pega somente uma posição

print(a[2]) # pega somente uma posição

print(a[0:2]) # pega um intervalo

print(a[3:]) # pega um intervalo

print(a[:4]) # pega um intervalo

print(a[-3:9]) # pega um intervalo

print(a[-3:-1]) # pega um intervalo

print(a[0], a[4]) # pega um intervalo


#  Concatenação de strings

a = "O rato "
b = "roeu "
c = "a roupa "
d = "do rei de Roma"

print(a + b + c + d) # união (+)

print(a + " " + b + " " + c + " " + d)

print(a * 3 + b * 2 + c + d) # repetição (*)

# Composição em strings

nome = "João"
anos = 25
meses = 3
dias = 6

"""
%d = números inteiros
%f = números decimais
%s = strings
"""

print("O " + nome + " tem " + str(anos) + " anos")

print("O %s tem %d anos" % (nome,anos))

print("O " + nome + " tem " + str(anos) + " anos, " 
	+ str(meses) + " meses e " + str(dias) + " dias" )

print("O %s tem %d anos, %d meses e %d dias" 
	% (nome, anos, meses, dias))


pi = 3.14159265358979

print("O valor de pi é %2.5f" % pi)

pi = str(pi)

print("O valor de pi é %s" % pi[0:6])

idade = 5

print("%3d" % idade)

print("%03d" % idade)

idade = 15

print("%03d" % idade)









