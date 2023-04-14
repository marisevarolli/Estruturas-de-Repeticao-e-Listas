populaçãoA=float(input("Digite a população do país A "))
populaçãoB=float(input("Digite a população do país B "))
ano=0
taxa_crescimentoA=float(input("Agora digite a taxa de crescimento da população do país A "))
taxa_crescimentoB=float(input("Agora digite a taxa de crescimento da população do país B "))
while populaçãoA < populaçãoB:
	populaçãoA+=round((populaçãoA*taxa_crescimentoA)/100)
	populaçãoB+=round((populaçãoB*taxa_crescimentoB)/100)
	ano=ano+1

print("Levará",ano,"anos para que a população do país A ultrapasse ou iguale a população do país B, mantida as taxas de crescimento")