jogador = {}
partidas = []
jogadores = []

while True:
    jogador.clear()
    partidas.clear()

    jogador['nome'] = str(input("Nome do jogador: ")).strip()
    tot = int(input(f"Quantas partidas {jogador['nome']} jogou? "))

    for c in range(0, tot):
        gols_jogo = int(input(f"   Quantos gols ele fez na partida {c + 1}: "))
        print(f"   Na partida {c + 1}, fez {gols_jogo} gols.")
        partidas.append(gols_jogo)

    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)

    jogadores.append(jogador.copy())

    esc = str(input("Deseja continuar [S/N]: ")).strip().upper()
    if esc == "N":
        break

print("-=" * 30)
print(f"{'cod':<4} {'nome':<15} {'gols':<15} {'total':<5}")
print("-" * 40)

for k, v in enumerate(jogadores):
    print(f"{k:<4} {v['nome']:<15} {str(v['gols']):<15} {v['total']:<5}")

print("-" * 40)
