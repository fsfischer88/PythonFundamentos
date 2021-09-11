# Curso: Pyhton Fundamentos Proway
# Aula: Dia 3 - Parte 4 - 1
# Assunto: Arquivos
# Data: 2021-09-11

# Primeiro argumento é o nome do arquivo, que pode ter o caminho da pasta
# o nome pode ter o caminho da pasta
# Segundo aqrquivo é o tipo de abertura
# 'a' - se o arquivo não existir, cria.
# Caso exista, adiciona o conteúdo no final do arquivo


arquivo = open('aula4/categoria.txt', 'a')
arquivo.write('Categoria 1\n') # Utiliza \n para pular de linha
arquivo.close()