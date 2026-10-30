import random as rand
while True:
  computador = rand.randint(0, 5)
  print("Eu escolhi um numero de 0 ao 5 tente adivilha qual e ")
  num = int(input("Qual numero eu escolhi: "))
  if num == computador:
    print(f"Você acertou o numero que era {computador}")
  else:
    print(f"Você errou o numero, o numero era {computador}")
  print("--Fim do codigo--")
  print(" ")