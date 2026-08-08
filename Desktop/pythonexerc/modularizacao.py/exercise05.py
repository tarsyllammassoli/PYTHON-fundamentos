import numpy as np

dataset = np.random.randint(1,101,10)
print('Dataset: ', dataset)

print('Primeiros 5:', dataset[:5])        # do índice 0 até 4
print('Últimos 5:', dataset[5:10])         # do índice 5 até 9
print('Do 3º até o fim:', dataset[2:])      # omitir o "fim" = vai até o final
print('De 2 em 2:', dataset[::2])           # passo 2 = pula um a um
print('Invertido:', dataset[::-1])          # passo -1 = de trás pra frente
print('Os 3 do meio:', dataset[3:6])



#---------------------------------------------------------------------------

np.random.randint(inicio, fim, passo) # gerar numero aleatorio
np.random.choice(vetor) # sorteia elemento aleatóro de dentro do vetor
np.arange(inicio,fim,passo) # cria um vetor em sequência, irmão do range()




# 1ª função: lê um vetor (array) de tamanho definido pelo usuário
def ler_vetor():
    tamanho = int(input('Quantos números o vetor terá? '))
    vetor = np.zeros(tamanho, dtype=int)  # cria vetor vazio (de zeros)
    for i in range(tamanho):
        vetor[i] = int(input(f'Digite o número {i+1}: '))
    return vetor

# 2ª função: lê UM número e retorna o fatorial dele
def calcular_fatorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado = resultado * i
    return resultado

# 3ª função: pega o vetor original e cria um NOVO vetor com o fatorial de cada elemento
def vetor_de_fatoriais(vetor):
    novo_vetor = np.zeros(len(vetor), dtype=int)
    for i in range(len(vetor)):
        novo_vetor[i] = calcular_fatorial(vetor[i])
    return novo_vetor

# 4ª função: exibe os vetores
def exibir_vetores(original, fatoriais):
    print('Vetor original:', original)
    print('Vetor de fatoriais:', fatoriais)

# Função de Fatorial !n ----------------------------------------------------------------------

def fatorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado = resultado * i
    return resultado

# Programa Principal --------------------------------------------------------------------------------------------

vetor_numeros = ler_vetor()
fatoriais = vetor_de_fatoriais(vetor_numeros)
exibir_vetores(vetor_numeros, fatoriais)