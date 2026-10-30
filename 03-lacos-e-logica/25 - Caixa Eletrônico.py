print("-=-" * 10)
print("BANCO CEV")
print("-=-" * 10)

valor = int(input("Quanto você quer sacar: R$"))

total = valor
ced_cinq = 0
ced_dez = 0
ced_um = 0

if total >= 50:
    ced_cinq = total // 50
    total = total % 50
if total >= 10:
    ced_dez = total // 10
    total = total % 10
if total >= 1:
    ced_um = total // 1
    total = total % 1

print(f"Total de {ced_cinq} cédulas de R$50")
print(f"Total de {ced_dez} cédulas de R$10")
print(f"Total de {ced_um} cédulas de R$1")