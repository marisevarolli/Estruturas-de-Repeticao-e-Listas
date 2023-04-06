notas = [8, 9, 10, 2]
medianotas = 0.0

for i in range (0, len(notas)):
    print ('nota', i+1, "=", notas[i])
    medianotas= medianotas+notas[i]
media=medianotas / len (notas)
print('Média:', media)