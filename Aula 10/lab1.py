#!/usr/bin/python
# -*- coding: utf-8 -*-

def menu():
    menu = '''     -= Sistema =-
        1) Cadastrar usuario
        2) Acessar sistema
        3) Sair
         Selecione uma opcao: '''
    print menu

def cadastrar():
    global usuarios, senhas
    login = raw_input('Login: ')
    senha = raw_input('Senha: ')

    usuarios.append(login)
    senhas.append(senha)

def logar():
    global usuarios, senhas
    login = raw_input('Insira login: ')
    senha = raw_input('Insira a senha: ')
    
    if login in usuarios:
        if senhas[usuarios.index(login)] == senha:
            print 'Logado com sucesso!'
        else:   
            print 'Login ou senha invalidos'


usuarios = []
senhas = []

while True:
    menu = '''     -= Sistema =-
        1) Cadastrar usuario
        2) Acessar sistema
        3) Sair
         Selecione uma opcao: '''
    opcao = input(menu)
    try:
        if opcao == 1:
            cadastrar()
        elif opcao == 2:
            logar()
            continue
        else:
            print 'Ate logo'
            break
    except Exception as e:
        print e