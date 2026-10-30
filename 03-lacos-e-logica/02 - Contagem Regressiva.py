num = int(input("Em qual número vai comecar a contagem: "))
while num > 0:
  print(f"{num}", end=' ')
  print("..." if num > 1 else ' ', end=' ')
  num -= 1