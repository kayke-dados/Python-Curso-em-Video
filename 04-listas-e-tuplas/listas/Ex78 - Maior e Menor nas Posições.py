lista = []
posimenor = []
posimaior = []

for p in range(0, 5):
  valor = int(input(f"Digite o valor na posição {p}: "))
  lista.append(valor)
  if p == 0:
    maior = valor
    menor = valor
  else:
    if valor < menor or valor == menor:
      menor = valor
    if valor > maior or valor == maior:
      maior = valor

for i, v in enumerate(lista):
  if v == menor:
    posimenor.append(i)
  if v == maior:
    posimaior.append(i)
    
print("-=-"*10)
print(f"Você digitou os valores {lista}")
print(f"O maior valor digitado foi {maior} nas posições {posimaior}")
print(f"O menor valor digitado foi {menor} nas posições {posimenor}")
print("-=-"*10)