print("-=-"*10)
print("JOGO NA MEGA SENA")
print("-=-"*10)

from random import randint
from time import sleep

tot_jogo = int(input("Quntos jogos você quer que eu sorteie? "))

lista_jogos = []

for cont in range(0, tot_jogo):
  jogo_atual = []
  while len(jogo_atual) <= 6:
    num = randint(0, 60)
    if num not in jogo_atual:
      jogo_atual.append(num)

  jogo_atual.sort()
  lista_jogos.append(jogo_atual)

print(f"\n-=-=- SORTEANDO {tot_jogo} JOGOS -=-=-")
for i, l in enumerate(lista_jogos):
  print(f"Jogo {i+1}: {l}")
  sleep(0.5)

print("-=-=- < BOA SORTE! > -=-=-")