print("-=-"*10)
print("LOJA SUPER BARATÃO")
print("-=-"*10)

cont = 0
menor_str = ""
menor = 0
maior = 0
total = 0

while True:
  produto = str(input("Nome do produto: "))
  preco = int(input("Preço: "))
  esc = str(input("Deseja continuar[S/N]: ")).strip().upper()
  cont += 1
  total += preco
  if preco >= 1000:
    maior += 1
    
  if esc == "S":
    if cont == 1:
      menor = preco
      menor_str = produto

    else:
      if menor > preco:
        menor = preco
        menor_str = produto

  if esc == "N":
    if menor == 0:
      menor = preco
    break
      
print("="*5, "FIM DO PROGRAMA", "="*5)
print(f"O total da compra deu R${total}.")
print(f"Temos {maior} produtos que custa acima de R$1000.")
print(f"O produto mais barato custou {menor} é e a {menor_str}")