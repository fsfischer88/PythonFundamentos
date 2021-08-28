
# Repetições While



# idade = int(input('Digite sua idade: '))

# invalido = True
# while(invalido):
#     if(idade >= 18):
#         print('Ok, cadastrado com sucesso!')
#         invalido = False
#     elif(idade > 0):
#         print('Cadastro não permitido!')
#         invalido = False
#     else:
#         print('Idade informada é inválida')
#         idade = int(input('Digite sua idade novamente: '))
import os

invalido = True
while(invalido):
    print('*'*10,'Sistema de bebidas','*'*10,'\n')
    print('\t1-Cadastrar uma bebida')
    print('\t2-Listar bebidas cadastradas')
    print('\t0-Sair')
    opcao = int(input('\tDigite uma opção no menu: '))

    if(opcao <0 or opcao >2):
        print('Opção é inválida!')
        input('Digite enter para continuar...')
        os.system('clear')
    else:
        invalido = False


        
