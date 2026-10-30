ano = int(input("Em que ano você nasceu: "))

idade = (2026 - ano)

if idade <= 9:
  print("Você e estudante MIRIM!")
elif 10 <= idade <= 14:
  print("Você e estudante INFANTIL!")
elif 15 <= idade <= 19:
  print("Você e estudante JÚNIOR!")
elif 20 <= idade <= 25:
  print("Você e estudante SÊNIOR!")
elif idade <= 26:
  print("Você e estudante MASTER!")

print("--Fim do Codigo--")
print("   ")