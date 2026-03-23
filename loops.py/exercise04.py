par = 0
while True:
  n = int(input(f"Digite um número inteiro positivo (digite 0 para parar): "))
  if n % 2 == 0:
    par += n
  if n > 0:
    continue
  elif n == 0:
    break

if n % 2 == 0:
    par += n
print(f"A soma dos pares é: {par}")