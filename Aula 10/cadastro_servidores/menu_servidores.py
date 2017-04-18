#!/usr/bin/python


from lib.Servidores import *

while True:
    menu = '''     -= Sistema =-
        1) Cadastrar Servidor
        2) Remover Servidor
        3) Definir administrador
        4) Sair
         Selecione uma opcao: '''
    opcao = input(menu)
    try:
        if opcao == 1:
            cadastrar_servidor()
        elif opcao == 2:
            remover_servidor()
            continue
        elif opcao == 3:
            definir_administrador()
            continue
        else:
            print 'Ate logo'
            break
    except Exception as e:
        print e