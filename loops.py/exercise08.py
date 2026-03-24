while True:
    n_inferior = int(input("Digite o número inteiro positivo inicial: "))
    n_superior = int(input("Digite o número inteiro positivo final (deve ser maior que o inicial): "))

    while n_superior < n_inferior:
        print("O número deve ser maior que o inicial!, tente novamente...\n")
        n_superior = int(input("Digite o número inteiro positivo final (deve ser maior que o inicial): "))
    
    n = int(input("Agora, digite o último número (n >= 2): "))
    while n < 2:
        print("Tente novamente...")
        n = int(input("Agora, digite o último número (n >= 2): "))

    for i in range(n_inferior,n_superior + 1):
        if i % n == 0:
            print(i, end=" ")
    break