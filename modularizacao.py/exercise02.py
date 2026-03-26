print("Fatoração")
def distancia(Px=0,Py=0,Qx=0,Qy=0):
    """
    Ajuda:
    Calculando distância a cada dois pontos
    """
    dist = ((Px - Qx)**2 + (Py - Qy)**2)**0.5
    return dist
for contador in range(1,101):
    print(f"\n\t Par {contador}º")

    Px = float(input(f"Digite o número do ponto Px: "))
    Py = float(input(f"Digite o número do ponto Py: "))
    Qx = float(input(f"Digite o número do ponto Qx: "))
    Qy = float(input(f"Digite o número do ponto Qy: "))

    print(f"\n\tDistância entre os pontos {Px},{Qx} e {Py},{Qy} = {distancia(Px,Qx,Py,Qy):.2f}")

    menu = input("Gostaria de parar? (S ou N): \n").upper()
    if menu == 'S':
        break