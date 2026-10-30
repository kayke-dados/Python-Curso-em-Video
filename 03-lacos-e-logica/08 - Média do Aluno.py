while True:
  nt1 = float(input("Primeira nota: "))
  nt2 = float(input("Segunda nota: "))

  ntf = (nt1 + nt2) / 2
  if ntf <= 4.9:
    print("Você esta REPROVADO!")
  if 5 <= ntf <= 6.9:
    print("Você esta de RECUPERAÇÃO!")
  if ntf >= 7:
    print(" Você foi APROVADO!")
  print("--Fim do Codigo--")
  print("   ")