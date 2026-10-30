matriz = [[], [], []]

for hori in range(0, 3):
    for vert in range(0, 3):
        n = int(input(f"Digite um valor para [{hori}, {vert}]: "))
        matriz[hori].append(n)

print("-=-" * 15)
for hori in range(0, 3):
    for vert in range(0, 3):
        print(f"[{matriz[hori][vert]:^5}]", end="")
    print()
print("-=-" * 15)
