notas = [7.5, 8.0, 9.0, 4.5, 6.0, 10.0, 5.0]
maior_nota = notas[0]
menor_nota = notas[0]

for nota in notas:
    if nota > maior_nota:
        maior_nota = nota
    if nota < menor_nota:
        menor_nota = nota

print("A maior nota é:", maior_nota)
print("A menor nota é:", menor_nota)