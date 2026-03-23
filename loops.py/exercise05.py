while True:
  num = int(input("Digite um número inteiro positivo que seja maior que 5: "))
  if num >= 5:
    break
  else:
    print("Número inválido. Digite novamente!")

s = 0.0
for k in range(1,num + 1):
  s += 6/(k**2)

print(f"\n S = {s:.2f}")
