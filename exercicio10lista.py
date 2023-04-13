vetorA = []
vetorB = []
for i in range(10):
    num_A = int(input(f"Digite o {i+1}º elemento do vetor A:"))
    vetorA.append(num_A)
    num_B = int(input(f"Digite o {i+1}º elemento do vetor B:"))
    vetorB.append(num_B)

intercalado = []
for i in range(10):
    intercalado.append(vetorA[i])
    intercalado.append(vetorB[i])

print("Vetor A:", vetorA)
print("Vetor B:", vetorB)
print("Intercalada:", intercalado)