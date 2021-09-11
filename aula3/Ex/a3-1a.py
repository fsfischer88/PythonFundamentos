# Exercício 1 - Aula Funcoes e Procedimentos
# Crie um sistemas de cadastro de produtos
# O sistema deve ter 4 funções
# 1 - Imprimir um cabeçalho
# utilizar a biblioteca os para limpar a tela
# 2 - Função que solicita os dados do produto
#  usar as funções input para solicitar nome, descrição e valor
#  salvar os dados em um dicionário
#  retornar o dicionário ao final da função
# 3 - Função de validação de dados
#  deve solicitar se o nome do produto maior que 5 caracteres
#  validar se valor maior que zero
# 4 - Imprimir um rodapé e os dados do produto cadastrado

import os


def imprimir_cabecalho():
    os.system('clear')
    print('*'*10,"Cadastrar Produtos",'*'*10)
    print('\n')

def cadastrar_produtos():
    produtos = {}
    valido = False
    while(not valido):
        nome = input('Digite o nome do produto: ')
        if(not len(nome) > 5):
            print('O nome do produto precisa conter mais de 5 letras')
         
        else:
            valido = True
            produtos.update({'nome': nome})

    valido = False
    desc = input('Digite a descrição do produto: ')
    produtos.update({'descrição': desc})
   
    while(not valido):
        valor = float(input('digite seu valor: '))
        if(not valor > 0):
            print('O valor precisa ser maior que ZERO')
        else:
            valido = True
            produtos.update({'valor': valor})
        return produtos
   
def imprimir_rodape(produtos):
    print('Produto cadastrado com sucesso')
    print('\t', produtos['nome'], produtos['descrição'], produtos['valor'])

imprimir_cabecalho()
p = cadastrar_produtos


  



