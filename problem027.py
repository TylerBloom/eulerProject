#! /usr/bin/python

import fileinput
import math

ok = True
num = 0
count = 0
maxCount = 0

for b in range(1001):
	for a in range(1000):
		n = 0
		while ok:
			num = n*n + a*n + b
			if num > 1.0 :
				ceil = math.sqrt(num)
				i = 2
				while ok and i <= ceil:
					if num % i == 0:
						ok = False
					i += 1
			if ok:
				n += 1
				count += 1
		if count > maxCount:
			maxCount = count
			maxB = b
			maxA = a
		count = 0
		ok = True


print maxCount, maxA, maxB
