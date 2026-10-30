while True:
  val = float(input("Qual o valor da casa: "))
  sal = float(input("Qual o seu salario: "))
  anos = int(input("Em quantos anos você ia pagar: "))

  #Variaves#
  meses = anos*12
  prest = val/meses
  salprest = sal*0.3

  #Condições#
  if prest > salprest:
    print("Emprestimo negado")
  elif prest < salprest:
    print("Emprestimo Sucedido")

  print("--Fim do Codigo--")
  print("   ")