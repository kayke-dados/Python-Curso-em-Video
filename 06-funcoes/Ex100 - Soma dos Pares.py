from random import randint

def pares():
  lista = []
  print(f"Sorteando 5 valores da lista: ", end=' ')
  tot_par = 0
  for num in range(0, 5):
    n = randint(0, 9)
    if n % 2 == 0:
      tot_par += n
    lista.append(n)
  print("PRONTO!")
  print(f"Somando todos os valores pares da lista {lista} temos {tot_par}")


pares()