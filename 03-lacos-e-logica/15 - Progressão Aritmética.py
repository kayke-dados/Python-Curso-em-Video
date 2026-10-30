print("GERADOR DE PA")
print("-="*15)

primeiro = int(input("Primeiro Termo: "))
razao = int(input("Razão do PA: "))
cont = 0

prirazao = razao
while cont < 10:
  print(primeiro,end='-')
  print(f"{razao}", end='')
  print("" if cont > 8 else '...', end=' ' )
  cont += 1
  razao += prirazao
  primeiro += 1
  