# Curso: Pyhton Fundamentos Proway
# Aula: Dia 2 - Parte 3
# Assunto: Listas, Tuplas, Dicionários
# Data: 2021-08-28-m 'Aula2 - parte 2 - While'

bebidas = ['Coca-Cola','Skol','Cachaça','Água']
print(bebidas)
print( bebidas[1] ) # segundo elemento da lista
print( bebidas[3] ) # quarto elemento da lista
print( bebidas[1:] ) # do segundo elemento até o final da lista
print( bebidas[:3] ) # do inicio ate o terceiro elemento da lista

bebidas.append('Corona')
print(bebidas)
bebidas[3] = 'Vodka'
print(bebidas)
bebidas.remove('Skol')
print(bebidas)
bebidas.pop(-1) # deleta o último elemento
print(bebidas)
ultima_bebida = bebidas.pop(-1)
print(ultima_bebida)
print(bebidas)
#inserir
bebidas.insert(0,'Refri') # Serve para inserir um elemento em uma determinada posição
bebidas.insert(2,'Cafe')
print(bebidas)
# deleta um dado ou intervalo de dados de uma lista
del(bebidas[1:3])
print(bebidas)

