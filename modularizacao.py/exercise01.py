def distancia_dois_pontos(Px,Py,Qx,Qy):
    '''
    Ajuda da função "distância":
    Parâmetros: Coordernadas dos pontos P(Px,Py) e (Qx,Qy)
    '''
    dist = ((Px - Qx)**2 + (Py + Qy)**2)**0.5
    return dist

distancia = distancia_dois_pontos(3,0,0,4)
print(f"\n\tDistância entre os pontos P({3},{0}) e Q({0},{4}) = {distancia:.2f}")