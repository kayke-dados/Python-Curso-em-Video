#Puxa o modelo#
import random

#Deixa em loop#
while True:
  a1 = str(input("Primeiro aluno: "))
  a2 = str(input("Segundo aluno: "))
  a3 = str(input("Terceiro aluno: "))
  a4 = str(input("Quarto aluno: "))

  lista = [a1, a2, a3, a4]
#faz a emparalha#
  random.shuffle(lista)
  print(f"A ordem de apresentação sera:")
  print(lista)

print(f"Fim do codigo")