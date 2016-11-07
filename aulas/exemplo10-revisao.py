"""
Disciplina:	Laboratório de Programação
Professor:	Orlewilson B. Maia

Autor:		Orlewilson B. Maia
Data:		31/10/2016
Descrição:	Revisão conteúdos para o Provão (2aARE)

"""

a =  [1, 2, ['a', 'b'], 4, 'cd']

print(a[1])
print(a[2])
print(a[4][1])


# exemplo de atribuição múltipla
a = 0
b = 2
c = 0

print(a,b,c)

a, c = b, a + b

#print(a,b,c)


# exercício 1
# Faça um programa, com uma função que
# necessite de três argumentos, e que 
# forneça a soma desses três argumentos. 

def soma(a, b, c):
	return a + b + c

print(soma(1,2,3))

#Faça um programa para imprimir:

#        1
#        2   2
#        3   3   3
#        .....
#        n   n   n   n   n   n  ... n

def imprimirPiramide(n):
	
	cont = 1
	while (cont <= n):
		a = ''
		cont2 = 1
		while (cont2 <= cont):
			a += ' ' + str(cont) + ' '
			cont2 += 1
		
		print(a) 
		cont += 1

def imprimirPiramide2(n):
	
	cont = 1
	for cont in range(1,n+1):
		a = ''
		for cont2 in range(1,cont+1):
			a += ' ' + str(cont) + ' '

		print(a) 


print(imprimirPiramide(5))
print(imprimirPiramide2(5))