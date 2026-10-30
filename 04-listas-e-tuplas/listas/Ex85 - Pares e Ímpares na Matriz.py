lista = []
impares = []
pares = []
lista.append(impares)
lista.append(pares)

for cont in range(1, 8):
  num =  int(input(f"Digite o {cont}° número: "))
  if num % 2 == 0:
    lista[1].append(num)
  else:
    lista[0].append(num)

lista[1].sort()
lista[0].sort()

print()
print("-=-"*10)
print(f"Os valores pares digitados foram {lista[1]}")
print(f"Os valores impares digitados foram {lista[0]}")
print("-=-"*10)