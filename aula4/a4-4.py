# Curso: Pyhton Fundamentos Proway
# Aula: Dia 3 - Parte 4 - 1
# Assunto: Arquivos
# Data: 2021-09-11

# Primeiro argumento é o nome do arquivo, que pode ter o caminho da pasta
# o nome pode ter o caminho da pasta
# Segundo aqrquivo é o tipo de abertura
# 'r' - somente leitura


arquivo = open('aula4/categoria.txt', 'r')
# Readlines = cria uma lista de string com todas as linhas do arquivo
linhas = arquivo.readlines()

for l in linhas :
    l_sem_barra_n = l.strip() # Strip remove \n, \t e espacos em branco
    print(l_sem_barra_n)

# Fechando o arquivo
arquivo.close()