#! /usr/bin/python

import fileinput
import math

val = ""
count = 0
a = []

for list in fileinput.input():
    a.append([])
    for i in list:
        if i != " ":
            val += i
        if i == " " or i == "\n":
            val = int(val)
            a[count].append(val)
            val = ""
        if i == "\n":
            break
    count += 1

for i in range(1,len(a)):
    for n in range(len(a[i])):
        if a[i][n] + a[i-1][n] > a[i][n] + a[i-1][n+1]:
            a[i][n] = a[i][n] + a[i-1][n]
        else:
            a[i][n] = a[i][n] + a[i-1][n+1]

for i in a:
    print i

