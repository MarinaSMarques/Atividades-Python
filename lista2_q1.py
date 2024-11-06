lista = 100
l = list(range(lista))
l_par = []
l_impar =[]

from random import *
def criar_lista():
    for i in range (lista):
        l[i] = randint(-100,100)

def quantidade_numeros():
    quant_par = 0
    quant_impar = 0
    for i in range (lista):
        if l[i] %2 ==0:
            quant_par+=1
        else:
            quant_impar+=1
    print("Quantidade de numeros pares: %d." %quant_par)
    print("Quantidade de numeros impares: %d." %quant_impar)

def gerar_listas():
    for i in range (lista):
        if l[i] %2 == 0:
            l_par.append(l[i])
        else:
            l_impar.append(l[i])

def maior_elemento():
    maior_elemento = l[0]
    for i in range (1, lista):
        if l[i] > maior_elemento:
            maior_elemento = l[i]
    print("Maior elemento da lista l: %d" %maior_elemento)

criar_lista()
quantidade_numeros()
gerar_listas()
maior_elemento()
print("Lista l", l)
print("Números pares:", l_par)
print("Números ímpares:", l_impar)