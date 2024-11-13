def num_elevado(lista):
    return [num ** 2 for num in lista]

numeros = [7, 4, 6]
lista2 = num_elevado(numeros)
print("Lista com números elevados ao quadrado:", lista2)
