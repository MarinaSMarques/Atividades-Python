nomes = ["Ana", "Beatriz", "Carlos", "Daniel", "Eduarda", "Fabio"]
cont = 0

for nome in nomes:
    if len(nome) > 5:
        cont +=1

print("A quantidade de nomes que possui mais de 5 letras são:", cont)