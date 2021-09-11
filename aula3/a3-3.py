# Curso: Pyhton Fundamentos Proway
# Aula: Dia 3 - Parte 3 - 3
# Assunto: Funções
# Data: 2021-09-11

import os

# imprimir cabecalho
def imprimir_cabecalho():
    os.system('clear')
    print('*'*10,'Bem vindo a loja Beber.com','*'*10)
    print('\n')

# entrada usuário    
def cadastra_usuario():
    nome = input('Digite seu nome: ')
    sobrenome = input('Digite o seu sobrenome : ')
    idade = int(input('Digite sua idade: '))
    usuario = {'nome': nome, 'sobrenome':sobrenome, 'idade':idade}
    return usuario

# validacao de cadastro
def valida_usuario(idade):
    if(idade >= 18):
        print('Ok, cadastrado com sucesso!')
    elif(idade > 0):
        print('Cadastro não permitido!')
    else:
        print('Idade inválida')

imprimir_cabecalho()
u = cadastra_usuario()
valida_usuario(u['idade'])
