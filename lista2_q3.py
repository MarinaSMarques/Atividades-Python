l = list(range(5))

from random import randint

for i in range (5):
    l[i] = randint(0,100)

print("Lista:", l)
print("Ordem inversa:", l[::-1])
print("Parte da lista: ", l[2:4])

l2 = list(range(5))

print("Lista 1:", l)
print("Lista 2 (inversa):", l2)