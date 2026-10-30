maiores = 0
homens = 0
mulheres = 0
esc = ""
while True:
  print("-=-"*10)
  print("CADASTRO")
  print("-=-"*10)
  
  idade = int(input("IDADE: "))
  sexo = str(input("SEXO[M/F]: ")).strip().upper()
  esc = str(input("Deseja continuar[N/S]: ")).strip().upper()
  
  if idade >= 18:
    maiores += 1
  if sexo == "M":
    homens += 1
  if idade <= 20 and sexo == "F":
    mulheres += 1

  if esc == "N":
    print(f"Teve um total de {maiores} pessoas com mais de 18 anos")
    print(f"Ao todo {homens} homens cadastrados")
    print(f"E {mulheres} com menos de 20 anos")
    break
