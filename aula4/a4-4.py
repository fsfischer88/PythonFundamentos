# Curso: Pyhton Fundamentos Proway
# Aula: Dia 3 - Parte 4 - 1
# Assunto: Arquivos
# Data: 2021-09-11

# Primeiro argumento é o nome do arquivo, que pode ter o caminho da pasta
# o nome pode ter o caminho da pasta
# Segundo aqrquivo é o tipo de abertura
# 'r' - somente leitura


arquivo = open('aula4/categoria.txt', 'r')
linhas = arquivo.readline()

for l in linhas :
    print(l.strip())

arquivo.close()