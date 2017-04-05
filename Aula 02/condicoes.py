#!/usr/bin/python
# -*- coding: utf-8 -*-

idade = int(raw_input('Qual a sua idade ? '))

if idade >= 18:
	estado = raw_input('Você está alcolizado ? (sim/nao) ').lower()
	if estado == 'nao':
		habilitacao = raw_input('Voce possui Habilitacao ? (sim/nao) ').lower()
		if habilitacao == 'sim':
			print "Tenha uma boa viagem!"
		elif habilitacao == 'nao':
			print "Você não pode dirigir, você não possui habilitação!! Carro apreendido e multa de R$200,00!"
		else:
			print "Digite apenas 'sim' ou 'não'"
	elif estado == 'sim':
		print "Você não pode dirigir, você está alcolizado... multa de R$1.900!"
	else:
		print "Digite apenas sim ou 'não'"
else:
	print "Você é menor de idade... com %s ano(s) não se pode dirigir dirigir!" % idade