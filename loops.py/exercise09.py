pares = 0
impares = 0
for i in range(999,99,-1):
    if i % 2 == 0:
        pares += i
    else:
        impares += i

print(f"Soma dos Pares: {pares}")
print(f"Soma dos ímpares: {impares}")