N = int(input("Digite um número inteiro positivo: "))
for i in range(2,N + 1):
  primo = True
  for j in range(2, i):
    if i % j == 0:
      primo = False
      break
  if primo:
    print(i, end=" ")