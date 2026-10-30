numeros = []

while True:
  num = int(input("Digite um número: "))
  numeros.append(num)
  esc = str(input("Deseja continuar[S/N]: ")).strip()
  
  if esc in "Nn":
    break

  else:
    ...

numeros.sort(reverse=True)
quant = len(numeros)
print("-=-"*20)
print(f"Você digitou {quant} elementos")
print(f"Os valores em ordem decresente sãom {numeros}")
if 5 in numeros:
  print(f"O valor 5 faz parte da lista")
else:
  print(f"O valor 5 não faz parte da lista")
