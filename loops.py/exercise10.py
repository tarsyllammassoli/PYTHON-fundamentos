empregado = 0
desempregado = 0

for habitantes in range(10):
    cidade = input("Você está empregado? (S = SIM | N = NÃO): ").upper()
    if cidade ==  'S':
        empregado += 1
    elif cidade == 'N':
        desempregado += 1
    else:
        print("Houve algum erro de digitação. Tente novamente.")

print(f"Há {empregado} Empregados e {desempregado} Desempregados nesta cidade.")

# tay, tomar cuidado na hora de somar, string não soma com int, float e afins.