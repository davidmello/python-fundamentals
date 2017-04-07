#!/usr/bin/python

# modulo de conexao com postgresql
import psycopg2

from datetime import datetime

# chama o meto de conexao e joga para a variavel con
con = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % ('localhost', 'projeto', 'postgres', '123456'))

cur = con.cursor()

data = datetime.now()

cur.execute("insert into posts(titulo, conteudo) values ('titulo1', '%s')") % str(data)

con.commit()