from random import randint
resul_fim = ""
cont = 0
ip = 0
while True:
  print("-=-"*7)
  print(" ")
  print("JOGO DO IMPAR OU PAR")
  print(" ")
  print("-=-"*7)
  
  computador = randint(0, 100)
  
  player = int(input("Qual número você quer: "))
  esc = str(input("Você quer Impar ou Par[I/P]")).strip().upper()
  if esc == "I":
    esc = 1
    print("legal")
  else:
    esc = 2

  soma = player + computador
  resul = soma % 2
  
  if resul == 1:
    resul_fim = 1
    painel = "IMPAR"
  else:
    resul_fim = 2
    painel = "PAR"

  print("-"*20)
  print(f"Você escolheu {player} e o computador {computador}. Total de {soma} DEU {painel}")
  print("-"*20)
  
  if resul_fim == esc:
    print("Você VENCEU!")
    cont += 1
    print("Vamos jogar novamente...")
    print("-=-"*7)
  else:
    print("Você PERDEU")
    if cont == 1:
      print(f"GAME OVER, você ganhou {cont} vez")
    else:
      print(f"GAME OVER, você ganhou {cont} vezes")
    break