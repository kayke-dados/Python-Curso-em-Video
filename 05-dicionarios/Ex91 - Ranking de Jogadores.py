from random import randint
from time import sleep
from operator import itemgetter

jogo = {"Jogador1":randint(0, 10),
          "Jogador2":randint(0,10),
          "Jogador3":randint(0, 10),
          "Jogador4":randint(0, 10)}

print("Valores Sorteados")
rank = dict()
for k, v in jogo.items():
  print(f"O {k} tirou {v} nos dados")
  sleep(0.5)
rank = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print("=====<QUALIFICAÇÃO>=====")
for k, v in enumerate(rank):
  print(f"O {k+1}° Lugar: {v[0]} com {v[1]}")
  