numeros = []
while True:
  num = int(input("Digite um número: "))
  if num not in numeros:
    numeros.append(num)
    print("Novo número adicionado!")
    
  else:
    print("Número Duplicado, Valor não adicionado!")
  esc = input("Você deseja continuar[S/N]").strip()
  if esc in "Ss":
    ...
  else:
    break

numeros.sort()

print("-=-"*30)
print(f"Você digitou os numeros {numeros}")
print("-=-"*30)