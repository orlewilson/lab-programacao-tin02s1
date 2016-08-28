"""
Disciplina: Laboratório de Programação
Professor:	Orlewilson B. Maia

Autor:		Orlewilson B. Maia
Data:		17/08/2016
Descrição:	Resolução exercícios realizados em sala 
			de aula.

"""
"""
Questões:

1) Faça um programa que exiba seu nome na tela.

2) Escreva um programa que leia dois valores informados pelo usuário, 
a e b, e exiba o resultado de 2a x 3b.

3) Converta as seguintes expressões matemáticas para que possam ser 
calculadas pelo interpretador Python:

a) 10 + 20 x 30
b) 4^2 ÷ 30
c) (9^2  + 2) x 6 - 1 

OBS: ^ é a operação de potência

"""

# Resposta da primeira questão
print("Orlewilson Maia")


# Resposta da segunda questão
a = int(input("Digite o valor de a: "))
#a = float(input("Digite o valor de a: "))

b = int(input("Digite o valor de b: "))

resultado = 2*a * 3*b

print(resultado)

# Resposta da terceira questão

# letra a)
print("10 + 20 * 30 = ", 10 + 20 * 30)

# letra b)
print("10 + 20 * 30 = ")
print(10 + 20 * 30)

# letra c)
resultado = 10 + 20 * 30
print(resultado)

print("4^2 ÷ 30 = ", 4**2 / 30)

print("(9^2 + 2) x 6 - 1 = ", (9**2 + 2) * 6 - 1 )

