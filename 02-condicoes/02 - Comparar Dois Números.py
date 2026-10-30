while True:
  n1 = float(input("Digite um numero: "))
  n2 = float(input("Digite um numero: "))

  if n1 > n2:
    print(f"O maior número e {n1}")
  if n2 > n1:
    print(f"O maior número e {n2}")
  if n1 == n2:
    print(f"Os dois números são IGUAIS")