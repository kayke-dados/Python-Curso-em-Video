from random import randint
while True:
  print("=====JOKENPO=====")
  print("[ 1 ] Pedra ")
  print("[ 2 ] Papel")
  print("[ 3 ] Tesoura")

  esc = int(input("Escolha: "))
  maq = randint(1, 3)

  if esc == 1:
    if maq == 2:
      print("Você PERDEU!, Você escolheu Pedra e a maquina Papel")
    if maq == 3:
      print("Você GANHOU!, Você escolheu Pedra e a maquina Tesoura")
    if maq == 1:
      print("O jogo EMPATOU!, Você escolheu Pedra e a maquina Também")

  if esc == 2:
    if maq == 3:
      print("Você PERDEU!, Você escolheu Papel e a maquina Tesoura")
    if maq == 1:
      print("Você GANHOU!, Você escolheu Papel e a maquina Pedra")
    if maq == 2:
      print("O jogo EMPATOU!, Você escolheu Papel e a maquina Também")

  if esc == 3:
    if maq == 1:
      print("Você PERDEU!, Você escolheu Tesoura e a maquina Pedra")
    if maq == 2:
      print("Você GANHOU!, Você escolheu Tesoura e a maquina Papel")
    if maq == 3:
      print("O jogo EMPATOU!, Você escolheu Tesoura e a maquina Também")

  print("   ")