while True:
  compras = float(input("Preço das compras: R$"))

  print("FORMAS DE PAGAMENTO")
  print("[ 1 ] Á vista dinheiro/cheque")
  print("[ 2 ] Á vista no cartão")
  print("[ 3 ] 2x no cartão")
  print("[ 4 ] 3x ou mais no cartão")

  pag = int(input("Qual é a opção? "))

  vist = compras * 0.90
  card = compras * 0.95
  juros = compras * 0.20
  x = compras / 2

  if pag == 1:
    print(f"Sua compra de R${compras} vai custar R${vist} no final")
  elif pag == 2:
    print(f"Sua compra de R${compras} vai custar R${card} no final")
  elif pag == 3:
    print(f"Sua compra de R${compras} sera parcelada em 2x com parcelas de R${x}")
  elif pag == 4:
    parc = int(input("Você deseja parcelar em quantas vezes: "))
    parctotal = juros * parc
    valortotal = compras + parctotal
    print(f"Sua compra de R${compras} sera parcelada em {parc}x, com parcelas de R${valortotal}")
  else:
    print("Erro, Você escolheu uma forma de pagamento inexistente.")
  print("--Fim do Codigo--")
  print("   ")