#Exercício Aula2 - 3 - Dicionários
#Crie um sistema de cadastro de produtos
#O sistema deve solicitar ao usuário que informe os seguintes dados:
# - Nome
# - Descrição
# - Categoria
# - Valor
# O sistema deve atender as seguintes regras:
# - Permitir casdastras produtos com valores maiores que zero;
# - O nome do produto deve ter mais de 3 letras;
# - A categoria deve possuir mais de 5 caracteres;
# - Todos os dados devem estar armazenados em um dicionário;


#Exemplo de como pegar a quantidade de letras de uma variável;
# nome = 'Cereveja Skol;
# len(nome)

import os
valido = False
produtos = {}

# - O nome do produto deve ter mais de 3 letras;
while(not valido):
    nome = input('digite o nome do produto: ')
    if(not len(nome) > 3):
        print('O nome do produto precisa conter mais de 3 letras')
        # if ternario no Python, se for == 'nt (windows) executa cls senão clear
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        valido = True
        produtos['nome'] = nome  # - Todos os dados devem estar armazenados em um dicionário;

produtos['descrição'] = input('digite a sua descrição: ')

valido = False
# - A categoria deve possuir mais de 5 caracteres;
while(not valido):
    categoria = input('digite a categoria do produto: ')
    if(not len(categoria) > 5):
        print('A categoria do produto precisa conter mais de 5 letras')
         # if ternario no Python, se for == 'nt (windows) executa cls senão clear
        os.system('cls' if os.name == 'nt' else 'clear')
       
    else:
        valido = True
        produtos['categoria'] = categoria  # - Todos os dados devem estar armazenados em um dicionário;

valido = False
# - Permitir casdastras produtos com valores maiores que zero;
while(not valido):
    valor = float(input('digite seu valor: '))
    if(not valor > 0):
        print('O valor deve ser maior que zero!')
        input('Digite o novo valor para continuar: ')
         # if ternario no Python, se for == 'nt (windows) executa cls senão clear
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        valido = True
        produtos['valor'] = valor  # - Todos os dados devem estar armazenados em um dicionário;
      
    







