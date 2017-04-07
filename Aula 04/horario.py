#!/usr/bin/python
# -*- coding: utf-8 -*-

from datetime import datetime, timedelta, date

#help(datetime)

# Dia de hoje - (X) dias
print datetime.now() - timedelta(7)

# Calcula os dias 
dias = str(datetime.now() - datetime(1981,11,13,8,15,0))

# faz a prova real, calcula se subtrair os dias, chega na data certa
print datetime.now() - timedelta(int(dias[:5]))


# Formatacao da data
antes = datetime(1981,11,13,8,15,0).strftime('%Y/%m/%d - %H:%m')

# Colocando entre conchetes
print "[" + antes + "]"
agora = datetime.now().strftime('%Y/%m/%d')


print datetime.now() + timedelta(
	days=4,
	seconds=1231,
	milliseconds=123,
	minutes=21,
	hours=4,
	weeks=1
	)


print date.today()
print dias + " desde que nasci"
print (datetime.now() - datetime(1981,11,13,8,15,0)).total_seconds()