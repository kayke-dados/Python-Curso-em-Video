num = int(input("Escolha o número para calcular o Fatorial: "))
print(f"Calculando {num}! = ", end=' ')

n = num
f = 1
f = f * num

while n > 1:
  print(f"{n}", end=' ')
  print(" x " if n > 1 else ' = ', end=' ' )
  n -= 1
  f = f * n
print(f"{n} = {f}")