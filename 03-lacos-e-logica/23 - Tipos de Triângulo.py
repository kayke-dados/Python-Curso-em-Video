while True:
  n1 = float(input("Primeiro segmento"))
  n2 = float(input("Segunda segmento"))
  n3 = float(input("Terceira segmento"))
  

  if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    if n1 == n2 == n3:
      print("Os segmentos acima PODEM FORMAR um triângulo, EQUILATERO!")
    elif n1 == n2 or n1 == n3 or n3 == n2:
      print("Os segmentos acima PODEM FORMAR um triângulo, ISÓSCELES!")
    else:
      print("Os segmentos acima PODEM FORMAR um triângulo, ESCALENO!")
  else:
    print("Os segmentos acima NÃO PODEM FORMAR um triângulo! ")

  print("--Fim do Codigo--")
  print("   ")