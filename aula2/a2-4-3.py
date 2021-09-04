# Curso: Pyhton Fundamentos Proway
# Aula: Dia 3 - Parte 4 - 3
# Assunto: for
# Data: 2021-09-04


produto = {'nome':'cerveja','desc':'larger','cat':'bebida','valor':1.89}
# imprime todas as chaves do dicionário

for p in produto:
    print(produto[p])

print('\n')

# pegando as chaves e valores do dicionário:
for (chave, valor) in produto.items():
    print(chave, valor)

