#!/usr/bin/python

import os
import json
from lib.Servidores import *

while True:
    menu = '''     -= Sistema =-
        1) Cadastrar Servidor
        2) Remover Servidor
        3) Sair
         Selecione uma opcao: '''
    opcao = input(menu)
    try:
        if opcao == 1:
            cadastrar_servidor()
        elif opcao == 2:
            remover_servidor()
            continue
        else:
            print 'Ate logo'
            break
    except Exception as e:
        print e