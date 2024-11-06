from random import *
lista = 10
l = list(range(lista))
numeros_negativos = 0
soma_positivos = 0.0
for i in range (lista):
    l[i] = round(uniform(-100,100),2)
    if l[i] < 0:
        numeros_negativos+=1
    else:
        soma_positivos+= l[i]

print("Lista:", l)
print("Quantidade de números negativos: %d" %numeros_negativos)
print("Soma dos números positivos: %.2f" %soma_positivos)