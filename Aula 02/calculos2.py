#!/usr/bin/python
# -*- coding: utf-8 -*-

num1 = int(raw_input("Digite o primeiro numero: "))
num2 = int(raw_input("Digite o primeiro numero: "))
tipo = raw_input("Digite o tipo de operacao: mult, div, sub, adic ou mod: ")


if tipo == "mult":
	print num1*num2
elif tipo == "div":
	print num1/num2
elif tipo == "sub":
	print num1-num2
elif tipo == "adic":
	print num1+num2
elif tipo == "mod":
	print num1%num2
else:
	print "Digite algo que faça sentido, cretino..."
