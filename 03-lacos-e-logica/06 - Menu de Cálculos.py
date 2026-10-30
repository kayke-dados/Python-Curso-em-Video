while True:

  num1 = int(input("Escolha o primeio número: "))
  num2 = int(input("Escolha o segundo número: "))

  print("===================")
  print("[1] Somar")
  print("[2] Multiplicar")
  print("[3] Maior")
  print("[4] Novos números")
  print("[5] Sair do programa")

  esc = int(input("Oque você que fazer com esses dois números: "))

  if esc == 1:
    soma = num1 + num2
    print(f"O resultado de {num1} + {num2} = {soma}")
    print(" ")
  
  elif esc == 2:
    multi = num1 * num2
    print(f"O resultado de {num1} X {num2} = {multi}")
    print(" ")
    
  elif esc == 3:
    if num1 > num2:
      maior = num1
    else:
      maior = num2
    print(f"Entre {num1} é {num2} o maior número e {maior}")
    print(" ")

  elif esc == 4:
    print("Escolhas os novos números")
    print(" ")

  elif esc == 5:
    print("Finalizando... Pronto")
    break

  else:
    print("Erro, Tente Novamente.")
    print(" ")
  