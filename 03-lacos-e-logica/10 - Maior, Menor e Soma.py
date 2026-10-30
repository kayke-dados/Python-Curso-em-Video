num_fim = 0
menor = 0
maior = 0
cont = 0
esc = ""
while esc in "Ss":
  num = int(input("Escolha um número: "))
  esc = str(input("Você deseja continuar[S/N]: "))
  cont += 1
  num_fim += num
  if cont == 1:
    menor = num
    maior = num
  elif num < menor:
    menor = num
  elif num > maior:
    maior = num
num_fim = num_fim / cont
print(f"Você digitou {cont} números e a media foi {num_fim}")
print(f"O maior número foi {maior} e o menor foi {menor}")