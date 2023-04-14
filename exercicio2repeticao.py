print("Cadastre-se.")
usuario=str(input("Digite um nome de usuário: "))
senha=str(input("Digite sua senha: "))
while usuario==senha:
	print("A senha não pode ser igual o nome de usuário. Por favor, tente novamente:")
	usuario=str(input("Digite um nome de usuário:  "))
	senha=str(input("Digite sua senha: "))
else:
	print("Cadastro efetuado com sucesso.")