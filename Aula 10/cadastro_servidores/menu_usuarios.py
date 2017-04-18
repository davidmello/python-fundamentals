#!/usr/bin/python


from lib.Usuarios import *

while True:
    menu = '''     -= Sistema =-
        1) Cadastrar Usuarios
        2) Acessar Sistema
        3) Alterar Senha
        4) Sair
         Selecione uma opcao: '''
    opcao = input(menu)
    try:
        if opcao == 1:
            cadastrar_usuario()
        elif opcao == 2:
            acessar_sistema()
            continue
        elif opcao == 3:
            alterar_senha()
            continue
        else:
            print 'Ate logo'
            break
    except Exception as e:
        print e