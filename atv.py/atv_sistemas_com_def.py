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
        print(f"Produto não encontrado. 1")

buscar_produto(produtos5, "Mousepad")

def atualizar_estoque(produtos5, nome, quantidade):
    encontrado = False
    for produto in produtos5:
        if produto["nome"] == nome:
            encontrado = True
            produto["estoque"] += quantidade
            print(f"O estoque foi atualizado para {produto["estoque"]}.")
    if encontrado == False:
        print(f"Produto não encontrado. 2")

atualizar_estoque(produtos5, "Mouse", 45)

def remover_estoque(produto5, nome, quantidade):
    Encontrado = False
    Estoque = False
    for produto in produto5:
        if produto["nome"] == nome:
            Encontrado = True
            if quantidade <= produto["estoque"]:
                Estoque = True
                produto["estoque"] -= quantidade
                print(f'O estoque foi atualizado para {produto["estoque"]}.')
    if Encontrado == False:
        print(f'Produto não encontrado.')
    elif Estoque == False:
        print(f'Estoque insuficiente.')

remover_estoque(produtos5, "Mouse", 200)

alunos = [
    {"nome": "Ana", "nota": 8},
    {"nome": "Carlos", "nota": 5},
    {"nome": "Julia", "nota": 9},
    {"nome": "Pedro", "nota": 6},
    {"nome": "Marina", "nota": 7}
]

def analisar_alunos(alunos):
    aprovados = []
    recuperacao = []
    reprovados = []
    for aluno in alunos:
        if aluno['nota'] >= 7.0:
            aprovados.append(aluno['nome'])
        elif aluno['nota'] < 7.0 or aluno['nota'] > 5.0:
            recuperacao.append(aluno['nome'])
        else:
            reprovados.append(aluno['nome'])

    print(f'Aprovados: ')
    for nome in aprovados:
        print(nome)

    print(f'Recuperação: ')
    for nome in recuperacao:
        print(nome)

    print(f'Reprovados: ')
    for nome in reprovados:
        print(nome) 
        
    print(f'Total de Aprovados: {len(aprovados)}')

analisar_alunos(alunos)

produtos6 = [
    {"nome": "Teclado", "preco": 150},
    {"nome": "Mouse", "preco": 80},
    {"nome": "Monitor", "preco": 900},
    {"nome": "Headset", "preco": 250},
    {"nome": "Webcam", "preco": 180}
]

def produtos_acima_De_200(produtos6):
    produto_maior_200 = []
    for produto in produtos6:
        if produto['preco'] > 200:
            produto_maior_200.append(produto['nome'])
    return produto_maior_200

resultado = produtos_acima_De_200(produtos6)
print(resultado)

categorias = ("Eletrônicos", "Informática", "Periféricos", "Acessórios")

def mostrar_categorias(categorias):
    tipo_c = 1
    for categoria in categorias:
        print(tipo_c, '-', categoria)
        tipo_c += 1

mostrar_categorias(categorias)

theproduto = ("Notebook", 3500, 8) # tupla (!!!)

def mostrar_produto(theproduto):
    nome, preco, estoque = theproduto # Desempacotando e dando nome
    print('Nome: ', nome)
    print('Preço: ', preco)
    print('Estoque: ', estoque)

mostrar_produto(theproduto)

def obter_informacoes(theproduto):
    nome, preco, estoque = theproduto # Desempacota... normal
    return nome, preco 

nome, preco = obter_informacoes(theproduto) # A tupla precisa ser desempacotada de novo fora do DEF

print(nome)
print(preco)

notas = [
    ("Ana", 8),
    ("Carlos", 5),
    ("Julia", 9),
    ("Pedro", 6),
    ("Marina", 7)
]

def analisar_notas(notas): # refazer atividade... (!)
    soma = 0

    for aluno in notas:
        nome, nota = aluno
        soma += nota

    media_notas_alunos = soma / len(notas)

    return media_notas_alunos

media = analisar_notas(notas)
print(f'Média: {media}')

produtos_p = [
    ("Teclado", 150),
    ("Mouse", 80),
    ("Monitor", 900),
    ("Headset", 250),
    ("Webcam", 180)
]

def produtos_caros(produtos_p):
    lista = []
    for i in produtos_p:
        nome, preco = i
        if preco > 200:
            lista.append(nome)
    return lista

lista_perifericos = produtos_caros(produtos_p)
print(f'Maior de 200R$: ', lista_perifericos)