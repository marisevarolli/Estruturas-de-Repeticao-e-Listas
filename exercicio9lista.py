vetorA = []
for i in range(10):
    num = int(input(f"Digite o {i+1}º número inteiro:"))
    vetorA.append(num)

somadosquadrados = sum([num**2 for num in vetorA])

print("Vetor A:", vetorA)
print("Soma dos quadrados:", somadosquadrados)