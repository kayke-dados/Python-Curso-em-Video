def leiaInt(msg):
  ok = False
  valor = 0

  while True:
    num = (input(msg))
    
    if num.isnumeric():
      valor = int(num)
      return valor
    else:
      print("ERRO!, Digite um número inteiro, porfavor")


numero = leiaInt("Digite um número inteiro: ")
print(f"Você acabou de digitar o número {numero}")