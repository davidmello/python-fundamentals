#!/usr/bin/python

import os
import json
from lib.Usuarios import *

while True:
    menu = '''     -= Sistema =-
        1) Cadastrar Usuario
        2) Acessar Sistema
        3) Sair
         Selecione uma opcao: '''
    opcao = input(menu)
    try:
        if opcao == 1:
            cadastrar_usuario()
        elif opcao == 2:
            acessar_sistema()
            continue
        else:
            print 'Ate logo'
            break
    except Exception as e:
        print e