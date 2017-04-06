#!/usr/bin/python
# -*- coding: utf-8 -*-


def func(valor):
	if valor:
		raise Exception('Deu Ruim')


try:
	numero = int(raw_input("insira um numero: "))
	numero2 = int(raw_input("insira um numero: "))
	print "A soma dos numeros eh: " + str(numero + numero2)
except Exception as e:
	pass
	#print "Voce precisa inserir um numero"
finally:
	print e
