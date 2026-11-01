from random import randint

def escolha(quant):
  if quant > 0:
    for vez in range(0, quant):
      n = randint(0, 9)
      print(f"{n}", end=' ')
      if vez == 0:
        maior = n
      else:
        if n > maior:
          maior = n
        else:
          ...
  else:
    maior = 0
  print(f"Foram informados {quant} valores ao todo.")
  print(f"O maior valor informado foi {maior}.")
  print('-=-'*15)


escolha(int(input("Digite um número: ")))