def somar_listas(lista1, lista2):
    return [lista1[i] + lista2[i]
            for i in range(len(lista1))]

lista1 = [5, 7, 9]
lista2 = [3, 5, 8]
resultado = somar_listas(lista1, lista2)

print("A soma das listas é:", resultado)