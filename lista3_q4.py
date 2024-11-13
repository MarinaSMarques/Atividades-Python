idades = [12, 17, 20, 15, 22, 30, 14, 18, 16, 25]

menores_de_18 = [idade for idade in idades if idade < 18]
maiores_ou_igual_18 = [idade for idade in idades if idade >= 18]

print("Idades menores que 18 anos:", menores_de_18)
print("Idades maiores ou iguais a 18 anos:", maiores_ou_igual_18)