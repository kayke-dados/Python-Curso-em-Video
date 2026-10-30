def fatorial(n, show=False):
  """
  -> Calcula o Fatorial de um número.
  :parem n: O número a ser calculado.
  :param show: (opcional) Mostrar ou não a conta.
  :return: O valor do Fatorial de um número n.
  """
  valorfinal = 0
  if show == True:
    for fat in range(n, 0, -1):
      if fat == n:
        valorfinal = n
      else:
        valorfinal *= fat
      print(f"{fat}", f"= {valorfinal}" if fat == 1  else "x", end=' ')
  else:
    for fat in range(n, 0, -1):
      if fat == n:
        valorfinal = n
      else:
        valorfinal *= fat
    print(valorfinal)
    
fatorial(6, True)