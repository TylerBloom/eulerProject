#! /usr/bin/python

import fileinput
import math

n1 = [1]
n2 = [1]
a = [0]
count = 2 

while len(a) < 1000:
	if len(n1) > len(n2):
		n2.append(0)
	for i in range(len(n1)):
		a[i] = n1[i] + n2[i]
	if a[-1] > 9:
		a.append(0)
	for i in range(len(a)):
		if a[i] > 9:
			a[i] -= 10
			a[i+1] += 1

	n2 = []
	for i in n1:
		n2.append(i)	
	n1 = []
	for i in a:
		n1.append(i)

	count += 1

print count
print a
