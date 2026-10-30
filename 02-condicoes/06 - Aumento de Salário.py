while True:
  sal = float(input("Qual o seu salario atual: R$"))
  if sal > 1250:
    saln = {sal*1.10}
    print(f"O seu novo salario sera {saln}")
  else:
    saln = {sal*1.15}
    print(f"O seu novo salario sera {saln}")

  print("--Fim do Codigo--")
  print("   ")
    