matriz = [[], [], []]
par = 0
soma_colu_ter = 0

for hori in range(0, 3):
    for vert in range(0, 3):
        n = int(input(f"Digite um valor para [{hori}, {vert}]: "))
        matriz[hori].append(n)
        if n % 2 == 0:
            par += n
      
print("-=-" * 15)
for hori in range(0, 3):
    for vert in range(0, 3):
        print(f"[{matriz[hori][vert]:^5}]", end="")
    print()
print("-=-" * 15)

for colu in range(0, 3):
    soma_colu_ter += matriz[colu][2]

for linh in range(0, 3):
    if linh == 0:
        maior = matriz[1][linh]
    else:
        if matriz[1][linh] > maior:
          maior = matriz[1][linh]

print()
print(f"A soma dos valores pares e igual a {par}")
print(f"A soma dos valores da terceira coluna e igual a {soma_colu_ter}")
print(f"O maior valor da segunda linha é {maior}")
print("-=-"*15)