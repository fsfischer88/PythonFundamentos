# Curso: Pyhton Fundamentos Proway
# Aula: Dia 3 - Parte 4 - 3
# Assunto: for
# Data: 2021-09-04


produto = {'nome':'cerveja','desc':'larger','cat':'bebida','valor':1.89}
produto2 = {'nome':'vodka','desc':'500ml','cat':'bebida','valor':18.99}

produtos_lista = [produto, produto2]

# imprimindo cada dicionário
for p in produtos_lista:
    print(p)

print('\n')
# imprimindo cada chave e valor dos dicionários de dentro da lista
for p in produtos_lista:
    for (c,v) in p:
        print(c,v)