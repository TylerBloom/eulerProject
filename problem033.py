#! /usr/bin/python

a = []

for i in range(10,100):
    i = str(i)
    for n in range(10,100):
        n = str(n)
        if float(n)/float(i) == 1:
            break
        if i[1] == '0' and n[1] == '0':
            break
        if i[0] == n[0]:
            try:
                if float(n)/float(i) == float(n[1])/float(i[1]):
                    a.append([n,i])
            except:
                pass
        elif i[0] == n[1]:
            try:
                if float(n)/float(i) == float(n[0])/float(i[1]):
                    a.append([n,i])
            except:
                pass
        elif i[1] == n[0]:
            try:
                if float(n)/float(i) == float(n[1])/float(i[0]):
                    a.append([n,i])
            except:
                pass
        elif i[1] == n[1]:
            try:
                if float(n)/float(i) == float(n[0])/float(i[0]):
                    a.append([n,i])
            except:
                pass

prod1 = 1
prod2 = 1

for i in a:
    prod1 *= float(i[0])
    prod2 *= float(i[1])

print prod1/prod2
        
