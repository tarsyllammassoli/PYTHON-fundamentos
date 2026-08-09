#Exercicio 1: Calculo de Bonus de Vendas (RH/Vendas) 
#Cenario: Uma empresa decidiu dar um bonus de 10% sobre o faturamento total para a 
#equipe de vendas. Objetivo: Calcule o valor do bonus e o faturamento final da empresa 
#apos subtrair esse bonus. 
# Faturamento inicial: 50.000 
# Percentual de bonus: 0.10

fat_inicial = 50000
percentual_bonus = 0.10

bonus = fat_inicial * percentual_bonus
faturamento_final = fat_inicial - bonus
print("Bônus: ", bonus)
print("Faturamento final: ", faturamento_final)

#Exercício 2: Controle de Estoque de E-commerce (Logística) 
#Cenário: Um e-commerce começou o dia com 250 unidades de um smartphone no 
#estoque. Durante o dia, foram vendidos 78 unidades e chegaram mais 100 unidades de um 
#fornecedor. Objetivo: Atualize a variável de estoque e exiba o saldo final.

Inicial = 250
Vendas = 78
Chegou = 100
total_sobrado = Inicial - Vendas
total_final = total_sobrado + Chegou

print(f"Total que restou durante o dia após as vendas: {total_sobrado}")
print(f"Total após repor o estoque no final do dia: {total_final}")

#Exercício 3: Divisão de Cargas (Logística/Transporte) 
#Cenário: Uma transportadora precisa levar 1.250 caixas em caminhões pequenos. Cada 
#caminhão suporta exatamente 12 caixas. Objetivo: 1. Quantos caminhões sairão 
#totalmente cheios? (Use //) 2. Quantas caixas sobrarão para serem enviadas em uma 
#última viagem menor? (Use %)

caminhoes_cheios = 1250//12 
sobras = 1250 % 12
print("Quantas caixas sobrarão: ", sobras)
print("Total de caminhões cheios: ", caminhoes_cheios)

#Exercício 4: Análise de Margem de Lucro (Financeiro) 
#Cenário: Uma consultoria faturou R$ 15.000,00 em um projeto. Os custos fixos foram de R$ 
#5.000,00 e o imposto sobre o faturamento é de 15%. Objetivo: Calcule o imposto, o lucro 
#líquido e a margem de lucro (Lucro / Faturamento). No final, crie uma variável booleana 
#chamada meta_atingida que verifica se a margem de lucro é superior a 0.30 (30%).

C_faturamento = 15000
C_fixos = 5000
imposto = C_faturamento % 0.15
Lucro_liquido = C_fixos - imposto
margem = Lucro_liquido / C_faturamento
meta_atingida = margem > 0.30
print(f"O lucro liquido foi de: {Lucro_liquido:.2f}")
print(f"A margem foi de: {margem:.2f}")
print(f"A meta atingida foi: {meta_atingida}")

#Exercício 5: Conversão de Tempo de Contrato (Gestão de Projetos) 
#Cenário: Um contrato de manutenção de software tem a duração de 40 meses. O cliente 
#quer ver esse tempo no formato: "X anos e Y meses". Objetivo: Utilize os operadores de 
#divisão inteira e resto da divisão para converter os 40 meses.

# lista compras

print("-"*20,"Lista","-"*20)
lista_compras = []
while True:
    compras = input(f"\t\nOpções:\t\n1 - Mostrar lista\t\n2 - Mostrar quantos produtos existem na lista\t\n3 - Adicionar produto\t\n4 - Remover produto\t\n5 - Finalizar lista\t\n")

    if compras == '1':
        print(f'\t\n{lista_compras}')

    elif compras == '2':
        print(f'\t\nSeu carrinho tem {len(lista_compras)} produtos.')

    elif compras == '3':
        add = input(f"\t\nDigite o nome do produto: ")
        lista_compras.append(add)

    elif compras == '4':
        remover = input(f'\t\nDigite o nome do produto: ')
        if remover in lista_compras:
            lista_compras.remove(remover)

    elif compras == '5':
        print(f'\t\nObrigada por comprar conosco.')
        break

