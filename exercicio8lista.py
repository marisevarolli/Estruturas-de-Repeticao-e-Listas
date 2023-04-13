i = 0
idade = []
altura = []

for i in range(5):
    print(f"Informações da pessoa {i+1}: ")
    id = int(input("Digite a idade: "))
    idade.append(id)
    alt = float(input("Digite a altura em cm: "))
    altura.append(alt)

idade.reverse()
altura.reverse()

print ("Idades inverso: ", idade)
print ("Alturas inverso: ", altura)