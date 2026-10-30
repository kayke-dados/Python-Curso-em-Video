while True:
  qnt = int(input("Quantas notas são: "))
  if qnt == 2:
    nt = float(input("Digite a primeira nota: "))
    nt2 = float(input("Digite a Segunda nota: "))
    print(f"A media e {(nt+nt2)/2}")
  elif qnt == 3:
    nt = float(input("Digite a primeira nota: "))
    nt2 = float(input("Digite a segunda nota: "))
    nt3 = float(input("Digite a terceira nota: "))
    print(f"A media e {(nt+nt2+nt3)/3}")
  else:
    print("Erro tentenovamente")