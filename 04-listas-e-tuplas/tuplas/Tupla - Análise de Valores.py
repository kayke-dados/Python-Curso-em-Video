núm = (int(input("Digite um número: ")),
  int(input("Digite outro número: ")),
  int(input("Digite mais um número: ")),
  int(input("Digite o ultimo número: ")))

print(f"Você Digitou os valores {núm}")

print(f"O valor 9 apareceu {núm.count(9)}")
if 3 in núm:
  print(f"o valor 3 apareceu na {núm.index(3)+1}° posição")
else:
  print(f"Você não digitou o valor 3")
print(f"Os valores pares que vc digitou foram: ", end='')
for n in núm:
  if n % 2 == 0:
    print(n,  end='')
print()