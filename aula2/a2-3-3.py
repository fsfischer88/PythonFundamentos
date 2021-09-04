
lista = ['Felipe']
tuplas = ['Felipe']
dicionario = {'nome':'Felipe','sobrenome':'Fischer','idade':32}

lista[0]
tuplas[0]

# Lendo os dados de um dicionário
print(dicionario['nome'])
print(dicionario['sobrenome'])
print(dicionario['idade'])

# Aterando dados de um dicionario
dicionario['nome'] = 'Joana'
dicionario['sobrenome'] = 'Nascimento'
dicionario['idade'] = 22

# Lendo os dados alterados
print(dicionario['nome'])
print(dicionario['sobrenome'])
print(dicionario['idade'])

# adicionando um novo conjunto de chave: valor
dicionario['cpf'] = '0555545646'
print(dicionario['cpf'])

cliente = {}
cliente2 = {'nome':'','sobrenome':'','idade':0}

cliente['nome'] = input('digite seu nome: ')
cliente['sobrenome'] = input('digite seu sobrenome: ')
cliente['idade'] = int(input('digite sua idade: '))

print(cliente)
# Deletando uma chave de um dicionário:
del(cliente['idade'])
print(cliente)


cliente2['nome'] = input('digite seu nome: ')
cliente2['sobrenome'] = input('digite seu sobrenome: ')
cliente2['idade'] = int(input('digite sua idade: '))

clientes = [cliente, cliente2]
print(clientes)
