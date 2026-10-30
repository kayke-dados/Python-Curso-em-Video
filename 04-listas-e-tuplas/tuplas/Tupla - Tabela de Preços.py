lista = ("lapis", 1.75,
        "Borracha", 2,
        "Caderno", 15.99,
        "Estojo", 25,
        "Transferidor", 4.50,
        "Compasso", 9.99,
        "Mochila", 120.32,
        "Canetas", 22.30,
        "Livros", 34.40)
print("-"*20)
print("LISTAGEM DE PREÇOS")
print("-"*20)
for item in range(0, len(lista)):
  if item % 2 == 0:
    print(f"{lista[item]:.<30}.", end='')
  else:
    print(f"R${lista[item]:>7.2f}")