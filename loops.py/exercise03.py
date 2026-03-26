n = int(input("Digite um número inteiro positivo: "))
for i in range(n + 1):
    for j in range(1, i):
        print("*", end=" ")
    print()