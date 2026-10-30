maior = 0
menor = 0
for p in range(1, 6):
  kg = float(input(f"Qual o peso da {p}° Pessoa: "))
  if p == 1:
    maior = kg
  else:
    if kg > maior:
      maior = kg
      
    if kg <= menor:
        menor = kg

print(f"O Maior Peso foi {maior}")
print(f"O Menor Peso foi {menor}")