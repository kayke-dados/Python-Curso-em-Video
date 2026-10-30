alunos = []

while True:
    nome = str(input("Nome: "))
    n1 = float(input("1° Nota: "))
    n2 = float(input("2° Nota: "))

    aluno = []
    nota = []

    aluno.append(nome)
    nota.append(n1)
    nota.append(n2)
    aluno.append(nota)
    alunos.append(aluno)

    esc = input("Deseja continuar [S/N]: ").strip().upper()
    if esc == "N":
        break

print("-=-" * 15)
print(f"{'No.':<4}{'NOME':<10}{'MÉDIA':>8}")
print("-" * 26)

for vez in range(0, len(alunos)):
    media = (alunos[vez][1][0] + alunos[vez][1][1]) / 2
    print(f"{vez:<4}{alunos[vez][0]:<10}{media:>8.1f}")

while True:
    print("-" * 35)
    opc = int(input("Mostrar notas de qual aluno? (999 interrompe): "))
    if opc == 999:
        print("FINALIZANDO...")
        break
    if 0 <= opc < len(alunos):
        print(f"Notas de {alunos[opc][0]} são {alunos[opc][1]}")
