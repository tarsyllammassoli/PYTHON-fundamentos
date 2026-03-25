salario_minimo = 1612.01
salario_com_superior = 0
salario_sem_superior = 0
for i in range(6):
    salario = float(input("Digite o seu salário (deve ser maior que 1612.01): "))
    while salario < salario_minimo:
        print("Valor Inválido\n")
        salario = float(input("Digite novamente: "))
    curso = input("Possui curso superior completo? (S - SIM / N - NÃO): ").upper()
    if curso == 'S':
        while salario > salario_com_superior:
            salario_com_superior = salario
    if curso == 'N':
        while salario > salario_sem_superior:
            salario_sem_superior = salario
print(f"Maior salário COM superior completo: {salario_com_superior}")
print(f"Maior salário SEM superior completo: {salario_sem_superior}")