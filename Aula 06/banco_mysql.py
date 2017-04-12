#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb
import requests
import random

# Lista de palvras randomicas
word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"

# Realiza a conexao com o banco
con = MySQLdb.connect(host="127.0.0.1", user="admin", passwd="4linux1234", db="projeto")
cur = con.cursor()



cur.execute("SELECT count(0) FROM posts")
result=cur.fetchone()
result=int(result[0])

# Executa um select
cur.execute("SELECT * FROM posts")

# Imprime as linhas
for registro in cur.fetchall():
	print registro

# insert
try:
	cur.execute("INSERT INTO posts (titulo, conteudo) VALUES ('teste1', 'teste2')")
	con.commit()
except Exception as e:
	con.rollback()

# Pega a lista de palavras randomicas
response = requests.get(word_site)
# Separa em linhas
WORDS = response.content.splitlines()
# Conta quantas linhas tem
total=len(WORDS)
# Gera um numero randomico baseado na qtde de linhas
randomico=random.randint(0,total)
# Gera um outro numero randomico, baseado na qtde de registros no banco
rando=random.randint(0,result)

# Atualiza um registro randomico com palavras randomicas
try:
	cur.execute("UPDATE posts SET titulo=\"%s\", conteudo=\"%s\" WHERE id=\"%s\"" % (WORDS[randomico], WORDS[randomico+rando], rando))
	# print cur._last_executed
	con.commit()
except Exception as e:
	print e
	con.rollback()