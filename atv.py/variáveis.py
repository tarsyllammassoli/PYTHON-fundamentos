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

anos = 40 // 12
print(f"Total Anos: {anos}")
meses = 40 % 12
print(f"Total Meses: {meses}")
print(f"{anos} anos e {meses} meses")