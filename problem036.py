#! /usr/bin/python

a = []
Sum = 0

for count in range(1000000): 
    if count % 2 == 1:
        i = str(count)
        test = ''
        length = len(i) - 1
        for n in range(len(i)):
            test += i[length-n]
        if test == i:
            b = format(int(i), 'b')
            test = ''
            length = len(b) - 1
            for n in range(len(b)):
                test += b[length-n]
            if test == b:
                a.append(int(i))

for i in a:
    Sum += i

print Sum
