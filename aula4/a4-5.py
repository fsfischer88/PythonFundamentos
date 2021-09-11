# Curso: Pyhton Fundamentos Proway
# Aula: Dia 3 - Parte 4 - 1
# Assunto: Arquivos
# Data: 2021-09-11


with open('aula4/teste.txt', 'w',encoding='utf-8') as arquivo:
    arquivo.write("Não precisa colocar o .close()")


with open('teste.txt', 'r') as arquivo:
    linhas = arquivo.readlines()
    for l in linhas :
        l_sem_barra_n = l.strip() # Strip remove \n, \t e espacos em branco
        print(l_sem_barra_n)