alunos = ['Ana','Carlos','João','Pedro','Maria'] #Pode ser alterada

#add = input(f'Remova um aluno a lista: ')
#alunos.remove(add)
#print(alunos)

notas = (8,4,9) #Não pode ser alterada
#print(notas)

aluno = {
    "Nome": "Ana",
    "Idade": 20,
    "Curso": "Engenharia de Software",
    "Semestre": 4
}

# del aluno["Idade"] # DELETAR

#print(aluno)

alunos = [
    {
        "Nome": "Ana",
        "Idade": 20,
        "Semestre": 5
    },
    {
        "Nome": "João",
        "Idade": 23,
        "Semestre": 7,
    }
]

#print(alunos)
#print(f"-"*20)
#print(alunos[0]["Nome"])

#for chave, valor in alunos[0].items(): # items() vai dar a chave junto do valor
    #print(chave,":", valor)

#for chave in alunos[1].keys(): # keys() da apenas a chave
    #print(chave)

#for valor in alunos[1].values(): # values() da apenas o valor
    #print(valor)

#for chave in alunos: # Da tudo que está no Dicionário
    #print(chave)

# ----------------------------------

produtos = [
    {
    "nome": "Blush",
    "preco": 99.90,
    "estoque": 45,
    "categorias": ("Maquiagens","Produto Feminino")
        },
        {
        "nome": "Barbeador",
        "preco": 37.90,
        "estoque": 81,
        "categorias": ("Higiene","Produto Masculino") 
    }
]

#print(produto["nome"])
#print(produtos["preco"])
#print(produto["categorias"][0])
#print(produto["categorias"][1])
#produto["estoque"] = 40
#print(produto["estoque"])
#produto["marca"] = "Ruby Rose"
#print(produto["marca"])

#for valor in produto.values():
    #print(valor)

#for produto in produtos:
    #print(produto["nome"],"- R$", produto["preco"])

#for produto in produtos:
    #print(produto["nome"], "R$", produto["preco"])
    #for categoria in produto["categorias"]:
        #print(categoria)

for produto in produtos:
    if produto["estoque"] > 50:
        print(produto["nome"], "- Estoque:", produto["estoque"])

for produto in produtos:
    if produto["nome"] == "Blush":
        produto["estoque"] = 30
        print(produto["nome"], produto["estoque"])

for produto in produtos:
    if produto["preco"] > 50:
        produto["preco"] = produto["preco"] * 0.90
        print(f"{produto["nome"]},- R$, {produto["preco"]:.2f}")