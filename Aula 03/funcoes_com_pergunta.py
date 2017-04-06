#!/usr/bin/python
# -*- coding: utf-8 -*-

def soma(a, b=0):
	return a+b

def multiplica(a, b=1):
	return a*b

def divisao(a,b=1):
	return a/b

def subtracao(a,b=0):
	return a-b

numero1 = int(raw_input("Digite um numero: "))
numero2 = int(raw_input("Digite outro numero: "))
if not numero1:
	numero1 = 0
if not numero2:
	numero2 = 0

print "A soma dos números eh: " + str(soma(numero1, numero2))
print "A multiplicacao dos números eh: " + str(multiplica(numero1,numero2))
print "A divisão dos números eh: %i " % divisao(numero1, numero2)
print "A subtração dos números eh: %i " % subtracao(numero1, numero2)