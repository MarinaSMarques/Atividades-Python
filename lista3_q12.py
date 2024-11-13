def soma_distintos(lista):
    resultado = []

    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            soma = lista[i] + lista[j]
            if soma in lista and soma not in resultado:
                resultado.append(soma)

    return resultado

lista = [3, 5, 7, 10, 15]
resultado = soma_distintos(lista)
print("Soma dos números:", resultado)