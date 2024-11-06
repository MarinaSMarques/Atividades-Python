lista = 3
l1 = []
l2 = list(range(lista))
from random import randint

def gravar_listas():
     for i in range (lista):
          l1.append(randint(0,100))
          l2[i] = randint(0,100)

def intercalaçao():
     l3 = []
     for i in range(lista):
         l3.append(l1[i])
         l3.append(l2[i])
     return l3

gravar_listas()
print("Lista 1: ", l1)
print("Lista 2: ", l2)
print("Lista intercalada  : ", intercalaçao())