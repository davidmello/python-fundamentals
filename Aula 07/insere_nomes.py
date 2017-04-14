#!/usr/bin/python
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import requests
import random

# Lista de palvras randomicas
word_site = "https://svnweb.freebsd.org/csrg/share/dict/propernames?view=co&content-type=text/plain"

# Pega a lista de palavras randomicas
response = requests.get(word_site)
# Separa em linhas
WORDS = response.content.splitlines()
# Conta quantas linhas tem
total=len(WORDS)
# Gera um numero randomico baseado na qtde de linhas
randomico1=random.randint(0,total)
randomico2=random.randint(0,total)
randomico3=random.randint(0,total)
randomico4=random.randint(0,total)
randomico5=random.randint(0,total)
# Gera um outro numero randomico, baseado na qtde de registros no banco



engine = create_engine('sqlite:///banco2.db')
Base = declarative_base()
lista_usuarios = [WORDS[randomico1], WORDS[randomico2], WORDS[randomico3], WORDS[randomico4], WORDS[randomico5]]
class Usuario(Base):
	__tablename__ = 'usuarios'
	id = Column(Integer, primary_key=True)
	nome = Column(String)
	email = Column(String)

if __name__ == '__main__':
	Base.metadata.create_all(engine)
	Session = sessionmaker()
	Session.configure(bind=engine)
	session = Session()
	try:
		for nomes in lista_usuarios:
			oto_randomico=random.randint(0,total)
			email = "%s.%s@gmail.com" % (nomes, WORDS[oto_randomico])
			usuario = Usuario(nome="%s" % nomes, email="%s" % email.lower())
			session.add(usuario)
			session.commit()
		usuario = session.query(Usuario).all()
		# print usuario.nome, usuario.id
		for u in usuario:
			print "%s - %s" % (u.nome,u.email)

	except Exception as e:
		print e
		session.rollback()