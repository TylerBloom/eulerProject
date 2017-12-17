#! /usr/bin/python

import math

t = float(10**12)
b = float(0.5 + math.sqrt(0.25 + (t*(t-1))/2))

while (b/t)*((b-1)/(t-1) != 0.5):
	t = t+1
	b = float(0.5 + math.sqrt(0.25 + float((t*(t-1)))/2))
print long(b), t
