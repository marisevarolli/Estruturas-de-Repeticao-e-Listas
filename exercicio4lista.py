letras = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')
vogais = ('a', 'e', 'i', 'o', 'u')
consoantes = ('b','c','d','f','g','h','j')

for i in letras:
    if i not in vogais:
        print(i)
x = len(consoantes)
print ("Número de consoantes:", x)