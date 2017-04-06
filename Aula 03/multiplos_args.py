#!/usr/bin/python
# -*- coding: utf-8 -*-


def conta_animais(*args):
	conta = len(args)
	print conta
	print args



conta_animais('um', 'dois', 'tres')


def somaOsAnimais(*args,**kwargs):
	print kwargs
	print args


somaOsAnimais(2,3,tigre=2,leao=3)