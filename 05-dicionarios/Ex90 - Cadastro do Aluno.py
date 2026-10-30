aluno = {}

aluno['nome'] = str(input("Nome: "))
aluno['media']= float(input("Media: "))

if aluno['media'] <= 5:
  resultado = 'Reprovado'
elif aluno['media'] <= 7:
  resultado = 'Reculperação'
else:
  resultado = 'Aprovado'

print('-=-'*10)
print()
print(f"- O nome e igual a {aluno['nome']}")
print(f"- A media e igual a {aluno['media']}")
print(f"- A situação e de {resultado}")
print()
print('-=-'*10)