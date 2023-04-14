print ("Informe as seguintes informações-->")
nome=str(input("Digite seu nome: "))
while ( len(nome) <=  3 ):
	nome=str(input("Digite seu nome: "))


idade=int(input("Digite sua idade: "))
while ( idade > 150 or idade < 0 ):
	idade=int(input("Digite sua idade: "))
	

salario=float(input("Digite seu salário: "))
while ( salario < 0 ):
	salario=float(input("Digite seu salário: "))

sexo=str(input("Digite a inicial do seu sexo: "))
while  sexo !="f" and sexo!="m" :
	sexo=str(input("Digite a inicial do seu sexo: "))

estado_civil=str(input("Digite a inicial do seu estado civil: "))
while ( estado_civil != "s" and estado_civil != "c" and estado_civil != "v" and estado_civil != "d" ):
	estado_civil=str(input("Digite a inicial do seu estado civil: "))