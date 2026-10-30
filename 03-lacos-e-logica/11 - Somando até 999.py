esc1 = 0
cont = 0
num = 0
while num != 999:
  esc = int(input("Digite um número [999 Para parar]: "))
  if esc == 999:
    num +=999
  else:
    esc1 += esc
  cont += 1
print(f"Você digitou {cont-1} números e a soma entre eles foi {esc1}")