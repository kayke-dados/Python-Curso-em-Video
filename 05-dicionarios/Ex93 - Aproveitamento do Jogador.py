from random import randint


jogador = {}
partidas = []


jogador['nome'] = str(input("Nome do jogador: "))
tot = int(input(f"Quantas partidas {jogador['nome']} jogou? "))


for c in range(0, tot):
    gols_jogo = randint(0, 5)
    print(f"   Na partida {c + 1}, fez {gols_jogo} gols.")
    partidas.append(gols_jogo)

  
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)


print("-=" * 30)
print(jogador)
print("-=" * 30)


print(f"O jogador {jogador['nome']} jogou {tot} partidas.")
for i, v in enumerate(jogador['gols']):
    print(f"   => Na partida {i + 1}, fez {v} gols.")
print(f"Foi um total de {jogador['total']} gols.")
