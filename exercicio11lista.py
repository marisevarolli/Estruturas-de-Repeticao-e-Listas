vetorA = []
vetorB = []
vetorC = []
for i in range(10):
    numA = int(input(f"Digite o {i+1}º elemento do vetor A:"))
    vetorA.append(numA)
    numB = int(input(f"Digite o {i+1}º elemento do vetor B:"))
    vetorB.append(numB)
    numC = int(input(f"Digite o {i+1}º elemento do vetor C:"))
    vetorC.append(numC)

intercalado = []
for i in range(10):
    intercalado.append(vetorA[i])
    intercalado.append(vetorB[i])
    intercalado.append(vetorC[i])

print("Vetor A:", vetorA)
print("Vetor B:", vetorB)
print("Vetor C:", vetorC)
print("Intercalada:", intercalado)