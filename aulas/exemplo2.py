"""
Disciplina:	Laboratório de Programação
Professor:	Orlewilson B. Maia

Autor:		Orlewilson B. Maia
Data:		10/08/2016
Descrição:	Criação e atribuição variáveis.

"""

# Impressão de conteúdo numérico
print (2 + 2)

# Atribuindo valor a uma variável
a =  2 + 2

# Imprimindo o conteúdo de uma variável
print (a)

# Exemplo de cálculo de aumento de salário

#salario = 4000
# entrada de valor pelo usuário
salario = float(input("Digite o salário desejado:"))

#aumento = 50
aumento = int(input("Digite o valor do aumento:"))

#salario = salario + (salario*aumento)/100

salario += (salario*aumento)/100

print (salario)

# para compilar usa-se 
# python3 nome_do_arquivo.py

# nomes de variáveis

variavel = 1 	# válido
#variavel 2 = 2	# não válido
variavel_3 = 3	# válido
variavel4 = 4	# válido
_variavel5 = 5	# válido
#6variavel = 6	# não válido

