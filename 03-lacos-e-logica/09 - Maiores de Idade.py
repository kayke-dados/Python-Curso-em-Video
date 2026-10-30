cont_menor = 0
cont_maior = 0

for pess in range(1, 8):
  ano = int(input("Em que Ano a Pessoa Nasceu: "))
  idade = 2026 - ano

  if idade >= 18:
    cont_maior += 1

  else:
    cont_menor += 1

print(f"Existem {cont_maior} Maiores de idade, e {cont_menor} Menores de idade")