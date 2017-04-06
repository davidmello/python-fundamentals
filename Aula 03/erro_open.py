#!/usr/bin/python
# -*- coding: utf-8 -*-

try:
	with open("lista.txt", "r") as host:
		print host.readline():
			
except Exception as e:
	print "Erro %s" % e