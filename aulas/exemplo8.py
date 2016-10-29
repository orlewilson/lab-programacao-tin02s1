"""
Disciplina:	Laboratório de Programação
Professor:	Orlewilson B. Maia

Autor:		Orlewilson B. Maia
Data:		11/10/2016
Descrição:	Exemplos de vetores e matrizes (listas)

"""

# exemplo de vetor 
lista = [1,2,3]


#imprime toda a lista
print(lista)


#imprime o valor dado um índice
print(lista[1])


#imprime o tamanho da lista
print(len(lista))


#exemplo de vetor
lista = [5,3,6]

#imprime toda a lista
print(lista)


#imprime o valor dado um índice
print(lista[1])


#imprime o tamanho da lista
print(len(lista))


#atribuir valor dado um índice
lista[1] = 4


#mostrar valores nova lista
print(lista)


#atribuir valor dado um índice
lista[1] = 'oi'
print(lista)


#atribuir valor de uma lista dentro de
#outra lista
lista[2] = [1,2,3]

print(lista)
print(lista[2][0])
print(lista[1][1])

#atribuir valor de uma lista dentro de
#outra lista
lista = [[0,3,7],[3,5,8],[1,7,9]]

print(lista[1][2])


Lista = [11, 14, 71]
print(Lista)

# adiciona novo elemento a lista na última posição
Lista.append(23) # Lista = [11, 14, 71, 23]

# adiciona novo elemento no índice indicado na lista
Lista.insert(0,12) # Lista = [12, 11, 14, 71, 23]

Lista.insert(1,15) # Lista = [12, 15, 11, 14, 71, 23]

# retorna a quantidade de vezes que o elemento aparece 
# na lista
print(Lista.count(14)) # 1

Lista.insert(0,23) # Lista = [23, 12, 15, 11, 14, 71, 23]

# remove um elemento da lista
Lista.remove(23) # Lista = [12, 15, 11, 14, 71, 23]

# Cópia de lista
Lista2 = Lista

# Inverte a lista
Lista2.reverse()
print(Lista2) #Lista2 = [23, 71, 14, 11, 15, 12]

