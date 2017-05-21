#! /usr/bin/python

import fileinput
import math

a = []

for line in fileinput.input():
	line = line.strip()
	a.append([line])

finalLength = len(a)
toSort = []

for i in a:
	toSort.append(i)

length = len(toSort)

while len(toSort) != 1:
	new = []
	for n in range(len(toSort)/2):
		new.insert(0,[])
		while len(toSort[0]) != 0 and len(toSort[1]) != 0:
			if toSort[0][0] < toSort[1][0]:
				new[0].append(toSort[0][0])
				toSort[0].pop(0)
			else:
				new[0].append(toSort[1][0])
				toSort[1].pop(0)
		
		if len(toSort[0]) > 0:
			for i in range(len(toSort[0])):
				new[0].append(toSort[0][0])
				toSort[0].pop(0)
		else:
			for i in range(len(toSort[1])):
				new[0].append(toSort[1][0])
				toSort[1].pop(0)
		toSort.pop(0)
		toSort.pop(0)
	
	if len(toSort) != 0:
		for i in toSort:
			new.append(i)
	
	toSort = new

for i in toSort[0]:
	print i

