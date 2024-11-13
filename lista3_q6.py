def remover_duplicatas(lista):
    return list(set(lista))

numeros = [1, 2, 3, 1, 4, 2]
resultado = remover_duplicatas(numeros)
print("Lista sem duplicatas:", resultado)