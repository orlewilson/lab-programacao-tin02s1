"""
Disciplina:	Laboratório de Programação
Professor:	Orlewilson B. Maia

Autor:		Orlewilson B. Maia
Data:		07/11/2016
Descrição:	Exemplos de funções recursivas

"""

# exemplo fatorial sem recursão

n = 5
fatorial = 1

for x in range(1,n+1):
	fatorial = fatorial * x

print("Fatorial de %d é %d" %(n,fatorial))	

# exemplo fatorial com recursão
def fatorial(n):

	# condição de parada
	if (n == 1 or n == 0):
		return 1
	else:
		return n*fatorial(n-1)

print("Fatorial de %d é %d" %(n,fatorial(n)))	

# exemplo fibonacci com recursão

def fibonacci(n):

	if (n == 1 or n == 2):
		return 1
	else:
		return fibonacci(n-2) + fibonacci(n-1)

n = 4
print("O elemento %d de Fibonacci é %d" %(n,fibonacci(n)))	

print("Sequência de Fibonacci: ")	
for x in range (1, 10):
	print (str(fibonacci(x)))

# exemplo fibonacci sem recursão
n = 6

a,b = 0,1
for i in range(n):
	a,b = b,a+b

print("O elemento %d de Fibonacci é %d" %(n,a))	



