# Curso: Pyhton Fundamentos Proway
# Aula: Dia 3 - Parte 4 - 1
# Assunto: Arquivos
# Data: 2021-09-11

# Primeiro argumento é o nome do arquivo, que pode ter o caminho da pasta
# o nome pode ter o caminho da pasta
# Segundo aqrquivo é o tipo de abertura
# 'w' - se o arquivo não existir, cria. Caso exista, sobreescreve

arquivo = open('aula4/Cliente.txt', 'w')
arquivo.write('Cliente1-ClientePF')
arquivo.close()