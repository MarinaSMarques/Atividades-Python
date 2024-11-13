from random import *
lista = 10
l = list(range(lista))
soma_pares = 0.0

for i in range (10):
    if l[i] % 2 == 0:
        soma_pares += l[i]

print("lista:", l)
print("Soma dos números pares:", soma_pares)
