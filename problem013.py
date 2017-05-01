#! /usr/bin/python

import fileinput
import math

a = []

for line in fileinput.input():
	line = line.strip()
	a.insert(0,[])
	for i in line:
		a[0].append(int(i))

for n in range(len(a)-1):
	for i in range(len(a[1])):
		a[0][i] += a[1][i]
	a.pop(1)
	length = len(a[0])
	for i in range(length-1):
		if a[0][length-i-1] > 9:
			a[0][length-i-1] -= 10
			a[0][length-i-2] += 1
			
print a[0]


