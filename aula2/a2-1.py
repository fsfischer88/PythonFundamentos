# Curso: Pyhton Fundamentos Proway
# Aula: Dia 2 - Parte 1
# Assunto: If, else, elif
# Data: 2021-08-28


idade = -18

# maior de idade > 18
# o Python trabalha com o conceito do tab e ":"
if(idade >= 18):
    print('Maior que 18')
else:
    if(idade > 0):
        print('Menor que 18')
    else:
        print('Idade inválida')

    if(idade >= 18):
        print('Maior que 18')
    elif(idade > 0):
        print('Menor que 18')
    else:
        print('Idade inválida')
