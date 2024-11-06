lista = 15
l = list(range(lista))

from random import *
def gravar_lista():
        for i in range (lista):
            l[i] = randint(-100,100)

def maior_numero():
    maior_numero = l[0]
    for i in range (1, lista):
        if l[i] > maior_numero:
            maior_numero = l[i]
    print("O maior número da lista é: %d." %maior_numero)


def menor_numero():
    menor_numero = l[0]
    for i in range (1, lista):
        if l[i] < menor_numero:
            menor_numero = l[i]
    print("O menor número da lista é: %d" %menor_numero)

gravar_lista()
maior_numero()
menor_numero()
print("Lista:", l)