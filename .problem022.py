#! /usr/bin/python

import fileinput
import math

a = []

for line in fileinput.input():
	line = line.strip()
	a.append(0)
	for i in line.lower():
		a[-1] += ord(i) - 96

sum = 0

for i in range(len(a)):
	sum += (i+1) * a[i]

print sum


