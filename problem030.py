#! /usr/bin/python

import fileinput
import math

a = []

for i in range(10,999999):
	string= str(i)
	sum = 0
	for n in string:
		sum += float(n)**5
	if sum == i:
		a.append(i)

print a

sum = 0

for i in a:
	sum += i

print sum
