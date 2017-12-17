#! /usr/bin/python

import math

maxChar = '9'

perms	= ['0']

for i in range(1,int(maxChar)+1):
	for n in range(len(perms)):
		for p in range(len(perms[0])+1):
			perms.append(perms[0][:p] + str(i) + perms[0][p:])
		del perms[0]

for i in perms:
	print i

