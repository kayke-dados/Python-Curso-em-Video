while True:
  dist = float(input("Qual a distancia da viagem: "))
  if dist <= 200:
    din = dist*0.5
    print(f"A passagem da sua viagem custara R${din}")
  else:
    din = dist*0.45
    print(f"A passagem da sua viagem custara R${din}")
  print("--Fim do Codigo--")
  print(" ")