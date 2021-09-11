# Curso: Pyhton Fundamentos Proway
# Aula: Dia 3 - Parte 4 - 1
# Assunto: Arquivos
# Data: 2021-09-11

# Primeiro argumento é o nome do arquivo, que pode ter o caminho da pasta
# o nome pode ter o caminho da pasta
# Segundo aqrquivo é o tipo de abertura
# 'x' - se o arquivo não existir, cria.
# Caso exista, ocorre um erro


arquivo = open('aula4/produto.txt', 'x')
arquivo.write('Produto 1')
arquivo.close()