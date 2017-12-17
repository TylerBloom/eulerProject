#! /usr/bin/python

string = ""

for i in range(1,1000000):
	string += str(i)
	if len(string) >= 1000000:
		break

s = "." + string

product = 1

for i in range(7):
	product *= int(s[10**i])

print product
