print("GERADOR DE PA")
print("-=" * 15)

primeiro = int(input("Primeiro Termo: "))
razao = int(input("Razão do PA: "))

termo = primeiro
cont = 0
total = 10

while cont < total:
    print(termo, end=' -> ')
    termo += razao
    cont += 1

    if cont == total:
        mais = int(input("Quantos termos quer mostrar a mais? "))
        if mais == 0:
            print("ENCERRANDO PROGRAMA.")
        total += mais

print("FIM")