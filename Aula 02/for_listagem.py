#!/usr/bin/python
# -*- coding: utf-8 -*-

listagem = ['maça', 'pera', 'uva', 'banana', 'melancia']

for valor in listagem:
	print valor
	if valor == 'pera':
		print "hmmmmm, pera!! Adoro pera!"
		#break

# insere no final da lista
listagem.append('kiwi')
print listagem

if 'maça' in listagem:
	print "Encontrei uma maça"


print listagem.count('melão')

# insere em uma posicao especifica
listagem.insert(2,'melão')
print listagem

print len(listagem)

# remove um item especifico
listagem.remove('maça')
print listagem

# remove o ultimo item da lista
listagem.pop()
print listagem

print len(listagem)

print "--------------------------------------------------------"

# Outro for, de palavra		
espaco = ' '
for VALORDAPALAVRA in 'PPYYTTHHOONN':
	um_espaco = '  '
	print espaco + VALORDAPALAVRA
	espaco = espaco + um_espaco
	