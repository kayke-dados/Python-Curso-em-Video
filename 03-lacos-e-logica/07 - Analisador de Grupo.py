nomevelho = ""
velhoano = 0
mulher20 = 0
idadefinal = 0
for i in range(1, 6):
  print(f"======={i}°=======")
  nome = input("Nome: ")
  idade = int(input("Idade: "))
  gen = str(input("Genero[F/M]: "))
  kg = float(input("Peso: "))

#Media Idade#
  idadefinal = idade + idadefinal

#Pessoas Mais Velha#
  if i == 1 and gen in "Mm":
    velhoano = idade
    nomevelho = nome

  if gen in "Mm" and  idade > velhoano:
    velhoano = idade
    nomevelho = nome
    
#Mulheres com menos de 20#
  if gen in "Ff" and idade <= 20:
    mulher20 = 1 + mulher20

#Media Resultado#
idadefinal = idadefinal/5

print(f"A media de idade das Pessoas e {idadefinal} Anos")
print(f"O Homem mais velho tem {velhoano} e o {nomevelho}")
print(f"Tem {mulher20} tem menos de 20 Anos")