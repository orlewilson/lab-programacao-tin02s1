"""
Disciplina:	Laboratório de Programação
Professor:	Orlewilson B. Maia

Autor:		Orlewilson B. Maia
Data:		24/08/2016
Descrição:	Exemplos com operadores relacionais, lógicos e
			expressões lógicas.

"""

# Exemplos de operadores relacionais

a = 1
b = 5
c = 2
d = 1

# operador de igualdade
print(a == d)

# operador de diferença
print(a != b)

# operadores de desigualdade
print("b > c: " + str(b) + " > " + str(c) + " = ", b > c)
print(a < b)
print(d >= a)
print(c <= b)

# Exemplo de operadores relacionais com variáveis do tipo
# lógico

nota1 = 5
nota2 = 6
nota3 = 7

mediaFinal = (nota1 + 2*nota2 + 2*nota3)/5

aprovado = mediaFinal >= 5

print("Média Final ", mediaFinal)
print("Aprovado? ", aprovado)

# Exemplo de operadores lógicos

a = True
b = False

# operador AND (E)
print (a and b)

# operador OR (OU)
print (a or b)

# operador NOT (NÃO)
print (not a)

#  Exemplos  de expressões lógicas

a = 1;b = 3;c = 2; d = 1;

resultado1 = a > b or c < d

resultado2 = b > a or c < d and a == c

resultado3 = (b > a or c < d) and a == c

resultado4 = (b > a or c < d) and not (a == c)

print(resultado1)

print(resultado2)

print(resultado3)

print(resultado4)

