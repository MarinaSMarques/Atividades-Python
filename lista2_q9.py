def lista_x():
    for i in range (max_lista):
        x[i] = randint(1,17)

def lista_y():
    i = max_lista - 1
    while i >= 0:
        y.append(x[i])
        i -= 1

from random import randint
max_lista = 5
x = list(range(max_lista))
y = []
lista_x()
lista_y()
z = sorted(x)
print("Lista x: (em ordem)", z)
print("Lista x:", x)
print("Lista y (inversa):", y)
