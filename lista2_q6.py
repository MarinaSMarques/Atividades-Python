lista = 20
preco = []
quantidade = list(range(lista))
from random import randint

def gravar_Listas():
    for i in range(lista):
        preco.append(randint(0, 20))
        quantidade[i] = randint(0,20)

def faturamento():
    for i in range(lista):
        faturamento = (preco * quantidade[i])
        print("Faturamento:", faturamento)

def faturamento_total():
    for i in range(lista):
        faturamento_total = (preco[i] * quantidade[i])
        print("Faturamento total:", faturamento_total)

gravar_Listas()
faturamento()
faturamento_total()
