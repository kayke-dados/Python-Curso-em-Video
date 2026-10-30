while True:
  soma = 0
  cont = 0
  for i in range(1, 7):
    num = int(input(f"Digite o {i}°: "))
    soma += num
    cont += 1
  print(f"A soma de todos e igual a {soma}")