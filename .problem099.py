#! /usr/bin/python

import fileinput
import math

list = []
count = 0

for line in fileinput.input():
	line = line.strip()
	if count % 2 == 0:
		list.append([int(line)])
	else:
		list[-1].append(int(line))
	count += 1

a = list[0][0]
n = list[0][1]
index = 0

for q in range(len(list)):	
	b = list[q][0]
	i = list[q][1]
	if (n)/(math.log(b, a)) < i:
		a = b
		n = i
		index = q

print index + 1
	
	