# numeros pares

numeros1 = [3,8,11,20,7,14,18,13,54,39]

for numero in numeros1:
    if numero % 2 == 0:
        print(numero, end=" ")

# maior e menor

numeros2 = [9,34,16,20,7,14,18,87,54,90]

maior = numeros2[0]

for numero in numeros2:
    if numero > maior:
        maior = numero

print(f"\t\nMaior: {maior}")

menor = numeros2[0]

for numero in numeros2:
    if numero < menor:
        menor = numero

print(f"\t\nMenor: {menor}")

soma = 0

for numero in numeros2:
    soma += numero

print(f"\t\nSoma: {soma}")

media = soma / len(numeros2)
print(f"\t\nMéda: {media}")

# Cadastro de Produto

produto = {
    "nome": "Teclado",
    "preco": 150.00,
    "estoque": 10
}

print(produto["nome"])
print(produto["preco"])
print(produto["estoque"])
produto["preco"] = 180.50
produto["categoria"] = ("Periféricos","Entrada")
print(produto)

# Boletim

aluno = {
    "nome": "Ana",
    "notas": [3,7,9]
}

print(aluno)

soma = 0
for nota in aluno["notas"]:
    soma += nota

media = soma / len(aluno["notas"])

aluno["media"] = media

if aluno["media"] >= 7:
    print("Aprovado(a)")

elif aluno["media"] >= 5 and aluno["media"] < 7:
    print("Recuperação")

elif aluno["media"] < 5:
    print("Reprovado(a)")

# Cadastro de Produtos

produtos = [
    {"nome": "Teclado", "preco": 150, "estoque": 60},
    {"nome": "Mouse", "preco": 70, "estoque": 42},
    {"nome": "Monitor", "preco": 180, "estoque": 12}
]

print(produtos)
for i in produtos:
    if i["preco"] > 100:
        print(f"Maior que 100: ", i["nome"])

for i in produtos:
    if i["estoque"] < 15:
        print(f"Menor que 15 no estoque: ", i["nome"])

maior_valor_estoque = 0

for i in produtos:
    valor_total = i["preco"] * i["estoque"]
    print(i["nome"], "-> R$ ", valor_total)
    
for i in produtos:
    valor_total = i["preco"] * i["estoque"]
    if valor_total > maior_valor_estoque:
        maior_valor_estoque = valor_total
        print(f"Produto com maior valor em estoque: {i["nome"]} R$ {maior_valor_estoque}")

# Sistema Simples Estoque

itens = [
    {"nome": "Rímel YSL","preco": 390, "estoque": 50},
    {"nome": "Blush Aurora YSL","preco": 450, "estoque": 20},
    {"nome": "Corretivo Rare Beauty","preco": 200, "estoque": 87}
]

while True:
    ask = input(f"\t\n1 - Ver produtos\t\n2 - Adicionar estoque\t\n3 - Remover estoque\t\n4 - Ver valor total do estoque\t\n5 - Sair\t\n")

    if ask == '1':
        print(itens)

    elif ask == '2':
        add_item = input(f"\t\nDigite o nome do produto: ")

        for item in itens:
            if item["nome"] == add_item:
                quantidade = int(input(f"\t\nDigite a quantidade que deseja: "))
                item["estoque"] += quantidade

    elif ask == '3':
        remove_item = input(f"Digite o nome do item: ")
        itens.remove(remove_item)

    elif ask == '4':
        print(itens)
    
    elif ask == '5':
        print("Você está saindo do Sistema.")
        break
            
anos = 40 // 12
print(f"Total Anos: {anos}")
meses = 40 % 12
print(f"Total Meses: {meses}")
print(f"{anos} anos e {meses} meses")
