num = int(input())
soma = 0
for i in range(1,num):
  if num % i == 0:
    soma += i
if soma == num:
  print(f"É um número perfeito!")
else:
  print(f"Não é um número perfeito...")