while True:
  n = int(input("Você que ver a Tabuada de que número: "))
  if n < 0:
    print("PROGRAMA TABUADA ENCERRADO. Volte sempre")
    break
  print("="*15)
  for i in range(0, 11):
    print(f"{n} x {i} = {n*i}")
  print("="*15)