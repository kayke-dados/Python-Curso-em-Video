while True:
  print("-="*12)
  print("SEQUENCIA DE FIBONACCI")
  print("-="*12)
  termo = int(input("Quantos termos você quer mostrar: "))
  cont = 0
  ant = 1
  fab = 0
  print("="*18)
  while cont < termo:
    print(f"{fab}", end=' -> ' if cont < (termo-1) else '...FIM')
    prox = ant + fab 
    ant = fab
    fab = prox
    cont += 1
  print()
  print("="*18)