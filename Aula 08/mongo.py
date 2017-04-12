#!/usr/bin/python
# -*- coding: utf-8 -*-

from pymongo import MongoClient

client = MongoClient('127.0.0.1')

db = client['devops']

# db.fila.insert({"_id": 2, "servico": "internet","status": 0 })
# db.fila.insert({"_id": 3, "servico": "dns","status": 0 })

# db.fila.update({"_id": 1, "servico":"dns"},
# 			   	{"$set": {
# 			   		"status": 1
# 			   	}
# 			   })

for d in db.fila.find({}):
	print d