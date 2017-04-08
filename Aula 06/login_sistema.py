#!/usr/bin/python
# -*- coding: utf-8 -*-

# modulo de conexao com postgresql
import psycopg2
import os
import getpass

# chama o meto de conexao e joga para a variavel con
con = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % ('localhost', 'projeto', 'postgres', '123456'))

cur = con.cursor()

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
		cur.execute("SELECT * FROM users WHERE usuario = '%s' AND senha = '%s'" % (usuario, senha))
		for linha in cur.fetchall():
			print "Usuario %s logado com sucesso \n\n\n" %linha[1]
			usuario_logado = True
		if cur.rowcount == 0:
			print "Usuário invalido, tente novamente."
	# Inserir Usuario
	elif pergunta == 2 and usuario_logado == True: 
		usuario=raw_input('digite o novo usuário: ')
		senha=getpass.getpass('digite a senha: ')
		try:
			cur.execute("insert into users(usuario, senha) values ('%s', '%s')" % (usuario, senha))
			if cur.rowcount:
				con.commit()
				print "usuário inserido com sucesso!"
				print "-----------------------------------------------------------------------------------"
		except Exception as e:
			print e
			con.rollback()
	# Buscar usuario
	elif int(pergunta) == 3 and usuario_logado == True:
		busca_titulo = raw_input('Qual usuário deseja buscar ?: ')
		cur.execute("select * from users where usuario like '%%%s%%'" % busca_titulo)
		for linha in cur.fetchall():
			print '%s' % linha[1]
		print "\t\t\t"
	elif int(pergunta) != 4 and usuario_logado == False:
			print "Antes de qualquer ação, por favor efetue o Login."
	else:
		teste = False
		usuario_logado = False
		print "Obrigado, volte sempre!"