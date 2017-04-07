#!/usr/bin/python
# -*- coding: utf-8 -*-

from paramiko.client import SSHClient

import paramiko

client = SSHClient()

client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

host = '192.168.202.11'
user = 'noturno'
passwd = '4linux'


client.connect(hostname=host, username=user, password=passwd)


stdin,stdout,stderr = client.exec_command('cat /etc/passwd2 | grep noturno')

if stderr.channel.recv_exit_status() != 0:
	print stderr.channel.recv_exit_status()
	print stderr.read()
else:
	print stdout.read()