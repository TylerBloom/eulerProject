#! /usr/bin/python

import fileinput
import math

a = [1]

for i in range(100):
	for n in range(len(a)):
		a[n] *= i+1
	t = 0
	lastIndex = len(a) - 1
	while t < len(a) :
		if a[lastIndex - t] > 9 and t == lastIndex:
			a.insert(0,0)
			lastIndex = len(a) - 1

		while a[lastIndex - t] > 9:
			a[lastIndex - t] -= 10
			a[lastIndex - t -1] += 1
		t += 1

sum = 0

for i in a:
	sum += i

print sum
