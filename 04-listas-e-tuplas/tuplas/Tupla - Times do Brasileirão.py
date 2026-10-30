times = ("Corinthias", "Palmeiras", "Santos", "Grêmio", "Cruzeiro", 
        "Flamengo", "Vasco da Gama", "Chapecoense", "Atlético", "Botafogo", 
        "Atlético-PR", "Bahia", "São Paulo", "Fluminense", "Sport Recife", 
        "EC Vitória", "Coritiba", "Avaí", "Ponte Preta", "Atlético-GO")

print("-=-"*8)
print(f"Lista de times do brasileirão: {times}")
print("-=-"*8)
print(f"Os 5 primeiros times são {times[0:5]}")
print("-=-"*8)
print(f"Os 4 ultimos times são {times[-4:]}")
print("-=-"*8)
print(f"Times em ordem alfabetica: {sorted(times)}")
print("-=-"*8)
print(f"O Chapecoense está na {times.index('Chapecoense')+1}° posição")