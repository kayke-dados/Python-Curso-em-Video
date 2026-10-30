from random import randint
computador = randint(0, 10)
print("Eu pensei em um número, Tente adivilha ele")
escolha = int(input("Qual número você acha que eu escolhi, de 0 a 10: "))
if escolha == computador:
  print("PARABÉNS, Você acertoi de primeira")
while not computador == escolha:
  print("Que pena você Errou")
  if escolha > computador:
    print(f"O meu número, e Menor que {escolha}.")
    escolha = int(input("Vai la e Tente novamente:"))
  elif escolha < computador:
    print(f"O meu número, e Maior que {escolha}.")
    escolha = int(input("Vai la e Tente novamente:"))

print(f"PARABÉNS, Você Acertou o numero que era {computador} ")