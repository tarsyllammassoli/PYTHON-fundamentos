def mostrar_numeros():
    numeros = [1,2,5,7,12]
    for numero in numeros:
        print(numero)
    return

def mostrar_pares(numeros):
   for numero in numeros:
       if numero % 2 == 0:
           print(numero)

mostrar_pares(numeros = [3, 8, 11, 20, 7, 14, 25, 30])

# ----------------------------------------------------------------------

produto1 = {
     "nome": "Notebook",
     "preco": 3500,
     "estoque": 5
}

def mostrar_produto(produto1):
    print("\t\nProduto:",produto1["nome"],
        "\nPreço:", produto1["preco"],
        "\nEstoque:", produto1["estoque"])

mostrar_produto(produto1)

def calcular_valor_estoque(produto):
    valor_total_estoque = produto["preco"] * produto["estoque"]
    return valor_total_estoque

valor = calcular_valor_estoque(produto1)

print("R$", valor)

# ---------------------------------------------------------------------

produtos = [
    {"nome": "Teclado", "preco": 150, "estoque": 10},
    {"nome": "Mouse", "preco": 80, "estoque": 5},
    {"nome": "Monitor", "preco": 900, "estoque": 3},
    {"nome": "Headset", "preco": 250, "estoque": 8}
]

def calcular_valor_total(produtos):
    acumulador = 0
    for produto in produtos:
        valortotal = produto["preco"] * produto["estoque"]
        acumulador += valortotal
        print(f"R$", valortotal)
    print(f"Soma total: {acumulador}")
    return

calcular_valor_total(produtos)

# -------------------------------------------------------------------

produtos2 = [
    {"nome": "Teclado", "preco": 150, "estoque": 10},
    {"nome": "Mouse", "preco": 80, "estoque": 5},
    {"nome": "Monitor", "preco": 900, "estoque": 3},
    {"nome": "Headset", "preco": 250, "estoque": 8},
    {"nome": "Webcam", "preco": 180, "estoque": 15}
]

def produtos_caros(produtos2):
    for produto in produtos2:
        if produto["preco"] > 200:
            print(produto["nome"], "-", produto["preco"])

produtos_caros(produtos2)

# -------------------------------------------------------------------

produtos3 = [
    {"nome": "Teclado", "preco": 150, "estoque": 10},
    {"nome": "Mouse", "preco": 80, "estoque": 5},
    {"nome": "Monitor", "preco": 900, "estoque": 3},
    {"nome": "Headset", "preco": 250, "estoque": 8},
    {"nome": "Webcam", "preco": 180, "estoque": 15}
]

def produtos_baixo_estoque(produtos3):
    for produto in produtos3:
        if produto["estoque"] < 10:
            print(produto["nome"], "-", produto["estoque"])

produtos_baixo_estoque(produtos3)

# ---------------------------------------------------------------------

produtos4 = [
    {"nome": "Teclado", "preco": 150},
    {"nome": "Mouse", "preco": 80},
    {"nome": "Monitor", "preco": 900},
    {"nome": "Headset", "preco": 250}
]

def aplicar_desconto(produtos4):
    for produto in produtos4:
        if produto["preco"] > 200:
            produto["preco"] = produto["preco"] * 0.90
            print(produto["nome"], "- R$", produto["preco"])

aplicar_desconto(produtos4)

# ---------------------------------------------------------------------

produtos5 = [
    {"nome": "Teclado", "preco": 150, "estoque": 10},
    {"nome": "Mouse", "preco": 80, "estoque": 5},
    {"nome": "Monitor", "preco": 900, "estoque": 3},
    {"nome": "Headset", "preco": 250, "estoque": 8}
]

def buscar_produto(produto5, nome):
    encontrado = False
    for produto in produto5:
        if produto["nome"] == nome:
            encontrado = True
            print(f"Produto: {produto['nome']}\nPreço: {produto['preco']}\nEstoque: {produto['estoque']}")
    if encontrado == False:
        print(f"Produto não encontrado.")

buscar_produto(produtos5, "Mousepad")