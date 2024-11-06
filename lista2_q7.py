L = [5,7,8,9,51,3,6,45,25,14]
p = int(input("Digite o número"))
for i in L:
    if i == p:
        print("Esse valor pertence à lista")
        break
    else:
        print("Elemento não encontrado")