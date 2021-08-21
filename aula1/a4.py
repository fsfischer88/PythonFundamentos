# Crie um sistema para cadastro de pessoa
# o sistema deve pedir o nome, idade e sexo
# cada dado deve ser armazenado em uma variável
# ao final, o programa deve imprimir uma com os dados do usuário

print('*'*10,'Sistema de Cadastro de Pessoas','*'*10)
print('\n')
nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
sexo = input('Digite seu sexo: ')
print('\n')
print( f'Seu nome é {nome} você tem {idade} anos e o seu sexo é {sexo}')