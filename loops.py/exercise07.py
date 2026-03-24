soma = 0
print(f"Múltiplos de 11 em ordem decrescente: \n")
for i in range(400,300,-1):
    if i % 11 == 0:
        soma += i
        print(i, end=" ")

print(f"\n\nSoma dos múltiplos de 11: {soma}")