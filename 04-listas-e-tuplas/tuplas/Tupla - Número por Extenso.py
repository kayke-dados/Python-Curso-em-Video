cont = ("zero", "um", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", 
        "onze", "doze", "treze", "cartoze", "quinze", "dzessete", 
        "dezoito", "dezenove", "vinte")

while True:
  num = int(input("Digite um número entre 0 e 20: "))
  if 0 <= num <= 20:
    break
  print("Tente novamente. ")
print(f"Você digitou o número {cont[num-1]}")