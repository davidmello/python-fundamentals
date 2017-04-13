#!/usr/bin/python

import psycopg2

class Conexao():
	@staticmethod
	def conectar(lista):
		con = psycopg2.connect(
			"host=%s dbname=%s user=%s password=%s" % lista
		)
		cur = con.cursor()
		return con, cur


class Banco():
	con = None
	cur = None

	def __init__(self, lista):
		self.con, self.cur = Conexao.conectar(lista)

	def find_one(self, id):
		self.cur.execute("SELECT * FROM posts WHERE id=%s" % id)
		return self.cur.fetchone()


	def update_one(self, id, conteudo):
 		self.cur.execute("UPDATE posts SET conteudo = '%s' WHERE id=%s" % (conteudo, id))
 		self.con.commit()

	def insert_one(self, titulo, conteudo):
		self.cur.execute("INSERT INTO posts (titulo,conteudo) VALUES ('%s', '%s')" % (titulo, conteudo))
		self.con.commit()

	def delete_one(self, id):
		self.cur.execute("DELETE FROM posts WHERE id='%s'" % id)
		self.con.commit()


lista = (('localhost', 'projeto', 'postgres', '123456'))
original = Banco(lista)
print original.find_one(34)

original.insert_one("novo titulo", "novo livro")

original.update_one(34,"agora um novo")

print original.find_one(34)

print original.find_one(33)
original.delete_one(33)
print original.find_one(33)



