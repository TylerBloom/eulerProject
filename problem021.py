#! /usr/bin/python

import fileinput
import math

a = []

for i in range(10001):
	a.append([])
	for n in range(i-1):
		if i % (n+1) == 0:
			if (n+1) != i:
				a[-1].append(n+1)	

sums = []

for i in range(len(a)):
	sums.append(0)
	for n in range(len(a[i])):
		sums[-1] += a[i][n]

amic = []

for i in range(len(sums)):
	if sums[i] <= len(sums):
		if i == sums[sums[i]] and i != sums[i]:
			amic.append(i)

aSum = 0

for i in amic:
	aSum += i

print aSum












