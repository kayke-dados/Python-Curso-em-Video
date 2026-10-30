numeros = []
pares = []
impares = []

while True:
  num = int(input("Digite um número: "))
  numeros.append(num)
  if num % 2 == 0:
    pares.append(num)
  else:
    impares.append(num)
    
  esc = str(input("Deseja continuar[S/N]: ")).strip()
  
  if esc in "Nn":
    break
  else:
    ...

print("-=-"*15)
print(f"A lista completa e {numeros}")
print(f"Os números pares são {pares}")
print(f"Os números impares sao {impares}")
print("-=-"*15)