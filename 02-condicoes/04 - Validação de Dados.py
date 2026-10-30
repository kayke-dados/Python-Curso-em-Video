sexo = str(input("Qual o seu sexo[F/M]: ".strip().upper()[0]))
while sexo not in "MmFf":
  sexo = str(input("Dados invalidos. Por favor Informe seu Sexo[F/M]".strip().upper()[0]))
print(f"Sexo {sexo}, Registrado com sucesso.")