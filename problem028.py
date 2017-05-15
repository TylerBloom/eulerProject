#! /usr/bin/python

import fileinput
import math

sum = 2
i = 2
shift = 0

while i*2 - 1 <= 1001:
	sum += (2*i-1)**2 - 0*(i+shift)
	sum += (2*i-1)**2 - 1*(i+shift)
	sum += (2*i-1)**2 - 2*(i+shift)
	sum += (2*i-1)**2 - 3*(i+shift)
	i += 1
	shift += 1

print sum
