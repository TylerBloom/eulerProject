#! /usr/bin/python

import fileinput
import math

vals = []

for a in range(2,101):
	for b in range(2,101):
		vals.append(a**b)
toSort = []

for i in vals:
        toSort.append([i])

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

sorted = toSort[0]
i = 0
length = len(sorted)

while i < length-2:
	if sorted[i] == sorted[i+1]:
		del sorted[i]
		i -= 1
		length -= 1
	i += 1

print len(sorted)


