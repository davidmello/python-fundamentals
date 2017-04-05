#!/usr/bin/python

# modulo que nao mostra o que esta sendo digitado
import getpass

hostname = raw_input('Insira o IP do host: ')
user = raw_input('Entre com o Usuario: ')
password = getpass.getpass('... e agora a senha: ')

print "Acessando host %s:%s@%s" % (user,password,hostname)