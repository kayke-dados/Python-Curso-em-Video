pessoas = []
pessoa = []
maior_list = []
menor_list = []
cont = 0

while True:
  nome = str(input("Nome: "))
  peso = float(input("Peso: "))

  pessoa.append(nome)
  pessoa.append(peso)
  pessoas.append(pessoa[:])
  pessoa.clear()
  
  esc = str(input("Deseja continuar[S/N]: ")).strip().upper()

  if cont == 0:
    maior = peso
    menor = peso
  else:
    if peso > maior:
      maior = peso
    if peso < menor:
      menor = peso
  cont += 1
  if esc == "N":
    break

for p in pessoas:
  if p[1] == maior:
    maior_list.append(p[0])
  if p[1] == menor:
    menor_list.append(p[0])

cont_pessoas = len(pessoas)

print("-=-"*15)
print(f"Ao todo, Você cadastrou {cont_pessoas} pessoas")
print(f"O maior peso foi {maior}kg, peso de {maior_list}")
print(f"O menor peso foi {menor}kg, peso de {menor_list}")
print("-=-"*15)