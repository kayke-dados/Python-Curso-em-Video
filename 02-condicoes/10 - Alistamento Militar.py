while True:
  ano = int(input("Em que ano vc nasceu: "))
  anon = 2026 - ano
  if anon >= 18:
    print("Você ja vez o alistamento militar")
  if anon == 17:
    print("Você precisa fazer o alistamento militar IMEDIATAMENTE!")
  if anon <= 16:
    print("Você ainda e muito jovem")
  print("--Fim do Codigo--")
  print("   ")