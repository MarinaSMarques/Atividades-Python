def digite_caracteres():
    print("Digite os caracteres da lista. Digite * para finalizar")
    while True:
        letra = input("Digite uma letra: ").upper()
        while (letra < "A" or letra > "Z" or len(letra) > 1) and (letra != "*"):
            print("Caractere digitado não é letra: %s" % letra)
            letra = input("Digite novamente uma letra: ").upper()
        if letra == "*":
            break
        else:
            l.append(letra)


def total_letras():
    cont_a = 0
    for i in range(len(l)):
        if l[i] == "A":
            cont_a += 1
    return cont_a


l = []
digite_caracteres()
total_letras()
print("Caracteres digitados: ", sorted(l))
print("Quantidade de letras 'A' digitadas: %d" % total_letras())
print("Quantidade de letras 'A' digitadas: %d" % l.count("A"))

