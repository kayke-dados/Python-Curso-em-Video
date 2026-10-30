def jogador(nome="<desconhecido>", gols=0):
  print(f"O jogador {nome} marcou {gols} gols")


print("-"*15)
n = str(input("Nome: "))
gol = str(input("Gols: "))

if gol.isnumeric():
  gol = int(gol)
else:
  gol = 0

if n.strip() == '':
  n = '<desconhecido>'

jogador(n, gol)