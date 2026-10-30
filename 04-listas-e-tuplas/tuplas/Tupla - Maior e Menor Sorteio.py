from random import randint
numeros = 0
n = (randint(1, 9), randint(1, 9), randint(1, 9), 
     randint(1, 9), randint(1, 9))
print("Os valores sorteados foram: ", end=' ')
print(f"{n}")

maior = n[1]
menor = n[1]
  
for i in range(1, 5):
  if n[i] > maior:
    maior = n[i]
  if n[i] < menor:
    menor = n[i]

print(f"O maior valor sorteado foi {maior}")
print(f"O menor valor sorteado foi {menor}")