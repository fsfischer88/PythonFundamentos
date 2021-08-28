# Crie um cadastro de clientes para uma loja de bebidas
# o cadastro deve solicitar ao usuário:
# Nome, Sobrenome e idade
# O sistema deve permitir apenas clientes maiores de idade
# Caso a idade seja menor, informa que não pode ser cadastrado

print('*'*10,'Bem vindo a loja Beber.com','*'*10)
print('\n')
nome = input('Digite seu nome: ')
sobrenome = input('Digite o seu sobrenome : ')
idade = int(input('Digite sua idade: '))

if(idade >= 18):
    print('Ok, cadastrado com sucesso!')
elif(idade > 0):
    print('Cadastro não permitido!')
else:
    print('Idade inválida')
