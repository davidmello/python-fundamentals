#!/usr/bin/python
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import requests
import random

engine = create_engine('sqlite:///banco3.db')
Base = declarative_base()

class Funcionario(Base):
	__tablename__ = 'funcionario'
	id = Column(Integer, primary_key=True)
	nome = Column(String)
	dependentes = relationship("Dependentes")


class Dependentes(Base):
	__tablename__ = 'dependentes'
	id = Column(Integer, primary_key=True)
	nome = Column(String)
	funcionario_id = Column(Integer, ForeignKey('funcionario.id'))


if '__name__' == '__main__':
	Base.metadata.create_all(engine)
	Session = sessionmaker()
	Session.configure(bind=engine)
	session = Session()

	try:
		funcionario = Funcionario(id=1, nome='Joaquim da Silva')
		session.add(funcionario)

		dependente1 = Dependentes(id=1, nome='Joaozinho')
		dependente2 = Dependentes(id=2, nome='Joaozinho')

		funcionario.dependentes.append(dependente1)
		funcionario.dependentes.append(dependente2)
		session.add(dependente1)
		session.add(dependente2)
		session.commit()

	except Exception as e:
		print e
		session.rollback()