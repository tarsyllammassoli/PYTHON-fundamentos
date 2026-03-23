massa = float(input("Digite quantos KG você tem: "))
altura = float(input("Digite sua altura em metros (ex.: 1.67): "))

IMC = massa / (altura**2)

print(f"Seu IMC é {IMC:.2f}")

if IMC < 18.5:
    print("Magreza")
elif 18.5 <= IMC < 25:
    print("Saudável")
elif 25 <= IMC < 30:
    print("Sobrepeso")
elif 30 <= IMC < 35:
    print("Obesidade Grau I")
elif 35 <= IMC < 40:
    print("Obesidade Grau II (Severa)")
else:
    print("Obesidade Grau III (Mórbida)")

# Prestar atenção quanto ao OR e AND