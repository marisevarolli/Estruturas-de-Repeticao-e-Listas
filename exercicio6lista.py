notas = []
media=[]
alunosup = 0

for i in range(10):
    print(f"Notas do aluno {i+1}:")
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    nota4 = float(input("Digite a quarta nota: "))   
    notas.append([nota1,nota2,nota3,nota4])
    mediaaluno = (nota1 + nota2 + nota3 + nota4 ) / 4
    media.append(mediaaluno)

    if mediaaluno >= 7.0:
        alunosup += 1

print(f"Número de alunos co média maior ou igual a 7.0: {alunosup}")        