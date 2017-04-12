#!/usr/bin/python
# -*- coding: utf-8 -*-

# modulo de conexao com postgresql
from pymongo import MongoClient
import os
import getpass
import sys


# chama o meto de conexao e joga para a variavel con
client = MongoClient('127.0.0.1')
db = client['devops']

teste = True
usuario_logado = False

# Limpa a tela:
os.system('clear')
# data = datetime.now()

while teste:
	# Menu
	pergunta = int(raw_input('Voce deseja: \n \
	(1) Logar \n \
	(2) Inserir Usuário \n \
	(3) Buscar Usuário: \n \
	(4) Sair \n \
	Digite sua opção: '))
	os.system('clear')
	# Efetuar Login
	if pergunta == 1:
		usuario=raw_input('Usuario: ')
		senha=getpass.getpass('Senha: ')
		usuario_senha = {"user": usuario, "pass": senha}
		for linha in db.users.find(usuario_senha):
			#for linha in db.users.find({}):
			# print linha
			print linha['user']
			print "Usuario logado com sucesso \n\n\n"
			usuario_logado = True
		# except Exception as d:
		# 	print d
		# if cur.rowcount == 0:
		# 	print "Usuário invalido, tente novamente."
	# Inserir Usuario
	elif pergunta == 2 and usuario_logado == True: 
		usuario=raw_input('digite o novo usuário: ')
		senha=getpass.getpass('digite a senha: ')
		novo_usuario = {"user": usuario, "pass": senha }
		try:
			db.users.insert(novo_usuario)
			print "usuário inserido com sucesso!"
			print "-----------------------------------------------------------------------------------"
		except Exception as e:
			print e
	# Buscar usuario
	elif int(pergunta) == 3 and usuario_logado == True:
		busca_titulo = raw_input('Qual usuário deseja buscar ?: ')
		busca_usuario = {"user": busca_titulo }
		for linha in db.users.find(busca_usuario):
			print linha['user'] + "|" + linha['pass']
		print "\t\t\t"
	elif int(pergunta) != 4 and usuario_logado == False:
			print "Antes de qualquer ação, por favor efetue o Login."
	else:
		teste = False
		usuario_logado = False
		print "Obrigado, volte sempre!"