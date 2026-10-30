while True:
  peso = float(input("Qual o seu peso(KG): "))
  alt = float(input("Qual a sua altura: "))

  imc = peso/(alt*alt)

  if imc <= 18.5:
    print(f"Você esta em ABAIXO DO PESO!")
  elif 18.5 < imc <= 25:
    print(f"Você esta em PESO IDEAL!")
  elif 25 < imc <= 30:
    print(f"Você esta em SOBREPESO!")
  elif 30 < imc <= 40:
    print(f"Você esta em OBESIDADE!")
  elif 40 < imc:
    print(f"Você esta em OBESIDADE MÓRBIDA!")
  
  print("--Fim do Codigo--")
  print("   ")