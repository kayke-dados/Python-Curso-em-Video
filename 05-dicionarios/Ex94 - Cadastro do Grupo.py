pessoa = {}
pessoas = []
mulherlist = []
idade_tot = 0

while True:
    pessoa.clear()
    pessoa['nome'] = str(input("Nome: ")).strip()
    

    while True:
        pessoa['sexo'] = str(input("Sexo [F/M]: ")).strip().upper()
        if pessoa['sexo'] in "FM":
            if pessoa['sexo'] == "F":
                mulherlist.append(pessoa['nome'])
            break
        print("ERRO! Por favor, digite apenas F ou M.")
        
    pessoa['idade'] = int(input("Idade: "))
    idade_tot += pessoa['idade']
    
    
    pessoas.append(pessoa.copy())
    

    while True:
        esc = str(input("Deseja continuar? [S/N]: ")).strip().upper()
        if esc in "SN":
            break
        print("ERRO! Por favor, digite apenas S ou N.")
        
    if esc == "N":
        break

cadastradas = len(pessoas)
idademedia = idade_tot / cadastradas

print("-=" * 30)
print(f"A) Ao todo temos {cadastradas} pessoas cadastradas.")
print(f"B) A média de idade é de {idademedia:.2f} anos.")
print(f"C) As mulheres cadastradas foram: {mulherlist}")
print("D) Lista das pessoas que estão acima da média:")

for p in pessoas:
    if p['idade'] >= idademedia:
        print(f"   -> Nome: {p['nome']}; Sexo: {p['sexo']}; Idade: {p['idade']}")

print("<< ENCERRADO >>")
