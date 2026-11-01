def voto(ano):
  idade = 2026 - ano
  if idade <= 15:
    print("Você tem {idade} e ainda não pode votar")
  elif idade <= 17:
    print("Você tem {idade} e seu voto NÃO É OBRIGATORIO")
  else:
    print("Você tem {idade} e seu voto É OBRIGATORIO")


voto(int(input("Em que ano você nasceu: ")))