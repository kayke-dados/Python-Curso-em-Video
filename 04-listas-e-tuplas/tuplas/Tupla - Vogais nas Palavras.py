pala = ("Aprender", "Programar", "Linguagens", "Curso",
        "Gratis", "Estudar", "Praticar", "Trabalhar",
        "Mercado", "Programador", "Futuro")
for palavras in pala:
  print(f"Na palavra {palavras} temos", end=" ")
  for letras in palavras:
    if letras.lower() in "aeiou":
      print(f"{letras.upper()}", end=' ')
  print()