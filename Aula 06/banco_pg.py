#!/usr/bin/python

# modulo de conexao com postgresql
import psycopg2
import os

from datetime import datetime
# import time

# chama o meto de conexao e joga para a variavel con
con = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % ('localhost', 'projeto', 'postgres', '123456'))

cur = con.cursor()


# Limpa a tela:
os.system('clear')
# data = datetime.now()
data = datetime.now()
while True:
	pergunta = raw_input('Voce deseja: \n \
	(1) Inserir um novo titulo \n \
	(2) Consultar a base completa ou \n \
	(3) Consultar um livro especifico: ?: \n \
	Pressione qualquer outra tecla para sair.')
	os.system('clear')
	# Inserir um novo titulo
	if int(pergunta) == 1:
		titulo=raw_input('digite o titulo: ')
		conteudo=raw_input('digite o conteudo: ')
		try:
			cur.execute("insert into posts(titulo, conteudo, date) values ('%s', '%s', '%s')" % (titulo, conteudo, data))
			if cur.rowcount:
				con.commit()
				print "registro inserido com sucesso!"
				print "-----------------------------------------------------------------------------------"
		except Exception as e:
			print e
			con.rollback()
	# Exibir o banco inteiro
	elif int(pergunta) == 2:
		cur.execute('select * from posts')
		print "ID\tTITULO\t\t\t\tCONTEUDO"
		for linha in cur.fetchall():
			print '%s\t%s\t\t\t-\t%s\t%s' % linha
		print "\t\t\t"
	# Buscar apenas um livro especifico (por trecho (like))
	elif int(pergunta) == 3:
		busca_titulo = raw_input('Qual titulo deseja buscar ?: ')
		cur.execute("select * from posts where titulo like '%%%s%%'" % busca_titulo)
		for linha in cur.fetchall():
			print '%s\t%s\t\t\t-\t%s\t%s' % linha
		print "\t\t\t"
	else:
		print "Obrigado, volte sempre!"
		break