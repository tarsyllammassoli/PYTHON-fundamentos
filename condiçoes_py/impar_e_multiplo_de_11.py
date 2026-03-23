n = int(input("Digite um número inteiro positivo: "))
quadrado = n ** 2
if quadrado % 2 == 1:
    print("É ímpar")
elif quadrado % 11 == 0:
    print("É múltiplo de 11.")
elif quadrado % 2 == 1 and quadrado % 11 == 0:
    print("É ímpar e múltiplo de 11")
else:
    print("Não é Ímpar ou Múltiplo de 11...")