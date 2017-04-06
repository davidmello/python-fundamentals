#!/usr/bin/python
# -*- coding: utf-8 -*-

f = lambda x,y,z: x + y + z
print f(1,2,10)


def size(words):
	return [len(w) for w in words]

palavras = ['pera', 'uva', 'mamao']
print size(palavras)

# em funcao lambda, trazendo ja a execucao do for
frutas = lambda words: [len(f) for f in palavras]
print frutas(palavras)

# retornando as palavras da lista, e ainda retornar em maiusculas
frutas = lambda words: [f[0].upper() for f in palavras]
print frutas(palavras)

# ==

def size2(words):
	lista = []
	for estados in words:
		lista.append(len(estados))
	return lista

print size2(palavras)