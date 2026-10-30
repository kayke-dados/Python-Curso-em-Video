from time import sleep


def contagem(ini, fim, pas):
  if fim < 0:
    fim = fim - 1
  else:
    fim = fim + 1
    print("-=-"*15)
    print(f"Contagem de {ini} até {fim} de {pas} em {pas}")
  for cont in range(ini, fim, pas):
    print(f"{cont}", end=' ')
    sleep(0.3)
  print("FIM!")

print("-=-"*15)
print("Contagem de 1 até 10 de 1 em 1")
for um in range(0, 10+1):
  sleep(0.3)
  print(f"{um}", "FIM!" if um == 10 else "", end=' ')
print()

print("-=-"*15)

print("Contagem de 10 até 0 de 2 em 2")
for dois in range(10, -1, -2):
  print(f"{dois}", "FIM!" if dois == 0 else "", end=' ')
  sleep(0.3)
print()

print("-=-"*15)

print("Agora é sua vez de personalizar a contagem!")
i = int(input("Início: "))
f = int(input("Fim: "))
p = int(input("Passo: "))

contagem(i, f, p)
