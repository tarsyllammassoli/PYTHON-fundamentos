#try:
#    idade = int(input('Digite sua idade: '))
#    print(f'Idade cadastrada: {idade}')
#except ValueError:
#        print(f'Digite uma idade válida.')

# ------------------- iniciando exercicios/testes
while True:
    try:
        numero = int(input('Digite um número: '))
        if numero != ValueError or TypeError: # coloquei IF mas não precisa
            print(f'Número válido: {numero}')
            break
    except (ValueError,TypeError): # quando for mais de 1 tipo de erro, eu coloco entre parenteses com virg.
        print('Digite apenas números inteiros.')

while True:
    try:
        menu = input(' ===== MENU ===== \n1 - Ver produtos \n2 - Adicionar produto \n3 - Sair \n\t')
        if menu == '1':
            print('Você escolheu ver produtos.')
        elif menu == '2':
            print('Você escolheu adicionar produto.')
        elif menu == '3':
            print('Saindo...')
            break
        else:
            print('Opção inválida.')
    except ValueError:
        print('ERRO: Digite novamente.')

# ------------

produtos = []

def cadastrar_produto(produtos):
    nome_produto = input('Digite o nome do produto: ')
    while True:
        try:
            preco_produto = float(input('Digite o preço do produto: '))
            break
        except ValueError:
            print("Digite um preço válido.")
    while True:
        try:
            quantidade_produto = int(input('Digite a quantidade do produto: '))
            break
        except ValueError:
            print("Digite uma quantidade válida.")

    produtos_Dic = {
        "nome": nome_produto,
        "preco": preco_produto,
        "estoque": quantidade_produto
    }
        
    produtos.append(produtos_Dic)

cadastrar_produto(produtos)
print(produtos)

def adicionar_estoque(produtos, nome, quantidade):
    encontrado = False
    for produto in produtos:
        if produto["nome"] == nome:
            encontrado = True
            produto["estoque"] += quantidade
            print(f'Estoque atualizado: {produto["estoque"]}')

    if encontrado == False:
        print("Produto não encontrado.")

adicionar_estoque(produtos, "Mouse", 20)
print(produtos)