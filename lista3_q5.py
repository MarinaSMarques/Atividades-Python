lista = [3, 6, 9, 12, 15, 18]

maior_numero = lista[0]

for numero in lista:
    if numero > maior_numero:
        maior_numero = numero

lista.remove(maior_numero)

print("Lista após remover o maior número:", lista)
print("Maior número removido:", maior_numero)