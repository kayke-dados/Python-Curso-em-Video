while True:
  preco = float(input("Preço do produto: R$"))
  des = float(input("Quanto de desconto: "))
  if des <= 9:
    print(f"R${preco} com {des}% de desconto, ficara {preco-(preco*des/10)}")
  else:
    print(f"R${preco} com {des}% de desconto, ficara {preco-(preco*des/100)}")