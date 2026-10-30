while True:
  velo = int(input("Qual a velovidade do veiculo"))
  if velo <= 80:
    print("Parabéns")
    print("Continue Dirigindo com segurança")
  else:
    print("VOCÊ TOMOU UMA MULTA")
    multa = (f"{(velo-80)*7}")
    print(f"O valor da multa sera de R${multa}!")