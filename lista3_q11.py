def intercalar_listas(lista1, lista2):
    intercalada = []

    for a, b in zip(lista1, lista2):
        intercalada.append(a)
        intercalada.append(b)

    intercalada.extend(lista1[len(lista2):])
    intercalada.extend(lista2[len(lista1):])
    return intercalada

lista1 = [2, 5, 8]
lista2 = [4, 7, 9, 16, 14,35]
resultado = intercalar_listas(lista1, lista2)

print("Lista 1:", lista1)
print("Lista 2", lista2)
print("Lista intercalada:", resultado)