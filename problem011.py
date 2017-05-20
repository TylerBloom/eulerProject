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
            val = float(val)
            a[count].append(val)
            val = ""
        if i == "\n":
            break
    count += 1
product = 0
biggest = 0

for i in range(len(a)):
    for n in range(len(a[i])):
        try:
             print a[i][n] * a[i][n+1] * a[i][n+2] * a[i][n+3]
        except:
            pass
        try:
            print a[i][n] * a[i+1][n] * a[i+2][n] * a[i+3][n]
        except:
            pass
        try:
            print a[i][n] * a[i+1][n+1] * a[i+2][n+2] * a[i+3][n+3]
        except:
            pass
        if n > 2:
            try:
                print a[i][n] * a[i+1][n-1] * a[i+2][n-2] * a[i+3][n-3]
            except:
                pass

